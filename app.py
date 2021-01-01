import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>AAAAAAAAAAAd</h1>"

@app.route("/about")
def about():
    return "<h1>BBBBBBBBBBBBBBBBBBBb</h1>"

if __name__ == "__main__":
    app.run()