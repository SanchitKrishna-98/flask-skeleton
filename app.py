from flask import Flask

app = Flask(__name__)

@app.get('/')
def hello() -> str:
    return 'Hello, Flask Skeleton!'

@app.get('/sanchit')
def sanchit() -> str:
    return 'I am Sanchit'

@app.get('/about')
def about() -> str:
    return 'This is the About page of the Flask Skeleton application.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=0, debug=True)
