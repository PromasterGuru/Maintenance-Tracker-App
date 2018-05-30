'''Test covers
Test whether a request is modified
'''
import unittest

class UserModifyRequest(unittest.TestCase):
    
    def test_not_modified(self):
        result = modifyRequest(request)
        self.assertEqual(result,"Request modification failled")
        
    def test_request_modified(self):
        result = modifyRequest(request)
        self.assertNotEqual(result,"Request modified successfully")
    
if __name__ == '__main__':
    unittest.main()