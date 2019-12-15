import unittest
from credential import User
from credential import Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for users

    Args
    unittest.TestCase to run before each test cases
    '''

    def setUp(self):
        '''
        Tear down method that does clean up after all test have been run
        '''
        User.user_list = [] 
