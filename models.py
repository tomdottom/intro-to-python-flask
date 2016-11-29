from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80), unique=True)
    last = db.Column(db.String(120), unique=True)

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return '%r %r' % (self.first, self.last)
