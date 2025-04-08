import json
import sys
import os
import datetime
def newcon():
    print("If you dont want to use a field just press enter")
    uname = input("Enter username: ")
    rname = input("Enter real name: ")
    pronouns = input("Enter pronouns: ")
    time_zone = input("Enter time zone using UTC +/- formatted as -1 or -8: ")


    json_file = open('names.json')
    passfile = json.load(json_file)
    
    passfile.update({uname: {
        "name": rname,
        "pronouns": pronouns,
        "time zone": time_zone
    }})


    with open("names.json", 'w') as file:
            json.dump(passfile, file, indent=6)
    python = sys.executable
    os.execl(python, python, * sys.argv)

def readcon():
      name = input("Enter the username: ")
      json_file = open('names.json')
      file = json.load(json_file)
      entry = file.get(name)
      entry_list = list(entry.values())
      cutimel = datetime.datetime.now(datetime.timezone.utc)
      cuh = int(cutimel.strftime("%H"))
      print("Name: ", entry_list[0])
      print("Pronouns: ", entry_list[1])
      print("Time zone: UTC", entry_list[2])
      print(cuh)
      python = sys.executable
      os.execl(python, python, * sys.argv)

option = input("Enter VIEW or ADD to select what you want to do: ")
if option == "VIEW":
      readcon()
if option == "ADD":
      newcon()