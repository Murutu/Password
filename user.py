#!/usr/bin/env python3.6
from credential import User
from credential import Credential
import random

def create_user(fname,lname,email,password):
    '''
    class to create a new user
    '''
    new_user = User(fname,lname,email,password)
    return new_user

def create_credential(username,email,password):
    '''
    class to create new credential
    '''
    new_credential = Credential(username,email,password)
    return new_credential

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()

def save_credential(credential):
    '''
    function to save credentials
    '''
    credential.save_credential()

def delete_credential():
    '''
    function to delete credential
    '''
    Credential.delete_credential()

def find_credential(email):
    '''
    function that finds credential by email and returns the credential
    '''
    return Credential.find_by_email(email)

def check_existing_credential(email):
    '''
    function that checks if a credential exists with that email and return a boolean
    '''
    return Credential.credential_exist(email)

def display_user():
    '''
    function that returns all saved users
    '''
    return User

def display_credential():
    '''
    function that returns all saved credentials
    '''
    return Credential

def main():
    print("Welcome to password locker,please choose the path you would like,thankyou")

    #while True:
    print("Use the paths provided: \n ga - create a new user account with user defined password, \n fa - create a new user account with auto-generated password, \n ag - display user accounts, \n x - exit from the credentials list")

    short_code = input().lower()

    if short_code == "ga":
               print("New user")
               print("-"*10)
               print("Enter the site interested in")
               site = input()
               print(f"{site}has been created")

               print("First name....")
               f_name = input()

               print("Last name....")
               l_name = input()

               print("Email....")
               email = input()

               print("Username....")
               username = input()

               print("Enter Password....")
               password = input()

               save_user(create_user(f_name,l_name,email,password))
               save_credential(create_credential(username,email,password))
               print("/n")
               print(f"A new {site} account by {f_name} {l_name} has successfully been created")
               print("\n")

    elif short_code == "fa":
                print("New user")
                print("-" * 10)
                print("What site are you interested in?")
                site = input()
                print(f"{site}created")

                print("First name....")
                f_name = input()

                print("Last name....")
                l_name = input()

                print("Email....")
                email = input()

                print("Enter Username.... Hint: a secure password will be generated for you")
                username = input()
                s =  "zqa@deac5894mk=486GGF;;b bhjsm-bds(nbsb)savj78sbah@515GfW()"
                # passlen = 10
                password = "".join(random.sample(s,10))
                save_user(create_user(f_name,l_name,email,password))
                print("/n")
                print(f" A new {site} account by {f_name} {l_name} has been successfully created")
                print(f"The username is {username} and the password is {password}")
                print("\n")


    elif short_code == "ag":
            
            if display_user():
                print("Here is a list of all your user accounts")
                print("\n")
                
                for user in display_user():
                    print(f"{user.first_name} {user.last_name} has an account for {site}")
                print("\n")
            else:
                print("\n")
                print("You dont seem to have any existing acounts")
                print("\n")
                
    elif short_code == "x":
                print("Thankyou for viewing your account")
                
    else:
                 print("I did not really get that")

if __name__ == "__main__":
    main()






