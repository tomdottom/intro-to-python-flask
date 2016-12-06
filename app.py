"""
    python app.py
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html',
        a_single_var='All hail the organisers!',
        a_list=['Tom', 'Matt'],
        a_dict={'first': 'Uncle', 'last': 'Bob'}
    )


if __name__ == "__main__":
    app.run(debug=True)
