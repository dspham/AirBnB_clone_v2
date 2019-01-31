#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return "Python {:s}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number_check(n):
    return "{:d} is a number".format(int(n))

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run()
