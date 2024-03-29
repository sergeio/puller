import subprocess

import git
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/abacus_push', methods=['GET', 'POST'])
@app.route('/abacus-push', methods=['GET', 'POST'])
def push_event():
    js = request.get_json()
    if js.get('ref') == 'refs/heads/master':
        # In [9]: g = git.Git('~/code/')
        # In [10]: g.clone('git@github.com:sergeio/abacus.git')
        # Out[10]: u''
        repo = git.Repo('~/code/abacus')
        info = repo.remote().fetch()
        repo.git.reset('--hard', 'origin/master')

        # Restart abacus and frontend
        p = subprocess.Popen(
            ['pkill', '-f', 'abacus/venv/bin/python.*flask run'],
            stdout=subprocess.PIPE)
        _, __ = p.communicate()
        subprocess.Popen(['ensure_abacus_running.sh'])

        p = subprocess.Popen(
            ['pkill', '-f', 'npm'],
            stdout=subprocess.PIPE)
        _, __ = p.communicate()

        subprocess.Popen(['ensure_frontend_running.sh'])

        if info:
            return 'Pulled branch successfully: ' + info[0].name, 200
        return 'Master push with no info. Maybe pulled?', 400
    return 'Ignoring non-master push: ' + js.get('ref', ''), 304
