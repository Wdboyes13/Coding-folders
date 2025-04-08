correct = int(input("Enter correct amount: "))
total = int(input("Enter total amount: "))

percentile = 100/total
percentcorrect = percentile * correct
lgrade = ""
if percentcorrect in range(86, 100):
    lgrade = "A"
if percentcorrect in range(73, 85):
    lgrade = "B"
if percentcorrect in range(67, 72):
    lgrade = "C+"
if percentcorrect in range(60, 66):
    lgrade = "C"
if percentcorrect in range(50, 59):
    lgrade = "C-"
if percentcorrect in range(0, 49):
    lgrade = "F"

print("THESE RESULTS SHOULD NOT BE USED AS A SUBSTITUTION FOR TEACHER ASSESMENT")
print("You got", str(percentcorrect)+"%", "("+lgrade+")")

# letter grade table found at final page of https://www2.gov.bc.ca/assets/gov/education/administration/legislation-policy/legislation/schoollaw/e/m192_94.pdf