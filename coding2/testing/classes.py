class Animal: 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed  
andat = [["Pumpkin", "Orange Tabby"], ["Alpine", "Siamese"], ["Piccolo", "Tabby"], ["Luna", "Labrador Retreiver"]]
for i in andat: curr = Animal(i[0], i[1]); print(curr.name,"|", curr.breed)