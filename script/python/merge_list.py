def merge_list():
    idwiki = []
    kompas = []
    result = ""
    with open('idwiki.txt') as idwiki_file, open('kompas.txt') as kompas_file:
        for line in idwiki_file:
            words = line.split()
            idwiki.append(words)
        #print(idwiki)

        for line in kompas_file:
            words = line.split()
            kompas.append(words)
        #print(kompas)

    merged_words = [x for x in idwiki if not x in kompas]
    for line in merged_words:
        result += ','.join(line) + '\n'
    return result


def write_file(result):
    file = open("merged.txt","w")
    file.write(result)
    file.close()


if __name__ == "__main__":
    result = merge_files()
    write_file(result)
