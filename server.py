from flask import Flask, jsonify, request
from project.main import *

app = Flask(__name__)


@app.route('/info')
def info():
    return 'Hello HTW'


@app.route('/show_customers')
def show_customers():
    return customer1.toJSON()


app.run(host='0.0.0.0', port=4000)
