# Dictionary-Based Phonebook

phonebook = {
    "AMIT": "9876543210",
    "RIYA": "9123456780",
    "Siya":"7890654321"
}

def add_contact():
    name = input("Enter name: ").strip().upper()
    if name in phonebook:
        print("Contact already exists!")
        return
    number = input("Enter number: ").strip()
    phonebook[name] = number
    print(f"{name} added successfully!")

def search_contact():
    query = input("Enter name to search: ").strip().upper()
    results = {n: p for n, p in phonebook.items() if query in n}
    if results:
        for name, number in results.items():
            print(f"{name} : {number}")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ").strip().upper()
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted!")
    else:
        print("Contact not found!")

while True:
    print("\n1. Add  2. Search  3. Delete  4. View All  5. Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        for name, number in phonebook.items():
            print(f"{name} : {number}")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")