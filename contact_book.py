# Store all contacts in a list.
contacts = []


# Add a new contact to the list.
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"{name} was added successfully.")


# Find a contact by name.
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


# Delete a contact by name.
def delete_contact(name):
    contact = search_contact(name)
    if contact is not None:
        contacts.remove(contact)
        print(f"{contact['name']} was deleted.")
    else:
        print("Contact not found.")


# Display every contact.
def view_all():
    if len(contacts) == 0:
        print("No contacts saved.")
    else:
        print("\n--- CONTACTS ---")
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("----------------")


# Keep showing the menu until the user chooses Exit.
while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        name = input("Enter name to search: ")
        contact = search_contact(name)
        if contact is not None:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "4":
        view_all()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 5.")
