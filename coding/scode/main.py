import sys

if len(sys.argv) < 2:
    print("Please provide the filename as an argument.")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as file:
    filename = file.read()

def tokenize(chars: str) -> list:
    return chars.split()

tokens = tokenize(filename)

i = 0
var = {}
commands = {"say", "if", "is"}

def add(i, vars):
        if tokens[i+1] in vars:
            if tokens[i+3] in vars:
                a = float(vars[tokens[i+1]]) + float(vars[tokens[i+3]])
                
            else:
                a = float(vars[tokens[i+1]]) + float(tokens[i+3])
                

        elif tokens[i+3] in vars:
              a = float(tokens[i+1]) + float(vars[tokens[i+3]])
              
        else:
            a = float(tokens[i+1]) + float(tokens[i+3])
           
        return a

def multiply(i, vars):
        if tokens[i+1] in var:
            if tokens[i+3] in var:
                a= float(var[tokens[i+1]]) * float(var[tokens[i+3]])
                
            else:
                a=float(var[tokens[i+1]]) * float(tokens[i+3])
                

        elif tokens[i+3] in vars:
            a=float(tokens[i+1]) * float(var[tokens[i+3]])
            
        else:
            a=float(tokens[i+1]) * float(tokens[i+3])
            
        return a

def subtract(i, var):
        if tokens[i+1] in var:
            if tokens[i+3] in var:
                a = float(var[tokens[i+1]]) - float(var[tokens[i+3]])
                
            else:
                a = float(var[tokens[i+1]]) - float(tokens[i+3])
                

        elif tokens[i+3] in vars:
              a = float(tokens[i+1]) - float(var[tokens[i+3]])
              
        else:
            a = float(tokens[i+1]) - float(tokens[i+3])
           
        return a

def divide(i, var):
        if tokens[i+1] in var:
            if tokens[i+3] in var:
                a= float(var[tokens[i+1]]) / float(var[tokens[i+3]])
                
            else:
                a=float(var[tokens[i+1]]) / float(tokens[i+3])
                

        elif tokens[i+3] in vars:
            a=float(tokens[i+1]) / float(var[tokens[i+3]])
            
        else:
            a=float(tokens[i+1]) / float(tokens[i+3])
        
        return a

while i < len(tokens):

   
    if tokens[i] == "is":
        varname = tokens[i - 1]
        if tokens[i + 1] == "user" and tokens[i + 2] == "input":
            var[varname] = input()
            i += 3
        elif tokens[i + 1] == "add":
            i+=1
            var[varname] = add(i + 1, var)
            i+=3

        elif tokens[i + 1] == "multiply":
            i+=1
            var[varname] = multiply(i + 1, var)
            i+=3

        elif tokens[i + 1] == "divide":
            i+=1
            var[varname] = multiply(i + 1, var)
            i+=3

        elif tokens[i + 1] == "subtract":
            i+=1
            var[varname] = multiply(i + 1, var)
            i+=3

        else:
            var[varname] = tokens[i + 1]
            i += 2


    if tokens[i] == "say":
        if tokens[i + 1] in var:
            print(var[tokens[i + 1]])
            i+=2
        elif tokens[i+1] == "add":
            i+=1
            print(add(i+1, var))
            i+=3
        elif tokens[i+1] == "multiply":
            i+=1
            print(add(i+1, var))
            i+=3
        elif tokens[i+1] == "divide":
            i+=1
            print(divide(i+1, var))
            i+=3
        elif tokens[i+1] == "subtract":
            i+=1
            print(subtract(i+1, var))
            i+=3
        elif tokens[i + 1].startswith('"'):
            message = []
            i += 1
            while i < len(tokens) and not tokens[i].endswith('"'):
                message.append(tokens[i].strip('"'))
                i += 1
            message.append(tokens[i].strip('"'))
            print(" ".join(message))
            i += 1


    if tokens[i] == "if":
        condition_met = False
        if tokens[i+2] == "=":
            if tokens[i+1] == tokens[i+3]:
                i+=5
        if tokens[i+2] == "<":
            if tokens[i+1] < tokens[i+3]:
                i+=5
        if tokens[i+2] == ">":
            if tokens[i+1] > tokens[i+3]:      
                i+=5