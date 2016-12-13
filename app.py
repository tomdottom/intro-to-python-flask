"""
    python app.py
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tmp.db'
db = SQLAlchemy(app)


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(80), unique=True)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '%r %r' % (self.first_name, self.last_name)


@app.route("/")
def index():
    members = Member.query.all()
    return render_template(
        'index.html.j2',
        a_single_var='A big hello from the organisers!',
        a_list=members,
        a_dict={'first': 'Uncle', 'last': 'Bob'}
    )


if __name__ == "__main__":
    app.run(debug=True)
