import os
import unittest
import tempfile

import app
from init_db import init_db


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.tmp_filename = tempfile.mkstemp()
        app.app.config['SQLALCHEMY_DATABASE_URI'] = (
            'sqlite:///' + self.tmp_filename)
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.tmp_filename)

    def test_index_renders_member(self):
        with app.app.app_context():
            init_db(app.db)

        response = self.app.get('/')

        assert 200 == response.status_code
        assert 'Tom' in response.data
        assert 'Matt' in response.data

if __name__ == '__main__':
    unittest.main()
