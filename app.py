from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print('in post')
    elif request.method == 'GET':
        print('in get')
    else:
        print(f'or in {request.method}')
    return 'Hello, world!'