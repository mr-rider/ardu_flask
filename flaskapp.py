# flaskapp.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run(host='0.0.0.0')


@app.route("/")
def index():
    return "<h1>The temperature is 30.5 C</h1>"


if __name__=="__main__":
    app.run(host='0.0.0.0')