import json
import unittest
from tests.version1.base_test import BaseTest
from tests.version1.helpers import office1,office2,office3, office4
import tests.version1.helper_methods as hm

class TestOffices(BaseTest):
    def test_create_offices(self):
        response = hm.create_office(self, office1)
        self.assertEqual(response.status_code,201)

    #Fix this test, it tests for invalid data not lack of json data
    def test_create_offices_does_not_work_without_json_data(self):
        response = self.client.post ("/api/v1/offices", data= office4)
        self.assertEqual(response.status_code,400)
       

    def test_create_offices_does_not_work_with_invalid_data(self):
        response = hm.create_office(self,office3)
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