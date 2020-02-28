import os
import shutil

from flask import Flask, send_from_directory, request

app = Flask(__name__)

image_file_name = os.listdir('origin/')

if not os.path.exists('j/'):
    os.mkdir('j/')
if not os.path.exists('k/'):
    os.mkdir('k/')
if not os.path.exists('space/'):
    os.mkdir('space/')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/name')
def name():
    return {
        'name': image_file_name.pop()
    }


@app.route('/origin/<path:image_name>')
def origin(image_name):
    return send_from_directory('origin/', image_name)


@app.route('/mv')
def mv():
    shutil.move(
        os.path.join('origin/', request.form['name']),
        os.path.join(request.form['dst'], request.form['name'])
    )
    return {
        'status': 200
    }
