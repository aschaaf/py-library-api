from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return 'Server is working...'


@app.route('/ping')
def ping():
    return 'Hello from Server'
