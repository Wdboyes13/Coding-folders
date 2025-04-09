i = 0
pitchhz = 440
print(pitchhz)
timesdn = 48
timesup = 39
i = 0
print("Going down from A4")
for i in range(timesdn):
    pitchhz /= 1.05946
    print(pitchhz)
    i+=1
i = 0
pitchhz = 440
print("Going up from A4")
for i in range(timesup):
    pitchhz *= 1.05946
    print(pitchhz)
    i+=1