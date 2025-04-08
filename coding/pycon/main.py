import json
import sys
import os
def newcon():
    print("You MUST use a unique display name for multiples of a first name")
    print("If you dont want to use a field just press enter")

    dispname = input("Enter a display name: ")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    emails = []
    emails.append(input("Enter a school/work email: "))
    emails.append(input("Enter a personal email address: "))
    phnums = []
    phnums.append(input("Enter a school/work phone number"))
    phnums.append(input("Enter a personal phone number"))


    json_file = open('contacts.json')
    passfile = json.load(json_file)
    if dispname == "":
        passfile.update({fname: {
            "name": fname + " " + lname,
            "email": emails,
            "phune number": phnums
        }})
    else:
          passfile.update({dispname: {
            "name": fname + " " + lname,
            "email": emails,
            "phone number": phnums
        }})

    with open("contacts.json", 'w') as file:
            json.dump(passfile, file, indent=6)
    restart_program()

def readcon():
      name = input("Enter the first name or display name as you entered it: ")
      json_file = open('contacts.json')
      file = json.load(json_file)
      entry = file.get(name)
      entry_list = list(entry.values())
      print("Name: ", entry_list[0])
      print("School/Work email: ", entry_list[1][0])
      print("Personal email: ", entry_list[1][1])
      print("School/Work phone number: ", entry_list[2][0])
      print("Personal phone number: ", entry_list[2][1])
      restart_program()

option = input("Enter VIEW or ADD to select what you want to do: ")
if option == "VIEW":
      readcon()
if option == "ADD":
      newcon()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)