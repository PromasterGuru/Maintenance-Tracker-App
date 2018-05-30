'''
This app tests users who have no requests

'''
import unittest
import requests
import json
import sys

class TestAllUserRequests(unittest.TestCase):

    def test_user_with_no_requests(self):
        result = requests.get('http://127.0.0.1:5000/api/v1/getAllRequests/3')
        self.assertEqual(
            result.json(), {"requests": "No requests found for this user"})

if __name__ == '__main__':
    unittest.main()
