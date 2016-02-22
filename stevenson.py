#!/usr/bin/env python

import os, sys
from flask import Flask, Response, send_file, jsonify, abort, request
from repos import repos

app = Flask(__name__)
log = True


# Basic hook handler
@app.route('/repo/<owner>/<name>/info', methods=['GET'])
def repo_get(owner, name):
    if log: print('repo_get({},{})'.format(owner, name))
    this_repo = repos[owner][name]

    return jsonify(this_repo)

# Basic root handler
@app.route('/', methods=['GET'])
def root():
    return 'sorry, you have reached a URL that is no longer in service'


@app.after_request
def add_header(response):
    # Force upstream caches to refresh at 100 minute intervals
    response.cache_control.max_age = 100
    # Enable CORS to allow cross-domain loading of tilesets from this server
    # Especially useful for SeaDragon viewers running locally
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(processes=3, host='0.0.0.0')
    print('welcome to Stevenson')