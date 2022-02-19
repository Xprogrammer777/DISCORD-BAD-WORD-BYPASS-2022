#!/bin/bash

RED='\033[1;31m'
NC='\033[0m'

printf "${RED}LINUX INSTALL SCRIPT${NC}\n"
sleep 2
echo '[*] Installing requirements...'
pip install --upgrade pip
pip install -r requirements.txt
echo '[*] Installing...'
chmod +x bypassblacklist.py
alias bypass='python3 ~/DISCORD-BAD-WORD-BYPASS-2022/bypassblacklist.py'
sleep 2
printf "${RED}[*] Installation completed (or requirements already satisfied)${NC}\n"
echo 'Do you want to run the program? y/n'
read launch
if [ $launch == "y" ]
then
echo '[*] Running...'
python3 bypassblacklist.py
elif [ $launch ==  "n" ]
then
echo '[!] Exit....'
sleep 2
exit
else
echo '[!] Check your syntax, wrong input! (Case sensitive "y" or "n")'
sleep 1
echo '[!] QUITTING!'
sleep 2
exit
fi

