import string
from random import choice


class Credantials :
    '''class of the credentials'''
    credential_list = []

    def __init__(self,user_password, credential_name,credential_password):
        self.credential_name = credential_name
        self.credential_password = credential_password
        self.user_password = user_password


    def save_credentals(self):
        """save credentials saves credentials in the credential list"""

        Credantials.credential_list.append(self)

        Credantials.credential_list.append(self)
    def delete_credential(self):
        '''
        method to delete a credential from the credential user_list
        '''
        Credantials.credential_list.remove(self)

    @classmethod
    def find_credential(cls,credential_name):
        """
        method must take in a name and return a name that matches that name
        """
        for credentials in cls.credential_list:
            if credentials.credential_name == credential_name:
                return credential_name

      

    @classmethod
    def credentials_exist(cls,credential_name):
        """
        checking if the name exist

        """
        for credentials in cls.credential_list:
            if credentials.credential_name == credential_name:
                return True
        return False
    
    @classmethod
    def display_credential(cls,password):
        """
        displaying all contacts 

        """
        user_credential_list = []

        for credentials in cls.credential_list:
            if credentials.user_password == password:
                user_credential_list.append(credentials)

        return user_credential_list
     

    @classmethod
    def gen_pass(cls):
        '''
        gen random number
        '''

        size = 8
        #generate random aphanumeris
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase
        #create password
        password = ''.join( choice(alphanum) for num in range(size) )
        return password

if __name__ == '__main__':
    unittest.main(verbosity=2)
