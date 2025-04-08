import datetime
import os
os.system("clear")
def tokenize(chars: str) -> list:
    return ''.join(chars)

def main():
    
    utch = int(datetime.datetime.now(datetime.timezone.utc).strftime("%H"))
    utcm = int(datetime.datetime.now(datetime.timezone.utc).strftime("%M"))
    print("To exit program enter EXIT in the next field")
    tz = input("Enter UTC+/-00:00 Code: UTC")
    if tz == "EXIT":
        quit()
    tz = tz.replace("+", "")
    tokens = tokenize(tz)
    if tokens[0] == "-":
        codehstr = tokens[1] + tokens[2]
        codeh = int(codehstr)
        timeh = utch - codeh
        codemstr = tokens[4] + tokens[5]
        codem = int(codemstr)
        timem = utcm - codem

    else: 
        codehstr = tokens[0] + tokens[1]
        codeh = int(codehstr)
        timeh = utch - codeh
        codemstr = tokens[3] + tokens[4]
        codem = int(codemstr)
        timem = utcm - codem


    if timeh < 0:
        timeh = timeh+24
    if timeh > 24:
        timeh = timeh-24
    print(timeh, ":", timem)

i = 0
while i == 0:
    main()

    