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
def save_credentials:
    """
    function for saving credentials
    """
    
    credentials.save_credentials()

#finding a contact 
def find_credantials:
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
