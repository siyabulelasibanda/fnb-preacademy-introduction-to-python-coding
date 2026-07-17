# Ask for the learner's name and three subject marks.
name = input("Enter learner name: ")
english = float(input("Enter English mark: "))
maths = float(input("Enter Maths mark: "))
science = float(input("Enter Science mark: "))

# Calculate the average mark.
average = (english + maths + science) / 3

# Assign a letter grade.
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign pass or fail status.
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Check if any subject needs intervention.
interventions = []
if english < 40:
    interventions.append("English needs intervention")
if maths < 40:
    interventions.append("Maths needs intervention")
if science < 40:
    interventions.append("Science needs intervention")

if interventions:
    intervention = ", ".join(interventions)
else:
    intervention = "None"

# Display the report card.
print("\n--- REPORT CARD ---")
print(f"Learner: {name}")
print(f"English: {english}")
print(f"Maths: {maths}")
print(f"Science: {science}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")
print(f"Status: {status}")
print(f"Intervention: {intervention}")
