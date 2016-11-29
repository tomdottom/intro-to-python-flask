"""
    python app.py
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello Wilmington Web Devs!"


@app.route("/hello/<name>")
def hello(name):
    return "Hello {}!".format(name)


@app.route("/tada/<name>")
def tada(name):
    name = name[0].upper() + name[1:]
    return render_template(
        "tada.html",
        name=name
    )


if __name__ == "__main__":
    app.run(debug=True)
