"""
    python app.py
"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Wilmington Web Devs!"

if __name__ == "__main__":
    app.run(debug=True)
