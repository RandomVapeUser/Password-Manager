import time
import sys
import os


print("""
      
        Welcome to Sal's password manager smh
        
        """)

#Users and Passwords
###############################
List1 = open("Default1", "a")
List2 = open("Default1", "r")
List3 = List2.read()
Last1 = open("Default2", "a")
Last2 = open("Default2", "r")
Last3 = Last2.read()
Lost1 = open("Default3", "a")
Lost2 = open("Default3", "r")
Lost3 = Lost2.read()
###############################

#Tries
##########
X = 3
##########

#Create files
##########################
open("Saved.txt", "w")
open("Username.txt", "w")
open("Default1.txt", "w")
open("Default2.txt", "w")
open("Default3.txt", "w")    
###########################

#Password and Username File handling
#######################################
Z = open("Saved.txt", "a")
Y = open("Saved.txt", "r")
Y2 = Y.read()
Z1 = open("Username.txt", "a")
Y1 = open("Username.txt", "r")
Y3 = Y1.read()
########################################

with open('Saved.txt', 'r') as file:
    content = file.read().strip()


def no_tried():

    global X

    if X == 0:
        os.system("cls")
        print("No more tries left!")
        print("Goodbye!")
        time.sleep(3)
        sys.exit()
        
def check_pass():
    
    global X

    while X > 0:

        if os.path.getsize("Saved.txt") == 0:
            print("It seems its your first time using the password manager!")
            print("Input a new username and password to begin.")
            user_input = input("\nUsername: ")
            Z1.write(user_input)
            Z1.close()
            X = input("\nPassword: ")
            Z.write(X)
            Z.close()
            break

        else:

            Y = input("\nPassword: ")
            if Y == content:
                print(f"Welcome Back {Y3}!")
                break
            else:
                X -= 1
                no_tried()
                print(f"Wrong Password! Try again you have {X} tries left!")
                time.sleep(3)
                os.system("cls")
                continue

check_pass()

def start():
    
    print(f"""

        Welcome back {Y3}!
      
        [1] - Store Password
        [2] - Password List

        Disclaimer: Since im kinda dumb you can only store 3 passwords and usernames lmao
    
            """)
    
os.system("cls")
start()


def show_password():
    os.system("cls")

    print("Your usernames and passwords: ")
    with open("Default1.txt", "r") as file:
        print("Default1:")
        print(file.read())

    with open("Default2.txt", "r") as file:
        print("Default2:")
        print(file.read())

    with open("Default3.txt", "r") as file:
        print("Default3:")
        print(file.read())
        
def go_back():

    os.system("cls")

    print("""
          
          [1] - Go Back
          [2] - Exit
          
          """)
    
    X = int(input("\nChoose: "))

    if X == 1:
        start()

        choice = int(input(" "))
        choice_assist()
    elif X == 2:
        show_password()
    else:
        print("Goodbye!")
        time.sleep(3)
        sys.exit()



def store_password():
        
        if os.path.getsize("Default1") == 0:
            
            os.system("cls")
            imp = input("Username 1: ") + "\n"
            List1.write(imp)
            print("Saving...")
            time.sleep(2)
            print("Saved!")
            os.system("cls")
            imp2 = input("Password 1: ") + "\n"
            List1.write(imp2)
            List1.close()
            print("Saving...")
            time.sleep(2)
            print("Saved!")
            os.system("cls")
            go_back()
        
        elif os.path.getsize("Default2") == 0:

            os.system("cls")
            imp = input("Username 2: ") + "\n"
            Last1.write(imp)
            print("Saving...")
            time.sleep(2)
            print("Saved!")
            os.system("cls")
            imp2 = input("Password 2: ") + "\n"
            Last1.write(imp2)
            Last1.close()
            print("Saving...")
            time.sleep(2)
            print("Saved!")
            os.system("cls")
            go_back()

choice = int(input(" "))

def choice_assist():

    if choice == 1:
        store_password()
    elif choice == 2:
        show_password()

choice_assist()