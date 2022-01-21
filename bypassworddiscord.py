import os
import sys
import time
import pyfiglet

word = ""
banner = pyfiglet.figlet_format("DISORD BLACKLISTED WORDS BYPASS 2022")

print(banner)
print("Fast, simple EDUCATIONAL PURPOSE ONLY")
word = str(input("[*] Type the word you want to bypass: "))

def startprocess():

    if "a" in word:
        word.replace('a', '\u0430') 

    if "c" in word:
        word.replace('c', '\u03F2')

    if "e" in word:
        word.replace('e', '\u0435')

    if "o" in word:
        word.replace('o', '\u043E')

    if "p" in word:
        word.replace('o', '\u0440')

    if "s" in word:
        word.replace('s', '\u0455')

    if "d" in word:
        word.replace('d', '\u0501')
    
    if "q" in word:
        word.replace('q', '\u051B')

    if "w" in word:
        word.replace('w', '\u051D')

    #print the result
    
    print("[*] Porcess succefully finished!")

    print("[*] COPY AND PAST THIS WORD: ", word)

if word == "":
    print("[!] Please type the word")
else:
    startprocess()
