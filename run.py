#!/usr/bin/env python3.6
import random
from credentials import Credantials
from user import User

#creating credetios
def create_user(first_name,last_name,password):
    """
    function to create new credentials
    """

    new_user = User(first_name,last_name,password)
    return new_user

def save_users(user):
    '''
    fuction that save users
    '''
    user.save_user()
def user_login_in(first_name,last_name,password):
    '''
    allows user to log in their credentials
    '''
    log_in = User.log_in(first_name,last_name,password)
    if log_in != False:
        return User.log_in(first_name,last_name,password)

def display_users():
    '''
    returns all saved user
    '''
    return User.display_user()

def check_existing_users(name):
    '''
    checks if user already exist
    '''
    return User.user_exist(name)


def create_credentials(user_password, account_name,account_password):
    '''
    function for creating new credentials
    '''
    new_credential = Credantials(user_password,account_name,account_password)

    return new_credential



#deletingcredentials
def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credantials.delete_credential(credentials)

#saving credentials
def save_credentials(credentials):
    """function of  saving"""
    credentials.save_credentals()

#finding if exist 
def existing_credential(credential_name):
    """
    checking is name exist 
    """

    return Credantials.credentials_exist(credential_name)

def search_credential(account):
    ''' funtion to find the credential in the list '''
    return Credantials.find_credential(account)



#displaying all contact 
def display_credentials(password):
    """
    trying to display all the credentials
    """

    return Credantials.display_credential(password)
def generated_password(name):
    '''
    Function that generates a password for the user

    Args:
        name : the name of the account
    '''
    password = Credantials.gen_pass()

    return password


def main():
   
        print("\n")
        print('''                 ~~~~~~([])=([])==([])~~~~~ welcome to password locker ~~~~~~~~([])=([])==([])~~~~~\n\n \n \n ''')

        print('''                 :::::::::::use the short codes::::::::: \n \n \n''')

         
        while True:
            '''
            Loop that is running the entire application
            '''
            print('''Use these short codes to navigate:\n\n
            (cu) - CREATE A PASSWORD LOCKER ACCOUNT \n
            (lg)- LOG INTO PASSWORD LOCKER ACCOUNT \n
            (du) - DISPLAY CURRENT PASSWORD LOCKER USERS \n
            (ex) - EXIT PASSWORD LOCKER''')

            # Get short codes from the user
            short_code = input().lower()

            if short_code == 'cu':
                '''
                Creating a Password Locker account
                '''

                print("\n")
                print("New Password Locker Account")
                print("-"*10)# prints a ten dotted-line

                print("First name ...")
                first_name = input()

                print("Last name ...")
                last_name = input()

                print("Password ...")
                password = input()
                #create and saves users
                save_users( create_user( first_name,last_name,password) )

                print(f"{first_name} welcome to Password Locker")
                print("\n")

            elif short_code == 'du':
                '''
                Display the names of the current users
                '''

                if display_users():
                    print("\n")
                    print("Here are the current users of Password Locker")
                    print("-"*10)

                    for user in display_users():
                        print(f"{user.first_name}")
                        print("-"*10)

                else:
                    print("\n")
                    print("Password Locker has no current user.\n    please be our first user :)")
                    print("\n")
            elif short_code == 'lg':
                '''
                Logs in the user into their Password Locker account
                '''
                print("\n")
                print("Log into Password Locker Account")
                print("Enter the first name")
                first_name = input()
                print("Enter the last name")
                last_name = input()
                print("Enter the password")
                password = input()
                if user_login_in(first_name,last_name,password) == None:
                    print("\n")
                    print("Please try again or create an account")
                    print("\n")
    
                else:
    
                    user_login_in(first_name,last_name,password)
                    print("\n")
                    print(f'''{first_name} welcome to your Credentials\n
                    ''')


                    while True:
                        '''
                        Loop to run functions 
                        '''
                        print(''' Use  Short codes to navigate:\n\n

                        (dc) - DISPLAY CREDENTIALS \n
                        (cc) - ADD CREDENTIAL \n
                        
                        (cg) - CREATE CREDENTIALS & AUTO-GENERATE PASSWORD \n
                        (dl) - DELETE CREDENTIALS \n
                        (ex) - EXIT CREDENTIALS''')

                        short_code = input().lower()

                        if short_code == 'cc':
                            '''
                            Creating a Credential
                            '''

                            print("\n")
                            print("New Credential")
                            print("-"*10)

                            print("Name of the credential ...")
                            credential_name = input()

                            print("Password of the credential ...")
                            credential_password = input()

                            save_credentials( create_credentials( password, credential_name, credential_password) )

                            print("\n")
                            print(f"Credentials for {credential_name} have been created and saved")
                            print("\n")


                        elif short_code == 'dc':
                            '''
                            Displaying credential name and password
                            '''

                            if display_credentials(password):
                                print("\n")
                                print(f"{first_name}\'s credentials")
                                print("-"*10)

                                for credential in display_credentials(password):
                                    print(f"Account ..... {credential.credential_name}")
                                    print(f"Password .... {credential.credential_password}")
                                    print("-"*10)

                        elif short_code == 'cg':
                            '''
                            Creating a credential with a generated password
                            '''

                            print("\n")
                            print("New Credential")
                            print("-"*10)

                            print("Name of the credential ...")
                            credential_name = input()

                            # Save new credential with its generated password
                            save_credentials( Credantials(password, credential_name, (generated_password(credential_name)) ) )
                            print("\n")
                            print(f" {credential_name} have been created and saved")
                            print("\n")

                        elif short_code == 'ex':
                            print(f"i cant wait to see you again {first_name}")
                            print("\n")
                            break
                        elif short_code == 'dl':
                            while True:
                                print(f"WARNING!!!!!! YOU WILL NOT BE ABLE TO RECOVER IT {first_name}, which credential would you like to remove?\n ")
                                credential_name = input()

                                if existing_credential(credential_name):

                                    search_cred = search_credential(credential_name)

                                    #print(f"ACOUNT: {search_cred.credential_name} \n ")
                                    print("Are You Sure You want to delete? y/n")
                                    confirm = input().lower()
                                    if confirm == 'y':
                                        pass
                                        #delete_credential(credential_name)
                                        print("deleted SUCCESFULLY")
                                        break
                                    elif confirm == 'n':
                                        continue

                                else:
                                    print(f" {first_name},You do not have {cred_to_delete} as your credentials" )
                                    break
                            print(f"{first_name} you are about to delete ")

                        else:
                            print("\n")
                            print(f'''{short_code} does 
                             the short codes''')
                            print("\n")
            elif short_code == 'ex':
               
                print("\n")
                print("[][][][][][][][][][][][]THANKS. PLEASE VISIT US AGAIN SOON [][][][][][][][][][][][] ")

                break

            else:
                print("\n")
                print(f'''Opps! {short_code} IS NOT RECOGNIZED AS A VALID COMMAND
            Please use the short codes''')
                print("\n")

if __name__ == '__main__':
    main()