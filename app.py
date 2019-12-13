from flask import Flask, request, render_template
from flask import request

from utils import validate

app = Flask(__name__)


@app.route('/', methods=['GET'])
def voting():
    return render_template('page.html')


@app.route('/final', methods=['GET'])
def final():
    return render_template('final.html')


@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')


@app.route('/voting', methods=['POST'])
def func():
    data = request.form
    valid = validate(data['user'])
    return {'valid': valid}, 200
