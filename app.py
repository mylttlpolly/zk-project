from flask import Flask, request, render_template
from flask import request

from utils import validate

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/voting', methods=['POST'])
def func():
    data = request.form
    valid = validate(data['user'])
    result = 'ok' if valid else 'not ok'
    return {'result': result}, 200
