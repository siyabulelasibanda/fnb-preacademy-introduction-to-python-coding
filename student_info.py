first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

full_name = f"{first_name} {surname}"

print(f"Welcome, {full_name}!")
print(f"Uppercase name: {full_name.upper()}")
print(f"Title case name: {full_name.title()}")
print(f"Age in months: {age * 12}")
print(f"Favourite number: {round(favourite_number, 2)}")

print(type(first_name))
print(type(surname))
print(type(age))
print(type(favourite_number))
