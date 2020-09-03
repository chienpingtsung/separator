import glob
import os
import shutil
from collections import deque

from flask import Flask, send_from_directory, request

app = Flask(__name__)

image_file_name = glob.glob('origin/*.bmp')
image_file_name = [os.path.basename(i) for i in image_file_name]
image_file_name = deque(image_file_name)
operations = deque()

if not os.path.exists('target/'):
    os.mkdir('target/')
sub_dir = ['{}/'.format(i) for i in range(10)] + ['space/']
for i in sub_dir:
    if not os.path.exists('target/' + i):
        os.mkdir('target/' + i)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/name')
def name():
    return {
        'name': image_file_name[-1] if image_file_name else ''
    }


@app.route('/origin/<path:image_name>')
def origin(image_name):
    return send_from_directory('origin/', image_name)


@app.route('/mv', methods=['POST'])
def mv():
    json = request.get_json()
    if json['dst'] == 'undo':
        if not operations:
            return {
                'status': 403
            }
        name, dst = operations.pop()
        try:
            shutil.move(
                'target/{}/{}'.format(dst, name),
                'origin/{}'.format(name)
            )
            image_file_name.append(name)
        except FileNotFoundError:
            return {
                'status': 404
            }
        return {
            'status': 200
        }
    else:
        try:
            name = image_file_name.pop()
            if name != json['name']:
                raise Exception("致命错误")
            shutil.move(
                os.path.join('origin/', json['name']),
                'target/{}/{}'.format(json['dst'], json['name'])
            )
            operations.append((json['name'], json['dst']))
        except FileNotFoundError:
            return {
                'status': 404
            }
        return {
            'status': 200
        }
