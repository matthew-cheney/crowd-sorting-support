from flask import Flask, request
import pickle

print('initializing app')
app = Flask(__name__)

print('defining routes')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print('in post')
    elif request.method == 'GET':
        print('in get')
    else:
        print(f'or in {request.method}')
    print(f'request: {request}\n'
          f'json: {request.json}\n'
          f'form: {request.form}\n'
          f'data: {request.data}')

    return 'Hello, world!'

print('done')
