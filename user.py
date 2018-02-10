from credentials import Credantials

class User:
    """
    class that generates instances of user
    """
    user_list = []#Empty contact list

    def __init__(self,first_name, last_name,password):
  
        """
        helps in defining properties of a method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
   

    def save_user(self):
        """
        save_user saves contact object into contact_list"""

        User.user_list.append(self)

    @classmethod
    def log_in(cls, first_name,last_name,password):

        '''
        checking if credential exist

        '''

        for user in cls.user_list:
            if user.first_name  and user.last_name and user.password:
                return Credantials.credential_list

        return False

    @classmethod
    def user_exist(cls, name):
        '''
        if user exist

        '''

        for user in cls.user_list:
            if user.first_name == name:
                return True

        return False

    @classmethod
    def display_user(cls):

        return cls.user_list

    @classmethod
    def find_credential(cls, name):

        for credential in Credantials.credential_list:
            if credential.account_name == account_name:
                return True
        return False
