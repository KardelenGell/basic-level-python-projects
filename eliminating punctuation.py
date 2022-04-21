# Kardelen Gel - 181805057

newText= ""
oldText = str(input("Please, write the text: "))

import string

for x in oldText:
    if x not in string.punctuation:
        newText += x

print(newText)