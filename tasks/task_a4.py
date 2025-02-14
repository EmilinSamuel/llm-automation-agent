import json

def task_a4():
    with open("data/contacts.json", "r") as file:
        contacts = json.load(file)
    
    # Sort by last_name, then first_name
    sorted_contacts = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))
    
    # Write the sorted list to a new file
    with open("data/contacts-sorted.json", "w") as file:
        json.dump(sorted_contacts, file, indent=4)