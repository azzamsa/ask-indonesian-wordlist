import string
import re

INPUT_FILE = "kompas.1gram"

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


def scale_between(unscaled_num):
    min_allowed = 1
    max_allowed = 255
    min_value = 271
    max_value = 795050
    return int((max_allowed - min_allowed) * (unscaled_num - min_value) / (max_value - min_value) + min_allowed)

def create_list():
    result = ""
    data = clean_list()
    for line in data.split('\n'):
        words = line.split(',')
        if words != ['']:
            kata = words[0]
            skala = words[1]
            skala_scaled = scale_between(int(skala))
            result += '<w f=\"' + str(skala_scaled) + '">'+ str(kata) +'</w>\n'
    return result

def write_file(result):
    file = open("hasil.xml","w")
    file.write(result)
    file.close()


if __name__ == "__main__":
    result = create_list()
    write_file(result)
