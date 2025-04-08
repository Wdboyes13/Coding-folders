import random
name = input("Enter name: ")
want = input("Enter what they want: ")
print("The chance of", name, "getting", want, "is", str(random.randrange(1, 100)) + "%")