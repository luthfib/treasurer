# We do this so that we can take advantage of async code from gevent
from gevent import monkey
monkey.patch_all()

import os

import requests
from flask import Flask, request

api_port = os.environ['PORT']
api_url = f'http://slow_api:{api_port}/'

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello there"


if __name__ == "__main__":
    app.run()