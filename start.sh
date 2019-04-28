#!/bin/bash
LOGS=~/abacus_start_logs.txt
export FLASK_APP=~/code/puller/puller.py

echo -e "\n$(date) starting puller" >> "$LOGS"
~/code/puller/venv/bin/flask run --host=0.0.0.0 --port=8080 >> "$LOGS" 2>&1
