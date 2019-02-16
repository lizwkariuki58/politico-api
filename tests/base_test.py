from unittest import TestCase

from run import app 
from app.version1.models import offices
from app.version1.models import parties

class BaseTestCase(TestCase):
    def setUp(self):
        client = app.test_client()
        self.client = client

    def tearDown(self):
        parties.clear()
        offices.clear()