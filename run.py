#!/usr/bin/env python3.6
from credentials import Credantials
from user import User

#creating credetios
def create_credentials():
    """
    function to create new credentials
    """

    new_credentials = credentials(account_name,account_password)
    return new_credentials
#deleting credentials
def delete_credentials():
    """
    function of deleting credentials 
    """
    credentials.delete_credentials()



#saving credentials
def save_credential(credentials):
    """function of  saving"""
    credentials.save_credentals()
#finding a contact 
def find_credantials(name):
    """
    finding credentials
    """
    return Credantials.find_by_name(name)
#finding if exist 
def check_existing(name):
    """
    checking is name exist 
    """

    return Credantials.credentials_exist(name)

#displaying all contact 
def display_credentials():
    """
    trying to display all the credentials
    """

    return Credantials.display_credentials()


def main():
    while True:
        print("\n")
        print('''                 ~~~~~~<<<~~~~~ welcome to password locker ~~~~~~~~>~~~~~\n\n \n \n ''')

        print('''                 ^^^^^use the short codes^^^^^  \n \n \n
         (cc) - create credentials\n
         (dc) - display credentials \n
         (ce) - check existing \n
         (sc) - save credential \n
         (dr) - delete credentials''')
         
        short_code = input().lower()

        if short_code == 'cc':
            print("create a user name...................\n ............")
            created_user_name= input()

            print("select a password")
            created_password= input()

            print ("confirm you password")
            comfirm_password = input()

if __name__ == '__main__':
    
    main()