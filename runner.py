import os
import argparse
import configparser

from collections import Counter


class BuildParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            '-c', '--config_file', type=str, help='Path to config file', default='config.conf')
        self.parser.set_defaults(**self.read_config())
        self.args = self.parser.parse_args()

    def read_config(self) -> dict:
        '''
        > Reads the config file and returns a dictionary of default values
        :return: A dictionary of the default values from the config file.
        '''
        # ?: Read config file
        args = self.parser.parse_args()
        config = configparser.ConfigParser()
        config.read(args.config_file)

        # ? Read default values from config file
        defaults = {}
        defaults.update(dict(config.items('Defaults')))
        return defaults


class TextSanitizer(BuildParser):
    def __init__(self):
        super().__init__()
        self.file_path = self.args.source
        self.is_file_available(self.file_path)
        result = self.sanitize_input(self.sanitize())
        print(f'Sanitized text: \n{result}\n', '-' * 100)
        self.simple_stats(result)
        self.write_to_file(result)

    def sanitize(self) -> str:
        '''
        It opens the file, reads the contents, and passes it to the `sanitize_input` function
        :return: The sanitized input.
        '''
        with open(self.file_path, 'r') as f:
            return self.sanitize_input(f.read())

    def is_file_available(self, file_path: str) -> None:
        '''
        > This function raises a `FileNotFoundError` if the file path passed to it does not exist

        :param file_path: The path to the file you want to check
        :type file_path: str
        '''
        if os.path.isfile(file_path) is False:
            raise FileNotFoundError(f'File not found: {file_path}')

    def sanitize_input(self, input_string: str) -> str:
        '''
        > This function sanitizes the input string by removing all the spaces and converting all the characters to lowercase

        :param input_string: The input string to sanitize
        :type input_string: str
        :return: The sanitized string
        :rtype: str
        '''
        input_string = input_string.replace('tab', '____')
        return input_string.lower().replace(' ', '')

    def simple_stats(self, input_string: str) -> None:
        '''
        > This function prints the simple stats of the input string

        :param input_string: The input string to get the stats of
        :type input_string: str
        '''
        print(f'Length of the input string: {len(input_string)}')
        print(f'Number of unique alphabet: {len(set(input_string))}')
        print('Number of each alphabet:')
        for k, v in Counter(input_string).items():
            print(f'> {k}: {v}')

    def write_to_file(self, output_string: str) -> None:
        '''
        > This function writes the output string to a file

        :param output_string: The output string to write to a file
        :type output_string: str
        '''
        if not os.path.exists(self.args.location):
            os.makedirs(self.args.location)

        with open(os.path.join(self.args.location, self.args.target), 'w') as f:
            f.write(output_string)


if __name__ == '__main__':
    TextSanitizer()
