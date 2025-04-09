
person1=input("Enter first peron: ")
person2=input("Enter second person: ")
i = 0
matches = []
while i < len(person1):
    if person1[i] in person2:
        matches.append(i)
    i+=1
i1 = 0
while i1 < matches[0]:
    print(person1[i1])
    i1+=1
    
if matches:
    # Get the index of the first match in person2
    first_match_index = person2.find(person1[matches[0]])  # find the first matched character from person2
    print(person2[first_match_index])  # Print the first match
    
    # Print all subsequent characters in person2 starting from the next character after the match
    i3 = first_match_index + 1  # Start from the next character after the first match
    while i3 < len(person2):
        print(person2[i3])
        i3 += 1
else:
    print("No matches found.")