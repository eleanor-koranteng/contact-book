import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
contacts = load_contacts()

def add_contact():
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email: ')

    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }

    contacts.append(contact)
    save_contacts()
    print('Contact added!')

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def view_contacts():
    if not contacts:
        print('No contacts saved.')
        return

    print('\nContacts:')
    for i, contact in enumerate(contacts, start=1):
        print(f'\nContact {i}')
        print(f'Name: {contact["name"]}')
        print(f'Phone: {contact["phone"]}')
        print(f'Email: {contact["email"]}')

def search_contact():
    search_name = input('Enter name to search: ').lower()

    for contact in contacts:
        if contact['name'].lower() == search_name:
            print('\nContact found:')
            print(f'Name: {contact["name"]}')
            print(f'Phone: {contact["phone"]}')
            print(f'Email: {contact["email"]}')
            return

    print('Contact not found.')
    
def main():
    while True:
        print('\nContact Book')
        print('1. Add contact')
        print('2. View contacts')
        print('3. Search contact')
        print('4. Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print('Goodbye.')
            break
        else:
            print('Invalid option.')


if __name__ == "__main__":
    main()
