first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio: ")

username = f"{first_name[0]}{last_name}".lower()
full_name = f"{first_name} {last_name}".title()
clean_bio = bio.strip()
short_bio = clean_bio.replace("I am", "I'm")

print(f"Username: {username}")
print(f"Full name: {full_name}")
print(f"Bio: {clean_bio}")
print(f"Bio characters: {len(clean_bio)}")
print(f"Updated bio: {short_bio}")
