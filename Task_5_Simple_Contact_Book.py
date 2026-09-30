import re
import sys

# Global in-memory contacts list
contacts = []

def isValidEmail(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def isValidPhone(phone: str) -> bool:
    pattern = r'^\+?[0-9\s\-]{7,15}$'
    return bool(re.match(pattern, phone))

def addContact():
    print("\n--- ADD NEW CONTACT ---")
    name = input("Enter Name: ").strip()
    if not name:
        print("⚠️ Error: Contact name cannot be empty.")
        return

    phone = input("Enter Phone Number: ").strip()
    if not isValidPhone(phone):
        print("⚠️ Error: Invalid phone number format.")
        return

    email = input("Enter Email Address: ").strip()
    if not isValidEmail(email):
        print("⚠️ Error: Invalid email address format.")
        return

    contact = {
        "id": len(contacts) + 1 if not contacts else max(c["id"] for c in contacts) + 1,
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"✅ Contact '{name}' added successfully!")

def viewContacts():
    print("\n--- ALL CONTACTS ---")
    if not contacts:
        print("No contacts found.")
        return

    print(f"{'ID':<5} | {'Name':<20} | {'Phone':<15} | {'Email':<25}")
    print("-" * 70)
    for c in contacts:
        print(f"{c['id']:<5} | {c['name']:<20} | {c['phone']:<15} | {c['email']:<25}")

def searchContact():
    print("\n--- SEARCH CONTACT ---")
    if not contacts:
        print("Contact list is empty.")
        return

    query = input("Enter name to search: ").strip().lower()
    if not query:
        print("⚠️ Search query cannot be empty.")
        return

    matches = [c for c in contacts if query in c["name"].lower()]

    if not matches:
        print(f"No contacts matching '{query}' were found.")
        return

    print(f"\nFound {len(matches)} matching contact(s):")
    print(f"{'ID':<5} | {'Name':<20} | {'Phone':<15} | {'Email':<25}")
    print("-" * 70)
    for c in matches:
        print(f"{c['id']:<5} | {c['name']:<20} | {c['phone']:<15} | {c['email']:<25}")

def deleteContact():
    global contacts  # Placed at the very top of the function to prevent SyntaxError
    print("\n--- DELETE CONTACT ---")
    if not contacts:
        print("Contact list is empty.")
        return

    viewContacts()
    try:
        contact_id = int(input("\nEnter the ID of the contact to delete: ").strip())
    except ValueError:
        print("⚠️ Error: Please enter a valid numerical ID.")
        return

    initial_length = len(contacts)
    contacts = [c for c in contacts if c["id"] != contact_id]

    if len(contacts) < initial_length:
        print(f"✅ Contact ID {contact_id} deleted successfully.")
    else:
        print(f"⚠️ Contact with ID {contact_id} not found.")

def main():
    while True:
        print("\n" + "=" * 45)
        print("           SIMPLE CONTACT BOOK           ")
        print("=" * 45)
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete Contact")
        print("5. Exit")
        print("=" * 45)

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            addContact()
        elif choice == "2":
            viewContacts()
        elif choice == "3":
            searchContact()
        elif choice == "4":
            deleteContact()
        elif choice == "5":
            print("\nExiting Contact Book application. Goodbye!")
            sys.exit(0)
        else:
            print("⚠️ Invalid choice! Please select an option between 1 and 5.")

if __name__ == "__main__":
    main()