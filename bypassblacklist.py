#Report any issue on Github.

import os
import sys
import time
import pyfiglet

# Note : the str "word" is only the raw input by user, it will not change...
word = ""
banner = pyfiglet.figlet_format("DISCORD BLACKLISTED WORDS BYPASS 2022")

print(banner)
print("A tool by Xprogrammer777")
word = str(input("[*] Type the word you want to bypass: "))

def startprocess():

    if "a" in word:
        bypassed = word.replace('a', '\u0430') 

    if "c" in word:
        bypassed = word.replace('c', '\u03F2')

    if "e" in word:
        bypassed = word.replace('e', '\u0435')

    if "o" in word:
        bypassed = word.replace('o', '\u043E')

    if "p" in word:
        bypassed = word.replace('p', '\u0440')

    if "s" in word:
        bypassed = word.replace('s', '\u0455')

    if "d" in word:
        bypassed = word.replace('d', '\u0501')
    
    if "q" in word:
        bypassed = word.replace('q', '\u051B')

    if "w" in word:
        bypassed = word.replace('w', '\u051D')

    #print the result
    
    print("[*] Porcess succefully finished!")
    
    time.sleep(1)

    print("[*] COPY AND PASTE THIS WORD: ", bypassed)

if word == "":
    time.sleep(1)
    print("[!] Please type a word")
else:
    print("[*] Starting...")
    time.sleep(1)
    startprocess()
