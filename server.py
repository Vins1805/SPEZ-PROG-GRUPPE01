from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/info')
def info():
    return 'Hello HTW'


app.run(host='0.0.0.0', port=4000)
