import classes

playe = classes.player(input("Enter your name: "))
enem = classes.enemy()
while 1 == 1:
    playe.play(enem)
    enem.play(playe)
    print(playe.hp)
    print(enem.hp)