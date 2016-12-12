import os
import unittest
import tempfile

from app import app, db
from init_db import init_db


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()
        self._create_tmp_db()
        with app.app_context():
            self._initalise_db(db)

    def _create_tmp_db(self):
        self.db_fd, self.tmp_filename = tempfile.mkstemp()
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            'sqlite:///' + self.tmp_filename)

    def _initalise_db(self, db):
        db.create_all()
        init_db(db)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.tmp_filename)

    def test_index_renders_member(self):

        response = self.test_client.get('/')

        assert 200 == response.status_code
        assert 'Tom' in response.data
        assert 'Matt' in response.data
