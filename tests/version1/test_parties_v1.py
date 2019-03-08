import unittest
from tests.version1.base_test import BaseTest
from tests.version1.helpers import party1,party2
import tests.version1.helper_methods as hm

class TestParties(BaseTest):
    def test_create_party(self):
        response= hm.create_party(self, party1)
        self.assertEqual(response.status_code,201)
    
    def test_get_all_parties(self):
        hm.create_party(self, party1)
        hm.create_party(self, party2)
        response = self.client.get("/api/v1/offices")
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()