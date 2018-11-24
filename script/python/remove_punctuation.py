def remove_punctuation():
    result = ""
    data = ""
    with open("hasil-pd.txt") as file:
        data = file.read()
        # remove corresponding char
        for r in (("(", ""), (")", ""),
                  ("[", ""), ("]", ""),
                  ("_", " "), ("|", " "),
                  (",", " "), (".", " "),
                  (" ", " "), ('"', ''),
                  ("{", ""), ("}", ""),
                  ("–", " "), (";",""),
                  ("''", ""), ('""',""),
                  (":", ""), ("/",""),
                  ("SM", ""), ("CE",""),
                  ("ke-", ""), ("---", "")):
            data = data.replace(*r)
        # remove digit
        data = ''.join([w for w in data if not w.isdigit()])
        # remove if sigle char only
        data = ' '.join( [w for w in data.split() if len(w)>1] )

    file = open("hasil-py.txt","w")
    file.write(data)
    file.close()

remove_punctuation()
