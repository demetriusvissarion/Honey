from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hi 🎃</h1>'


@app.route("/<string:name>")
def greet(name):
    return f'<h1>Hello {name}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
