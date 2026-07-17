# Store friend names and phone numbers in a dictionary.
contacts = {
    "Lebo": "0821112222",
    "Thabo": "0833334444",
    "Aisha": "0845556666"
}

# Ask the user which friend they want to find.
name = input("Enter a friend's name: ")

# Check if the name is in the dictionary.
if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")
