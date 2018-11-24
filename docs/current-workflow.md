# My current workflow

This document describe the steps I took to make Indonesian wordlist
for Anysoftkeyboard

## Getting the sources

- [kbbi.web.id](https://kbbi.web.id/)
- [ardwort/freq-dist-id](https://github.com/ardwort/freq-dist-id)
- [geovedi/indonesian-wordlist](https://github.com/geovedi/indonesian-wordlist)

I use words from [kbbi web](/raw_data/kbbi-web.txt). Geovedi also had
kbbi list, but kbbi has more complete list. I also use
[kompas.1gram](/raw_data/kompas.txt) and
[idwiki.1gram](/raw_data/idwiki.txt) from adwort.

## Tidy up the sources

### Remove digit, punctuation, one char only, and sites

I use `r"\d+"` to move digit all together. Before I use
`r"\d{2}/\d{2}/\d{4}` for date format and `r"\d+/\d+/\d+"` but it's
better to remove any digit from dictionary. We don't have digit vocab :).

``` python
def clean_list():
    result = ""
    digit_re = r"\d+"
    sites_re = r".com$|.org$|.net$|.io$"

    with open(INPUT_FILE) as file:
        for line in file:
            words = line.split()
            word = str(words[0])
            if ((not any(re.match(regex, word) for regex in [digit_re, sites_re])) and
            len(word)>1 and word != string.punctuation):
                result += ','.join(words) + '\n'

        return result

```

### Make a xml word list

min_allowed and max_allowed are default value in android
dictionary. min_value and max_value are specified according to your
list frequency value. Take the highest and the lowest value.

Data source example:

``` text
yang	975156
dan	964511
di	917963
pada	438597
```

``` python
def scale_between(unscaled_num):
    min_allowed = 1
    max_allowed = 255
    min_value = 271
    max_value = 795050
    return int((max_allowed - min_allowed) * (unscaled_num - min_value) / (max_value - min_value) + min_allowed)

def create_list():
    result = ""
    data = clean_list()
    for line in data.split('\n'):  # read line by line
        words = line.split(',')    # separate word and frequency
        if words != ['']:          # don't read the blank lines
            kata = words[0]
            skala = words[1]
            skala_scaled = scale_between(int(skala))
            result += '<w f=\"' + str(skala_scaled) + '">'+ str(kata) +'</w>\n'
    return result
```

The complete script for this is [convert2xml](/script/python/convert2xml.py)

:tada: In this step you have ready to use Indonesian wordlist for
Anysoftkeyboard. But I have additional step to make better wordlist.


## Merge list between 'kompas.1gram' and 'idwiki.1gram' (manually)

Merge two list and remove duplicate.

``` python
def merge_files():
    idwiki = []
    kompas = []
    result = ""
    with open('idwiki.txt') as idwiki_file, open('kompas.txt') as kompas_file:
        for line in idwiki_file:
            words = line.split()
            idwiki.append(words)

        for line in kompas_file:
            words = line.split()
            kompas.append(words)

    # remove duplicate word
    merged_words = [x for x in idwiki if not x in kompas]
    for line in merged_words:
        result += ','.join(line) + '\n'
    return result
```

The script I use for this is [merge_list.py](/script/python/merge_list.py)

## Remove non official word (slank word)

Since the initial word is coming from kompas and wikipedia. There a
lot of unofficial word (slank word). So I have to pick only the
official one.

### Remove clutter items from kbbi e.g digit inside parens

``` python
import re
replaced = ""
with open('kbbi-web.txt') as file:
    for line in file:
        replaced += re.sub('\([^)]*\)', '', line)

    file = open("replaced.txt","w")
    file.write(replaced)
    file.close()
```
The script I use for this is [rm_paren.py](/script/python/rm_paren.py)

### Pick word if match the word from kbbi

I use kbbi from [kbbi-web-id](/raw_data/kbbi-web.txt)

``` python
def pick_kbbi():
    '''take kkbi words only'''''
    kbbi_only = []
    kbbi_ku = []
    kbbi_mising = []
    result = ""
    with open('kbbi-only.txt') as kbbi_only_file, open('kbbi-ku.txt') as kbbi_ku_file:
        for line in kbbi_only_file:
            words = line.rstrip('\n').split(',')
            kbbi_only.append(words[0])

        for line in kbbi_ku_file:
            words = line.rstrip().split('\n')
            kbbi_ku.append(' '.join(words))

    # pick only kbbi words
    for item in kbbi_ku:
        if item not in kbbi_only:
            result += str(item) + '\n'

    return result
```

The script I use for this is [pick_only_kbbi.py](/script/python/pick_only_kbbi.py)

## Add missing KBBI words

Since the initial source only 1gram of the big chunk. I add missing
kbbi word to them.

It has the same logic as removing slank word from the wordlist.

## Add missing result to wordlist (manually)

I put the missing result for 'missing kbbi word' below the wordlist
that have 'real' frequency. Then I give them the value of 1 in their frequency.

## Remove prefix word

Since Indonesian language had a lot of prefix words. e.g "meng-, me-,
pe-". I remove them. I think it's not that useful to put them in
wordlist.

``` python
def remove_awalan():
    result = ""
    with open('kbbi-missing.txt') as kbbi_missing_file:
        for line in kbbi_missing_file:
            words = line.split()
            if ''.join(words)[-1] != '-':
                result += ' '.join(words) + ',1\n' # add the value of one (dummy value)
        return result
```

The script I use for this is [remove_awalan.py](/script/python/remove_awalan.py)

## Create final wordlist

This has the same logic as 'Make a xml word list'

# Autotext wordlist

I get use [Wikipedia:Daftar kosakata bahasa Indonesia yang sering_salah dieja](https://id.wikipedia.org/wiki/Wikipedia:Daftar_kosakata_bahasa_Indonesia_yang_sering_salah_dieja)
for autotext wordlist.

- Take the wikimedia format.
- Create the list from them using simple python script.

# Note

Beware of the slicing `foo[0]` in those script. Double check that
there no word missing.
