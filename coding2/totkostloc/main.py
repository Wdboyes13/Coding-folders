from locs import locations
from fuzzywuzzy import process
import func
dn = int(input("DSK > "))

if dn in locations:
    cmd = input("CMD > ")
    if cmd == "ls":
        for track, name in locations[dn].items():
                print(f"Disk {dn} Track {track}: {name} \n")

    if cmd == "trt":
        tr = input("Enter track number > ")
        print(f"Disk {dn} Track {tr}: {locations[dn][int(tr)]}")

    if cmd == "search":
         searcher = func.search(locations)
         term = input("Enter search term: ")
         result = searcher.fuzzysearch
         print(result)
