from locs import locations
dn = int(input("DSK > "))
if dn in locations:
    cmd = input("CMD > ")
    if cmd == "ls":
        for track, name in locations[dn].items():
                print(f"Disk {dn} Track {track}: {name} \n")

    if cmd == "trt":
        tr = input("Enter track number > ")
        print(f"Disk 1 Track {tr}: {locations[dn][int(tr)]}")