from turtle import clear
import unittest
from app import app
import unittest


class RatesTest(unittest.TestCase):
    def get_testeing_api(self):
        return '/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main'

    def test_api_connection(self):
        tester = app.test_client(self)
        response = tester.get(self.get_testeing_api())

        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_response_content_type(self):
        tester = app.test_client(self)
        response = tester.get(self.get_testeing_api())
        self.assertEqual(response.content_type, "application/json")

    def test_response_data(self):
        tester = app.test_client(self)
        response = tester.get(self.get_testeing_api())
        self.assertTrue(
            b'average_price' in response.data and b'day' in response.data)


if __name__ == "__main__":
    unittest.main()
