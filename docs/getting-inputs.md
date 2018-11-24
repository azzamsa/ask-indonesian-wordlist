# Getting input files

This document describe how I get the input files for Indoensian LanguagePack.

:rotating_light: Take a note that I don't use these input files from now. The result
from small amount of wikipedia article just make the value ambious. I
need bunch more of Indonesian article to mimic the usage value of real
word. I will try to use indoensian dumps from wikipedia if I have time
in near future.

## Take wikipedia entry

I use the featured article in Indonesian wikipedia. e.g 'Kematian
Muhammad', 'filsafat budi'

- Take the source of the article in wikimedia format then parse to plain text using pandoc.

``` bash
pandoc -f mediawiki -t plain -s data.txt  -o hasil-pandoc.txt
```

- Remove reference, see also and unused part (manual)
- Remove punctuation and cluttered word using
  [remove.py](/script/python/remove_punctuation.py)

Take a note that this version is very basic. You can use
string.punctuation from python library for better approach.


