from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('hello.html', list_of_names=['Mike', 'John', 'Adam'])


@app.route("/<string:name>")
def greet(name):
    return f'<h1>Hello {name}</h1>'


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
