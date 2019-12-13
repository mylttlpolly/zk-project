from flask import Flask, request, render_template
from flask import request

from utils import validate

app = Flask(__name__)


@app.route('/')
def voting():
    return render_template('page.html')


@app.route('/final')
def final():
    return render_template('final.html')


@app.route('/voting', methods=['POST'])
def func():
    data = request.form
    valid = validate(data['user'])
    result = 'ok' if valid else 'not ok'
    return {'result': result}, 200
