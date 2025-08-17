# empty dictionary
my_dict = {}

while True:
    print('\nContact Book App')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Search Contact')
    print('5. Delete Contact')
    print('6. Count Contacts')
    print('7. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':  # Add contact
        name = input('Enter name: ')
        if name in my_dict:
            print(f'Contact name {name} already exists.')
        else:
            age = input('Enter age: ')
            email = input('Enter email: ')
            phone = input('Enter phone number: ')
            my_dict[name] = {'age': int(age), 'email': email, 'phone': phone}
            print(f'Contact name {name} added successfully!')

    elif choice == '2':  # View contact
        name = input('Enter name to view: ')
        if name in my_dict:
            contact = my_dict[name]
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Phone: {contact['phone']}")
        else:
            print('Contact not found.')

    elif choice == '3':  # Update contact
        name = input('Enter name to update: ')
        if name in my_dict:
            age = input('Enter updated age: ')
            email = input('Enter updated email: ')
            phone = input('Enter updated phone number: ')
            my_dict[name] = {'age': int(age), 'email': email, 'phone': phone}
            print(f'Contact name {name} updated successfully!')
        else:
            print('Contact not found.')

    elif choice == '4':  # Search contact (case-insensitive)
        name = input('Enter name to search: ')
        found = False
        for contact_name, contact_info in my_dict.items():
            if contact_name.lower() == name.lower():
                print(f'Found contact - Name: {contact_name}, Age: {contact_info["age"]}, Email: {contact_info["email"]}, Phone: {contact_info["phone"]}')
                found = True
                break
        if not found:
            print('No contact found with that name.')

    elif choice == '5':  # Delete contact
        name = input('Enter name to delete: ')
        if name in my_dict:
            del my_dict[name]
            print('Contact deleted successfully!')
        else:
            print('Contact not found.')

    elif choice == '6':  # Count contacts
        print(f'Total contacts in address book: {len(my_dict)}')

    elif choice == '7':  # Exit
        print('Goodbye! Exiting...')
        break

    else:
        print('Invalid choice. Please try again.')
