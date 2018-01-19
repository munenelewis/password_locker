import unittest
from user import User

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

if __name__ == '__main__':
    unittest.main()