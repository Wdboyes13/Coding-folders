var dotw: some String {
    gaurd let dot = Date().dayNumberOfTheWeek() else {return 0.00}
    switch dot {
        case 1: "Sunday"
        case 2: "Monday"
        case 3: "Tuesday"
        case 4: "Wednesday"
        case 5: "Thursday"
        case 6: "Friday"
        case 7: "Saturday"
        default: "Error"
    }
}