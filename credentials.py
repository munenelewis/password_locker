class Credantials :
    '''class of the credentials'''
    credential_list = []
    def __init__(self, account_name,account_password):
        self.account_name = account_name
        self.account_password = account_password

    def save_credentals(self):
        """save credentials saves credentials in the credential list"""

        Credantials.credential_list.append(self)
    def delete_credentials(self):
        """delete credentials from credential list """
        Credantials.credential_list.remove(self)


    @classmethod
    def find_by_name(cls,name):
        """
        method must take in a name and return a name that matches that name
        """
        for credentials in cls.credential_list:
            if credentials.account_name == name:
                return credentials

    @classmethod
    def credentials_exist(cls,name):
        """
        checking if the name exist

        """
        for credentials in cls.credential_list:
            if credentials.account_name == name:
                return True
        return False
    
    @classmethod
    def display_credentials(cls):
        """
        displaying all contacts 

        """
        return cls.credential_list