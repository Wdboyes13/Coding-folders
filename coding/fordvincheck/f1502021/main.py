print("Ford VIN Checker for F-150 2021 by William Boyes \n")
vin = input("Enter your VIN: ")
info = []
if vin[0] == "1" & vin[1] == "F" & vin[2] == "T":
    print("Valid Ford VIN")
    print("Continuing process...")
    info.append("Manufacturer: Ford Motor Company, USA")
    info.append("Make: Ford")
    info.append("Type: Truck (Completed Vehicle)")
    if vin[3] == "M":
        print("4th Digit checked")
        info.append("Brake System: Hydraulic")
        info.append("GVWR Class: E")
        info.append("GVWR Range: 6001-7000")
        info.append(["Cat 5", "Manual Belts", "Driver Frontal", "Passenger Frontal", "1st Row Side Inflatable"])

    if vin[3] == "N":
        print("4th Digit checked")
        info.append("Brake System: Hydraulic")
        info.append("GVWR Class: F")
        info.append("GVWR Range: 7001-8000")
        info.append(["Cat 5", "Manual Belts", "Driver Frontal", "Passenger Frontal", "1st Row Side Inflatable"])
    
    if vin[3] == "E":
        print("4th Digit checked")
        info.append("Brake System: Hydraulic")
        info.append("GVWR Class: E")
        info.append("GVWR Range: 6001-7000")
        info.append(["Cat 5", "Manual Belts", "Driver Frontal", "Passenger Frontal", "1st Row Side Inflatable", "2nd Row Side Inflatable"])

    if vin[3] == "N":
        print("4th Digit checked")
        info.append("Brake System: Hydraulic")
        info.append("GVWR Class: F")
        info.append("GVWR Range: 7001-8000")
        info.append(["Cat 5", "Manual Belts", "Driver Frontal", "Passenger Frontal", "1st Row Side Inflatable", "2nd Row Side Inflatable"])
    
    if vin[4] == "F" & vin[5] == "1" & vin[6] == "C":
        print("Checked digits 5-7")

