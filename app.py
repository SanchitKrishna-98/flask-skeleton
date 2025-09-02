from flask import Flask

app = Flask(__name__)

@app.get('/')
def hello() -> str:
    return 'Hello, Flask Skeleton!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
