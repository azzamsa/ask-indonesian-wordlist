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

    for item in kbbi_ku:
        if item not in kbbi_only:
            result += str(item) + '\n'

    return result

def write_file(result):
    file = open("kbbi-missing.txt","w")
    file.write(result)
    file.close()


if __name__ == "__main__":
    result = pick_kbbi()
    write_file(result)
