from contact_function import load_contacts, save_contacts, backup_contacts
from contact import Contact

def contact_exists(contacts, name, phone):
    """
    Check if a contact with the same name and phone already exists.
    """
    return any(contact.name == name and contact.phone == phone for contact in contacts)

def create_contact(contacts):
    try:
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()

         
        if contact_exists(contacts, name, phone):
            print("Error: A contact with the same name and phone already exists.")
            return

         
        contacts.append(Contact(name, phone, email))
        save_contacts(contacts)
        print("Contact created successfully!")
    except Exception as e:
        print(f"Error creating contact: {e}")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    try:
        print("\n--- All Contacts ---")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact.name} | {contact.phone} | {contact.email}")
    except Exception as e:
        print(f"Error displaying contacts: {e}")

def search_contact(contacts):
    try:
        query = input("Enter name or phone to search: ").strip().lower()
        results = [contact for contact in contacts if query in contact.name.lower() or query in contact.phone]
        if results:
            print("\n--- Search Results ---")
            for contact in results:
                print(f"{contact.name} | {contact.phone} | {contact.email}")
        else:
            print("No contacts found matching the query.")
    except Exception as e:
        print(f"Error searching contact: {e}")

def update_contact(contacts):
    try:
        phone = input("Enter phone of the contact to update: ").strip()
        for contact in contacts:
            if contact.phone == phone:
                contact.name = input(f"Enter new name (current: {contact.name}): ").strip() or contact.name
                contact.email = input(f"Enter new email (current: {contact.email}): ").strip() or contact.email
                save_contacts(contacts)
                print("Contact updated successfully!")
                return
        print("Contact not found.")
    except Exception as e:
        print(f"Error updating contact: {e}")

def remove_contact(contacts):
    try:
        phone = input("Enter phone of the contact to remove: ").strip()
        for contact in contacts:
            if contact.phone == phone:
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact removed successfully!")
                return
        print("Contact not found.")
    except Exception as e:
        print(f"Error removing contact: {e}")

def main():
    contacts = load_contacts()
    while True:
        try:
            print("\n--- Contact Book Management System ---")
            print("1. Create Contact")
            print("2. View All Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Remove Contact")
            print("6. Backup Contacts")
            print("7. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                create_contact(contacts)
            elif choice == "2":
                view_contacts(contacts)
            elif choice == "3":
                search_contact(contacts)
            elif choice == "4":
                update_contact(contacts)
            elif choice == "5":
                remove_contact(contacts)
            elif choice == "6":
                backup_file = backup_contacts()
                if backup_file:
                    print(f"Backup created: {backup_file}")
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
