import unittest
from tests.base_test import BaseTest
from tests.helpers import office1,office2,office3, office4

class TestOffices(BaseTest):
    def test_create_offices(self):
        response = self.client.post("/api/v1/offices", data=office1)
        self.assertEqual(response.status_code,200)

    def test_create_offices_does_not_work_without_json_data(self):
        response = self.client.post("api/v1/offices", data=office4)
        self.assertEqual(response.status_code,400)
        self.assertIn(b'Bad Request, Input all your data in JSON format.',response.data)

    def test_create_offices_does_not_work_with_invalid_data(self):
        response = self.client.post("api/v1/offices", data=office3)
        self.assertEqual(response.status_code,400)
        self.assertIn(b'Bad Request, Update all fields of your JSON data',response.data)

    def test_get_all_offices(self):
        self.client.post("/api/v1/offices", data=office1)
        self.client.post("/api/v1/offices", data=office2)
        response = self.client.get("/api/v1/offices")
        self.assertEqual(response.status_code,200)
  
    def test_get_specific_office(self):
        self.client.post("api/v1/offices", data=office1)
        response = self.client.get("api/v1/offices")
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()