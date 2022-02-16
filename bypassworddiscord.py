import os
import sys
import time
import pyfiglet

word = ""
banner = pyfiglet.figlet_format("DISCORD BLACKLISTED WORDS BYPASS 2022")

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
    #looking the code? I will add other IDN, but not homograph, because some words are not "bypassed"

    #print the result
    
    print("[*] Porcess succefully finished!")
    
    time.sleep(1)

    print("[*] COPY AND PASTE THIS WORD: ", word)

if word == "":
    time.sleep(1)
    print("[!] Please type a word")
else:
    print("[*] Starting...")
    time.sleep(1)
    startprocess()
