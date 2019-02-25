import unittest
from tests.base_test import BaseTest
from tests.helpers import party1,party2,office1, office2

class TestParties(BaseTest):
    def test_create_party(self):
        response=self.client.post("/api/v1/parties", data=party1)
        self.assertEqual(response.status_code,200)
    
    def test_get_all_parties(self):
        self.client.post("/api/v1/offices", data=office1)
        self.client.post("/api/v1/offices", data=office2)
        response = self.client.get("/api/v1/offices/")
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()