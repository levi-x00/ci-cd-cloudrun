import app
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        # Make your assertions
        assert 'OK' in result._status

if __name__ == '__main__':
    unittest.main()