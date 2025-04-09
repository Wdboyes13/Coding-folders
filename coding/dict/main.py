import json
word = input("Enter word: ")

json_file = open('dict.json')
passfile = json.load(json_file)

entry = passfile.get(word)
print(entry)