import requests, html2text

word = str(input("Enter a verb in latin: "))
r = requests.get('https://www.dizionario-latino.com/dizionario-latino-italiano.php?parola='+word)

line = []
for c in r.text:
    if c!='\n':
        line.append(c)
    else:
        if "paradigma" in "".join(line):
            print(html2text.html2text("".join(line)), end="")
            break
        line = []
