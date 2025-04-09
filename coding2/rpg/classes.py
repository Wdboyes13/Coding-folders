class player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
    
    def damage(self):
        self.hp -= 10

    def attack(self, enem):
        enem.damage()
    
    def play(self, enem):
        move = input("Enter move: ")
        match move:
            case "attack": self.attack(enem)

class enemy:
    def __init__(self):
        self.name = enemy
        self.hp = 100
    
    def damage(self):
        self.hp -= 10

    def attack(self, playe):
        playe.damage()
    
    def play(self, playe):
        self.attack(playe)