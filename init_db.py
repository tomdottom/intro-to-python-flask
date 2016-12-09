#!/usr/bin/env python

from app import app, db, Member


def init_db(db):
    db.create_all()

    tom = Member('Tom', 'Marks')
    matt = Member('Matt', 'Eckmann')

    db.session.add(tom)
    db.session.add(matt)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        init_db(db)
