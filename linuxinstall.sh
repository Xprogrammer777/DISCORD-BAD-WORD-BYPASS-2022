#!/bin/bash

echo 'LINUX INSTALL SCRIPT'
sleep 2
echo '[*] Installing requirements...'
chmod +x bypassworddiscord.py
pip install --upgrade pip
pip install -r requirements.txt
sleep 2
echo '[*] Installation completed (or requirements already satisfied)'
echo 'Do you want to run the program? y/n'
read launch
if [ $launch == "y" ]
then
echo '[*] Running...'
python3 bypassworddiscord.py
elif [ $launch ==  'n' ]
then
echo '[!] Exit....'
sleep 2
exit
else
echo '[!] Check your syntax! (Case sensitive "y" or "n")'
sleep 2
exit
fi

