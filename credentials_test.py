'''
import uniittest to create uniittests for credential module
import Password Locker Module to be tested (Credential in this case)
'''
import unittest
from credentials import Credantials

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential Class behaviours

    '''
    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        # Create credential object
        self.new_credential = Credantials("kim","Lewis","munene")

    def tearDown(self):
        '''
            tears down / cleans up data for every variable after the case tests are
         over for each method
        '''
        Credantials.credential_list = []

    def test_init(self):
        '''
            checks if the initialization of varaibles are handled properly
        '''
        self.assertEqual( self.new_credential.user_password, "kim")
        self.assertEqual( self.new_credential.account_name, "Lewis" )
        self.assertEqual( self.new_credential.account_password, "munene" )

    def test_save_credential(self):
        '''
            test case to ensure credentials are saved
        '''
        # Save the new credential
        self.new_credential.save_credentals()

        self.assertEqual( len(Credantials.credential_list), 2)

    def test_save_multiple_credentials(self):
        '''
            test case to ensure multiple users are saved
        '''
        # Save the new credential
        self.new_credential.save_credentals()

        test_credential = Credantials("lewis","munene","123")

        test_credential.save_credentals()

        self.assertEqual( len(Credantials.credential_list), 4)

    def test_gen_pass(self):
        '''
            test case to ensure random passwords are generated for credentials
        '''
        generated_password = self.new_credential.gen_pass()

        self.assertEqual( len(generated_password), 8 )

    def test_display_credential(self):
        '''
        test case for display credential method
        '''
        # Save the new credential
        self.new_credential.save_credentals()

        test_credential = Credantials("lewis","munene","123")

        test_credential.save_credentals()

        test_credential = Credantials("lewis","irimu","123")

        test_credential.save_credentals()

        self.assertEqual( len(Credantials.display_credential("lewis")) ,4 )

    def test_delete_credential(self):
        '''test if the delete method works'''
        #self.new_credential.delete_credential()
        test_credential = Credantials("ken","more","1234")#create a credential
        test_credential.save_credentals()#save it
        test_credential = Credantials("joe","brown","1234")#create anothercredential so that te list has two
        test_credential.save_credentals()#save it as well

        test_credential.delete_credentials()#delete one

        self.assertEqual(len(Credantials.credential_list),3)# check if there is one remaining to confirm if the delete method works



    def test_credential_exist(self):
        '''
        test case to ensure credentials in question exist
        '''
        # Save the new credential
        self.new_credential.save_credentals()

        test_credential = Credantials("lewis","munene","123")

        test_credential.save_credentals()

        # use contact exist method
        credentials_exist = Credantials.credentials_exist("Lewis")

        self.assertTrue(credentials_exist)


if __name__ == '__main__':
    unittest.main(verbosity=2)
