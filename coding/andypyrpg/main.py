import random
from time import time, sleep
import os
from split import split

print("Frac game")
print("press enter when you want to start")
input()

os.system("clear")
print("3")
sleep(1)
print("2")
sleep(1)
print(1)
sleep(1)
print("Go!")
sleep(1)
os.system("clear")

points = 0
lives = 3


def gen():
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    num3 = random.randrange(1, 10)
    num4 = random.randrange(1, 10)
    operations = ["x", "/", "+", "-"]
    opr = operations[random.randrange(0, 3)]
    print(num1, " ", num3)
    print("-", opr, "-")
    print(num2, " ", num4)
    return [num1, num2, num3, num4, opr]


while lives > 0:
    os.system("clear")
    print("Points: " + str(points) + " Lives: " + str(lives))
    gened = gen()
    num1 = [gened[0] / gened[1], gened[0], gened[1]]
    num2 = [gened[2] / gened[3], gened[2], gened[3]]

    if gened[4] == "+":
        ans = num1[0] + num2[0]
    elif gened[4] == "-":
        ans = num1[0] - num2[0]
    elif gened[4] == "x":
        ans = num1[0] * num2[1]
    elif gened[4] == "/":
        ans = num1[0] / num2[0]
        if len(str(num1[1] / num2[1])) >= 2 or len(str(num1[2] / num2[2])) >= 2:
            continue
            pass

    inp = split(input(">> "), "/")
    if inp == "help me pls":
        continue

    try:
        if float(inp[0]) / float(inp[1]) == ans:
            print("Correct")
            print("+1 point")
            points += 1
            sleep(1.5)
        else:
            print("Incorrect")
            print("-1 life")
            lives -= 1
            sleep(1.5)
    except:
        print("invalid input, format is numerator/denominator")
        sleep(2)

os.system("clear")
print("...")
sleep(2)

if random.randrange(1, 100) == 1:
    print(f"\033[96m" + "IT WAS A SPECIAL DAY")
    sleep(2)
    print("YOU WANTED TO GET BACK FAST")
    sleep(2)
    print("BUT YOU WERE TOO TIRED")
    sleep(2)
    print("YOU WENT OFF THE ROAD")
    sleep(3)
    print("WHAT WERE YOU THINKING?" + "\033[0m")
else:
    print(f"GAME OVER    Score: {points}")
