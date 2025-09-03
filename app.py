from flask import Flask

app = Flask(__name__)

@app.get('/')
def hello() -> str:
    return 'Hello, Flask Skeleton!'

@app.get('/sanchit')
def sanchit() -> str:
    return 'I am sanju'

@app.get('/about')
def about() -> str:
    return 'This is the About page of the Flask Skeleton application.'

@app.get('/home')
def home() -> str:
    return 'This is my home'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
