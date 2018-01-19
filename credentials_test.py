import unittest
from credentials import Credantials

class TestCredantials(unittest.TestCase):
    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.new_credentials = Credantials("munene","123") #create contact
    def tearDown(self):
        """
        allow clean up after each test
        """
        Credantials.credential_list=[]

       
    def test_init(self):
        
        '''
        check if object is initialized propery
        '''

        self.assertEqual(self.new_credentials.account_name,"munene")
        self.assertEqual(self.new_credentials.account_password,"123")

#test if you can save 

    def test_save_credentals(self):
        """test if the object has been saved into the contact list"""
        self.new_credentials.save_credentals()#saving the contact
        self.assertEqual(len(Credantials.credential_list),1)

#test to see if you can save multiple credentials
    def test_save_multiple_credentials(self):
        '''
        test multiple credentials 
        '''

        self.new_credentials.save_credentals()
        test_credentials = Credantials("wyne","222")
        test_credentials.save_credentals()
        self.assertEqual(len(Credantials.credential_list),2)

if __name__ == '__main__':
    unittest.main()

#  def test_save_multiple_credentials(self):
#         '''
#          to check if we can save multiple contact
#         objects to our credential_list
#         '''
#         self.new_credentials.save_credentals()
#         test_credentials= Credantials("Test","user") # new contact
#         test_credentials.save_credentals()
#         self.assertEqual(len(Credantials.credential_list),2)