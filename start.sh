#!/bin/bash
LOGS=~/puller_start_logs.txt
export FLASK_APP=~/code/puller/puller.py

echo "\n\$(date) starting puller" >> "$LOGS"
~/code/puller/venv/bin/flask run --host=0.0.0.0 --port=3003 2>&1 >> "$LOGS"
