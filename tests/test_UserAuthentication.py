'''The test ensures that
1. username is entered
2. password is entered
4. password and email are correct
'''
import unittest

class UserAuthentication(unittest.TestCase):
    
    def test_email_not_empty(self):
        result = userLogin("","pass")
        self.assertEqual(result,'Please enter your username')
    
    def test_password_not_empty(self):
        result = logIn("someone@mail.com","")
        self.assertEqual(result,'Please enter your password')    
    
    def test_test_email_and_username_correct(self):
        result = logIn("someone@mail.com","password")
        self.assertEqual(result,'Authentication rejected')

if __name__ == '__main__':
    unittest.main()