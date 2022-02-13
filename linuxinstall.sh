echo 'WELCOME TO THE LINUX INSTALLER'
sleep(2)
echo '[*]INSTALLING REQUIREMENTS'
chmod +x pythonbadwordsbypass.py
pip install -r requirements.txt
sleep(2)
echo '[*]FINISHED'
echo 'Do you want to run the program? y/n'
read launch
if $launch == "y"
then
echo '[*] Running'
python3 pythonbadwordbypass.py
elif $launch ==  'n'
then
echo '[!] exit....'
sleep(2)
exit
else
echo 'Check your syntax'
sleep(2)
exit
fi

