# Ask the user for their password and remove extra spaces.
password = input("Enter your secret password: ").strip()

# Get the first and last letter of the password.
first_letter = password[0]
last_letter = password[-1]

# Show the password hint in uppercase.
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")
