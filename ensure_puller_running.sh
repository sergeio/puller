#!/bin/bash
# ensures puller is running

# Make symlink in /usr/bin
# make executable

process='/root/code/puller/venv/bin/python /root/code/puller/venv/bin/flask run'
makerun="/root/code/puller/start.sh"

if ps ax | grep -v grep | grep "$process" > /dev/null
then
    exit
else
    "$makerun" &
fi

exit
