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

#initialize       
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


#deleting credentials
    def test_delete_credentials(self):
        """
        test to see if i can delete a credential
        """
        self.new_credentials.save_credentals()
        test_credentials = Credantials("wyne","222")
        test_credentials.save_credentals()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credantials.credential_list),1)
    def test_find_credential_by_name(self):
        """
        test to see if we can dinf contact by name and display the details
        """
        self.new_credentials.save_credentals()
        test_credentials = Credantials("wyne","222")#add a new credential
        test_credentials.save_credentals()

        found_credentials = Credantials.find_by_name("wyne")

        self.assertEqual(found_credentials.account_name,test_credentials.account_name)

#test if the object really exist 
    def test_credetials_exist(self):
         """
         to check if the credential really exist 
         """
         self.new_credentials.save_credentals()
         test_credentials = Credantials("wyne","222")
         test_credentials.save_credentals()

         credentials_exist = Credantials.credentials_exist("wyne")
         self.assertTrue(credentials_exist)
#display all contacts 
    def test_display_all_credentials(self):
        """
        method to display all the contacts 
        """
        self.assertEqual(Credantials.display_credentials(),Credantials.credential_list)

if __name__ == '__main__':
    unittest.main()