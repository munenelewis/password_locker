import unittest
from user import User
from credentials import Credantials


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the user class behaviour"""

    
    def setUp(self):
        """run before the test"""
        self.new_user = User("lewis","munene","munenei")#create user object

    def tearDown(self):
        '''
        it does clean up after very test
        '''
        User.user_list=[]

    def test_init(self):
        """test if initialized properly"""

        self.assertEqual(self.new_user.first_name,"lewis")
        self.assertEqual(self.new_user.last_name,"munene")
        self.assertEqual(self.new_user.password,"munenei")


#save contact

    def test_save_contact(self):
        """
        testing is user is being save in the user object
        """
        self.new_user.save_user() #save the new user
        self.assertEqual(len(User.user_list),1)

    def test_multiple_user(self):
        '''
        multiple users save
        '''
        self.new_user.save_user()
        test_user = User("milly","molly","moe")#new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_find_credential(self):
        '''
        check if user object is saved into the user list
        '''
        self.new_user.save_user()
        test_user = User('lewis','munene','munenei')
        test_user.save_user()
        found_credential = User.find_credential('kim')
        self.assertEqual(found_credential, False)

    def test_user_exist(self):
        
        self.new_user.save_user()
        test_user = User('lewis','munene','munenei')
        test_user.save_user()

        user_exists = User.user_exist('lewis')
        self.assertTrue(user_exists)

    def test_log_in(self):
        self.new_user.save_user()
        test_user = User('lewis','munene','munenei')
        test_user.save_user()
        found_credential = User.log_in('lewis','munene','munenei')
        self.assertEqual(found_credential, Credantials.credential_list)

    def test_display_user(self):
        self.assertEqual( User.display_user() , User.user_list )
if __name__ == '__main__':
    unittest.main(verbosity=2)