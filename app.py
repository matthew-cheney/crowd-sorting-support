from flask import Flask, request

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
    return 'Hello, world!'

print('done')
