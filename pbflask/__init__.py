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
    with open('req_pickle.pkl', 'wb') as f:
        pickle.dump(request, file=f)
    return 'Hello, world!'

print('done')
