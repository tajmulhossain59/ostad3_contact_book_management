import json
import os
import datetime
from contact import Contact

DATA_FILE = "contacts.json"

def load_contacts():
    try:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return [Contact.from_dict(item) for item in data]
    except FileNotFoundError:
        print("Error: Data file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Data file is corrupted.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def save_contacts(contacts):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump([contact.to_dict() for contact in contacts], file)
    except Exception as e:
        print(f"Error saving contacts: {e}")

def backup_contacts():
    try:
        backup_file = f"backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(DATA_FILE, "r") as original, open(backup_file, "w") as backup:
            backup.write(original.read())
        return backup_file
    except FileNotFoundError:
        print("Error: Original file not found for backup.")
        return None
    except Exception as e:
        print(f"Unexpected error during backup: {e}")
        return None
