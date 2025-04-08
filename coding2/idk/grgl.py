import json
class bsns:
    def __init__(self, name):
        self.name = name

    def calc_id(self, out=False):
        id_value = ""
        for char in self.name.lower():
                id_value += str(ord(char))
        self.id = int(id_value)
        if out:
            print(self.id)
        return self.id

    def dmpjson(self):
        self.calc_id()
        json_file = open("names.json")
        confile = json.load(json_file)
        confile.update({self.name: {
            "id": self.id
        }})
        with open("names.json", "w") as file:
            json.dump(confile, file, indent=4)

class jsr:
    def __init__(self, file):
        self.file = file
        
    def read(self):
        with open(self.file, "r") as file:
            self.jsfile = json.load(file)
    
    def dmp(self):
        self.read()
        print(self.jsfile)

class jsw:
    def __init__(self, file):
        self.file = file
        self.name = input("Enter name: ")
        self.email = input("Enter email: ")
        def calc_id(self, out=False):
            id_value = ""
            for char in self.name.lower():
                id_value += str(ord(char))
            self.id = int(id_value)
            if out:
                print(self.id)
            return self.id
        calc_id()
    
    def add(self):
       json_file = open(self.file)
       data = json.load(json_file)
       data.update({self.name: {
           "id": self.id,
           "email": self.email
       }
       })
       with open(self.file, "w") as file:
           json.dump(data, file, indent=4)
           
