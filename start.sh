#!/bin/bash
export FLASK_APP=~/code/puller/puller.py
~/code/puller/venv/bin/flask run --host=0.0.0.0 --port=3003 2>&1 >> ~/puller_start_logs.txt
