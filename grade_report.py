# Store five students and their marks.
students = [
    {"name": "Lebo", "maths": 85, "english": 78, "science": 82},
    {"name": "Thabo", "maths": 65, "english": 70, "science": 68},
    {"name": "Aisha", "maths": 92, "english": 88, "science": 90},
    {"name": "Sipho", "maths": 48, "english": 55, "science": 42},
    {"name": "Nomsa", "maths": 35, "english": 45, "science": 40}
]

results = []
all_marks = []

# Calculate the average, grade and status for every student.
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3

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

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    result = {
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status
    }
    results.append(result)

    # Add each subject mark to the class marks list.
    all_marks.append(student["maths"])
    all_marks.append(student["english"])
    all_marks.append(student["science"])

# Calculate class statistics.
class_average = sum(result["average"] for result in results) / len(results)
highest_mark = max(all_marks)
lowest_mark = min(all_marks)

# Display the class report.
print("\n--- CLASS GRADE REPORT ---")
print("Name       | Average | Grade | Status")
print("-------------------------------------")
for result in results:
    print(f"{result['name']:<10} | {result['average']:<7} | {result['grade']:<5} | {result['status']}")

print("\n--- CLASS STATISTICS ---")
print(f"Class average: {round(class_average, 2)}")
print(f"Highest mark: {highest_mark}")
print(f"Lowest mark: {lowest_mark}")

# Allow the user to search for students.
while True:
    search_name = input("\nEnter a student name to search (or type stop): ").strip()

    if search_name.lower() == "stop":
        print("Search ended.")
        break

    found = False
    for result in results:
        if result["name"].lower() == search_name.lower():
            print(f"{result['name']}: Average {result['average']}, Grade {result['grade']}, {result['status']}")
            found = True

    if found == False:
        print("Student not found.")