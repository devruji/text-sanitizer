# text-sanitizer
long-write-text-sanitizer

## Requirements
|                     | My version (dev)           |
|---------------------|----------------------------|
| Python              | 3.10                       |

*P.S. I think, we can use less than this version krub*

## Get Started
```bash
git clone https://github.com/devruji/text-sanitizer.git

python runner.py
```

## Example result
```bash
> python runner.py

Sanitized text: 
loremipsumdolorsitamet,consecteturadipiscingelit,seddoeiusmodtempor____incididuntutlaboreetdoloremagnaaliqua.volutpatblanditaliquametiameratvelitscelerisqueindictumnon.aliquetsagittisidconsecteturpurusutfaucibuspulvinarelementum.sedodiomorbiquiscommodoodioaeneansed____adipiscingdiam.accumsantortorposuere____acutconsequatsemper.
 ----------------------------------------------------------------------------------------------------
Length of the input string: 329
Number of unique alphabet: 22
Number of each alphabet:
> l: 14
> o: 25
> r: 16
> e: 32
> m: 17
> i: 32
> p: 9
> s: 21
> u: 24
> d: 18
> t: 27
> a: 25
> ,: 2
> c: 15
> n: 17
> g: 4
> _: 12
> b: 4
> q: 6
> .: 5
> v: 3
> f: 1
```