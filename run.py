#!/usr/bin/env python3.6
import random
from credentials import Credantials
from user import User

#creating credetios
def create_credentials(account_name,account_password):
    """
    function to create new credentials
    """

    new_credentials = Credantials(account_name,account_password)
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
                print (f"welcome {created_user_name} to our service i hope you enjoy")
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
                print('''                          (i)- search credentials\n
                                    (ii) - add new credentials \n
                                    (iii) - view saved credentials \n
                                    (iv)- remove credentials \n
                                     (v) - logout ''')
                option = input()
                if option == 'ii':
                    while True:
                        print("Do you still wanna add contacts ? yes or no?\n")

                        choice =input().lower()
                        if choice == 'yes':
                            print ("enter the account name \n")
                            account_name  = input()
                            print("enter account password \n")
                            print("to generate a random password password please type 'gen' to create your own password please type 'own'/n")
                            pass_choice = input().lower()

                            if pass_choice == 'gen':
                                account_password = random.randint(1111, 1111)
                                print(f" Account : {account_name} \n")
                                print(f" Password : {account_password} ")
                                print('\n')
                            elif pass_choice =='own':
                                print("create your own password \n")
                                account_password = input()
                                print (f" your account name is : {account_name} \n")
                                print(f"you password is : {account_password} \n")
                            else:
                                print("enter a valid choice")
                                save_credentals(create_credentials(account_name, account_password))
                        elif choice=='no':
                                    continue
                        else:
                            print("please use 'yes' or 'no' ")    
                elif option=="i":
                    while True:
                        print("do you wish to continue? 'y' or 'n'\n")
                        con = input().lower()
                        if con == "y":
                            print("enter credentials you want to find \n")

                            search_name = input()

                            if check_existing(search_name):
                                search_credential = find_credantials(search_name)
                                print(f"Account name : {search_credential.account_name} \n Password: {search_credential.account_password}")
                            else:
                                print("contact doesnt exist")
                        elif con=="n":
                            break
                        else:
                            print("please pick 'y' or 'no' ")
                elif option=="iv":
                    while True:
                        print ("search the credentials you want to delete")
                        search_name = input()
                        if check_existing(search_name):
                            search_credential = find_credantials(search_name)
                            print (f"ACCOUNT NAME : {seach_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            print("delete credentials? abort or cont ")
                            descion = input().lower()
                            if descion == "cont":
                                delete_credentials(search_credential)
                                print("account has been deleted")
                                break
                            elif descion == "abort":
                                continue
                            else:
                                print("That contact does not exist")
                                break
                elif option == "iii":
                    while True:
                        print("below are your saved credentials")
                        if display_credentials():
                            
                            for credentials in  credential_list():
                                print("ACCOUNT NAME :"+ {credentials.account_name}+" \n ACCOUNT PASSWORD"+ {credentials.account_password})
                        
                        else:
                            print("you havent saved any credentials yet \n")


                            print("back to menu? y or n")

                            back = input().lower()
                            if back == "y":
                                continue
                            elif back == "n":
                                break
                elif option=="v":
                    print("Warning if you log out all your credentials will be deleted. want to log out ? y or n")
                    logout= input().lower()
                    if logout == "n":
                        continue
                    elif logout =="y":
                        break
                    else:
                        print("invalid choise")
                        
                            
                else:
                    print("inavalide code")
        elif short_code == 'lg':
            print("welcome \n")
            print("enter user name ........................")
            default_user_name = input()

            print("Enter your password ....................")
            default_user_password = input()
            print("\n")
                  

            while default_user_password != '09876' or default_user_name != 'Testuser':
                print ("wrong password. User name 'Testuser' and password '09876' ")
                print("ENTER USER NAME \n")
                default_user_name = input()

                print("enter you password")
                default_user_password = input()
                print('\n')

            if default_user_name=="Testuser" and default_user_password=="09876":
                print("welcome to you account what would you like to do? /n")
                print("select the options below to continue :")
                print('''                          (i)- search credentials\n
                          (ii) - add new credentials \n
                          (iii) - view saved credentials \n
                          (iv)- remove credentials \n
                          (v) - logout ''')
                option = input()

                if option == 'ii':
                    while True:
                        print("Do you still wanna add contacts ? yes or no?\n")

                        choice =input().lower()
                        if choice == 'yes':
                            print ("enter the account name \n")
                            account_name  = input()
                            print("enter account password \n")
                            print("to generate a random password password please type 'gen' to create your own password please type 'own'/n")
                            pass_choice = input().lower()

                            if pass_choice == 'gen':
                                account_password = random.randint(1111, 1111)
                                print(f" Account : {account_name} \n")
                                print(f" Password : {account_password} ")
                                print('\n')
                            elif pass_choice =='own':
                                print("create your own password \n")
                                account_password = input()
                                print (f" your account name is : {account_name} \n")
                                print(f"you password is : {account_password} \n")
                            else:
                                print("enter a valid choice")

                            save_credential(create_credentials(account_name, account_password))
                        elif choice=='no':
                            break
                        else:
                            print("please use 'yes' or 'no' ")
                elif option=="i":
                    while True:
                        print("do you wish to continue? 'y' or 'n'\n")
                        con = input().lower()
                        if con == "y":
                            print("enter credentials you want to find \n")

                            search_name = input()

                            if check_existing(search_name):
                                search_credential = find_credantials(search_name)
                                print(f"Account name : {search_credential.account_name} \n Password: {search_credential.account_password}")
                            else:
                                print("contact doesnt exist")
                        elif con=="n":
                            break
                        else:
                            print("please pick 'y' or 'no' ")
                elif option=="iv":
                    while True:
                        print ("search the credentials you want to delete")
                        search_name = input()

                        if check_existing(search_name):
                            search_credential = find_credantials(search_name)
                            print (f"ACCOUNT NAME : {seach_credential.account_name} \n PASSWORD: {search_credential.account_password}")
                            print("delete credentials? abort or cont ")
                            descion = input().lower()
                            if descion == "cont":
                                delete_credentials(search_credential)
                                print("account has been deleted")
                                break
                            elif descion == "abort":
                                continue
                        else:
                            print("That contact does not exist")
                            break
                elif option == "iii":
                    while True:
                        print("below are your saved credentials")
                        if display_credentials():
                            
                            for credentials in  credential_list():
                                print("ACCOUNT NAME : {credentials.account_name} \n ACCOUNT PASSWORD {credentials.account_password")
                        
                        else:
                            print("you havent saved any credentials yet \n")


                        print("back to menu? y or n")

                        back = input().lower()
                        if back == "y":
                            continue
                        elif back == "n":
                            break
                        else:
                            print("inavalide code")
                elif option=="v":
                    print("Warning if you log out all your credentials will be deleted. want to log out ? y or n")
                    logout= input().lower()
                    if logout == "n":
                        continue
                    elif logout =="y":
                        break
                    else:
                        print("invalid choise")
                                                                           
        elif short_code == "ex":
            break
        else:
            print("invalid code")
                                       
if __name__ == '__main__':
    main()