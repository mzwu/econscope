from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>It works!!!!!!!</h1>"


@app.route("/covid")
def covid_view():
    return "<h2>covid page</h2>"
