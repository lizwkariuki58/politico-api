from tests.base_test import BaseTest
from tests.test_helpers import office1,office2,office3

class TestOffices(BaseTest):
    def test_create_office(self):
        result = self.client.post("api/v1/offices", data=office1)
        self.assertEqual(result.status_code,200)

    def test_get_all_offices(self):
        self.client.post("/api/v1/offices", data=office1)
        self.client.post("/api/v1/offices", data=office2)
        response = self.client.get("/api/v1/offices")
        self.assertEqual(response.status_code,200)
