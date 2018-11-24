def remove_awalan():
    result = ""
    with open('kbbi-missing.txt') as kbbi_missing_file:
        for line in kbbi_missing_file:
            words = line.split()
            if ''.join(words)[-1] != '-':
                result += ' '.join(words) + ',1\n'
        return result

def write_file(result):
    file = open("kbbi-tanpa-awalan_with_value.txt","w")
    file.write(result)
    file.close()


if __name__ == "__main__":
    result = remove_awalan()
    write_file(result)
