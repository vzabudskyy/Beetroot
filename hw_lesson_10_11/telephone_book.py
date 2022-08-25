"""
Task 2

Extend Phonebook application

Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program


The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application,
else raise an error. After the user exits, all data should be saved to loaded JSON.
"""
import json
from pprint import pprint


HELP = """
        Dear User,
        
        Use this commands to interact with program:
        
            (0) - search contact. You are able to search by every attribute
            of contact.
            (1) - create new contact.
            (2) - update contact by phone number.
            (3) - delete contact by phone number.
            (h) - help.
            (x) - exit.
            
        Have a nice user experience!
"""


def create_phonebook(name):
    with open(f"phonebooks\\{name}.json", "w") as file:
        json.dump({"people": []}, file)


def get_new_contact_info():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = f"{first_name} {last_name}"
    phone_number = input("Enter phone number: ")
    state = input("Enter state: ")
    city = input("Enter city: ")
    contact = {"first_name": first_name,
               "last_name": last_name,
               "full_name": full_name,
               "phone_number": phone_number,
               "state": state,
               "city": city}

    return contact


def create_new_contact(phonebook_name, contact):
    with open(f"phonebooks/{phonebook_name}.json", "r+") as file:
        phonebook = json.load(file)
        file.seek(0)
        file.truncate(0)
        if contact not in phonebook["people"]:
            phonebook["people"].append(contact)
            json.dump(phonebook, file)
        else:
            return 0


def search(key, phonebook_name):
    with open(f"phonebooks/{phonebook_name}.json", "r") as file:
        file_read = file.read()
        phonebook = json.loads(file_read)
        for i in phonebook["people"]:
            if key in i.values():
                return i
            else:
                pass


def delete_record(phone_number, phonebook_name):
    with open(f"phonebooks/{phonebook_name}.json", "r+") as file:
        file_read = file.read()
        phonebook = json.loads(file_read)
        file.seek(0)
        file.truncate(0)
        for i in phonebook["people"]:
            if phone_number in i.values():
                phonebook["people"].remove(i)
                json.dump(phonebook, file)


def update_record(phone_number, updated_contact, user_phonebook):
    with open(f"phonebooks/{user_phonebook}.json", "r+") as file:
        file_read = file.read()
        phonebook = json.loads(file_read)
        file.seek(0)
        file.truncate(0)
        for i in range(len(phonebook["people"])):
            if phone_number in phonebook["people"][i].values():
                updated_contact["phone_number"] = phonebook["people"][i]["phone_number"]
                phonebook["people"][i] = updated_contact
                json.dump(phonebook, file)
                return


def main():
    print(HELP)
    user_phonebook = input("Enter phonebook name:")
    while True:
        user_input = input("Enter command: ")
        if user_input == "0":
            search_key = input("Enter key: ")
            result = search(search_key, user_phonebook)
            pprint(result)
        elif user_input == "1":
            new_contact = get_new_contact_info()
            create_new_contact(user_phonebook, new_contact)
        elif user_input == "2":
            contact_number = input("Enter phone number: ")
            updated_contact_info = get_new_contact_info()
            update_record(contact_number, updated_contact_info, user_phonebook)
        elif user_input == "3":
            contact_number = input("Enter phone number: ")
            delete_record(contact_number, user_phonebook)
        elif user_input == "h":
            print(HELP)
        elif user_input == "x":
            print("End of session")
            return
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
