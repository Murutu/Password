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
        Setup method to run before each test
        '''
        self.new_user = User("Murutu","Peter","murutu@peter.com","P100")

    def tearDown(self):
        '''
        Tear down method that does clean up after all test have been run
        '''
        User.user_list = []

    def test_init(self):
        '''
        To test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Murutu")
        self.assertEqual(self.new_user.last_name,"Peter")
        self.assertEqual(self.new_user.email,"murutu@peter.com")
        self.assertEqual(self.new_user.password,"P100")    

    def test_save_user(self):
        '''
        test_save_user test case to test if user is saved in user is saved in user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple users in user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","murutu@peter.com","p100")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_all_user(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_user(), User.user_list) 

class TestCredential(unittest.TestCase):

    def setUp(self):
        '''
        setup method to run before each test
        '''
        self.new_credential = Credential("Murutu","murutu@peter.com","p100")

    def test_init(self):
        '''
        To test if object is initialized properly
        '''
        self.assertEqual(self.new_credential.username,"Murutu")
        self.assertEqual(self.new_credential.email,"murutu@peter.com")
        self.assertEqual(self.new_credential.password,"p100")

    def test_save_credential(self):
        '''
        Test_save_credential to check if credentials are saved in credentials in credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        '''
        teardown method that does clean up after all test have been run
        '''
        Credential.credential_list = []

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Murutu","murutu@peter.com","p100")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_email(self):
        '''
        Test to check if we can find credential by email and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Murutu","murutu@peter.com","p100")
        test_credential.save_credential()

        found_credential= Credential.find_by_email("murutu@peter.com")
        self.assertEqual(found_credential.email,test_credential.email)

    def test_credential_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the credential.
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Murutu","murutu@peter.com","p100")
        
        credential_exists = Credential.credential_exists("murutu@peter.com")
        
        self.assertTrue(credential_exists)

    def display_credential(self):
        '''
        method that returns a list of credentials saved
        '''
        self.assertEqual(Credential.display_credential(), Credential.credential_list)

if __name__ == "__main__":
    unittest.main()                       

       


