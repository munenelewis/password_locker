#!/usr/bin/env python3.6
from credentials import Credantials
from user import User

#creating credetios
def create_credentials(account_name,account_password):
    """
    function to create new credentials
    """

    new_credentials = credentials(account_name,account_password)
    return new_credentials
#deleting credentials
def delete_credentials(credentials):
    """
    function of deleting credentials 
    """
    Credantials.credential_list.remove(crede)


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
         (lg) - loging \n
         (ex) - exit''')
         
        short_code = input().lower()

        if short_code == 'cc':
            print("create a user name...................\n ............")
            created_user_name= input()

            print("select a password")
            created_password= input()

            print ("confirm you password")
            comfirm_password = input()
            while created_password != comfirm_password:
                print('''              #@#@#@#  error you password dont match    #@#@#@#  \n''')
                print('''      please input your password again     \n''')
                created_password = input()
                print('''      comfirm  your password  ''')
                comfirm_password = input()
            else:
                print (f"welcome {created_user_name} to our service i hope you enjoy ")
                print("\n")
                print("you can proceed to your account")
                print("name")
                entered_username= input()
                print("password")
                entered_password = input()
            while entered_username != created_user_name or entered_password != created_password:
                print('''  /\/\/\/\/\/\  your pass word or username is incorect please check your credentials  /\/\/\/\/\/\/\  ''')
                print ( " enter your user name ")
                entered_username = input()
                print(" enter your password ")
                entered_password = input()
            else:
                print(f" welcome to your account ")
                print("\n")
                print("please choose what you would like to so in your account : ")
                print("\n")
                print('''                       (a) - delete account \n
                            (b) - view your details \n
                            (c) - Add new credentials    \n         
                            (d) - search credentials\n
                            (e) - log out      \n   ''')
                option = input()

                if option == 'a':
                    print('''  ------------ ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT ?--------''')
                    print ('''                                      (y) - yes i want to delete my account \n
                                            (n) - no i dont want ro delete my account \n ''')
                    choice = input().lower()
                    if choice == "n":
                        
                        continue
                elif confirm == 'c':
                    print ("create user name")
                    created_username = input()

                    print("select password")
                    selected_password = input()

                    print("confrim password")
                    comfirm_password = input()

                else:
                        continue     
        elif short_code == 'lg':
            print("welcome \n")
            print("enter user name ........................")
            default_user_name = input()

            print("Enter your password ....................")
            default_user_password = input()
            print("\n")
                  
if __name__ == '__main__':
    main()