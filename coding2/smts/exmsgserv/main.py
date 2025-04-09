import smts
import users
import random
acc = input("Do you have an account? (y/n) ")
if acc == "n":
    uname = input("Enter a username: ")
    uid = random.randint(1000000000000000, 9999999999999999)
    users.insert_user(uname, uid)
if acc == "y":
    uname = input("Enter your username: ")
    user = users.find_user(uname)
    if user == None:
        print("Error: User not found.")
        exit()
    uid = user[2]