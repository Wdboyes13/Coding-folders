import random
import os
import sys
os.system("clear")
def main():
    person1=input("Enter first person: ")
    person2=input("Enter second person: ")

    print(person1 + "+" + person2, "has a", str(random.randrange(1, 100)) + "% chance of working")
    usrin = input("Would you like to do another Y/N: ")
    if usrin == "N" or usrin == "n":
        sys.exit()
i = 0
while i == 0: 
    os.system("clear")
    main()