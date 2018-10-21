from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('newroute')
def new_route():
    return 'This is a new route'


if __name__ == '__main__':
    app.run()
