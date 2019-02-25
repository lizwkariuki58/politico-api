from unittest import TestCase

from app import create_app 
from instance.config import app_config
from app.version1.models.models import offices
from app.version1.models.models import parties

class BaseTest(TestCase):
    def setUp(self):
        self.app=create_app('testing')
        self.client = self.app.test_client()


    def tearDown(self):
        #parties.clear()
        #offices.clear()
        pass