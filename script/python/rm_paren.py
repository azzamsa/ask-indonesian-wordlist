import re
replaced = ""
with open('kbbi-web.txt') as file:
    for line in file:
        replaced += re.sub('\([^)]*\)', '', line)

    file = open("replaced.txt","w")
    file.write(replaced)
    file.close()
