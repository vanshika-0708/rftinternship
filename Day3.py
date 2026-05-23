#Dictionary based phonebook
phonebook={
    "AMIT":"9874563210",
    "RIYA":"9087065432",
    "Shivani":"4536732190",
    "Saniya":"789654321"
}
def add_contact():
   name=input("Enter name:").strip().upper()
   if name in phonebook:
      print("Contact already exist!")
      return
   number=input("Enter number:").strip()
   phonebook[name]=number
   print(f"{name} added successfully!")

def search_contact():
   query=("Enter name to search:").strip().upper()
   results={n:p for n,p in phonebook.items()if query in n }
   if results:
      for name,number in results.item():
         print("Contact not found!")

def delete_contact():
   name=input("Enter name to delete:").strip().upper()
   if name in phonebook:
      del phonebook[name]
      print(f"{name} deleted!")
   else:
      print("Contact not found!")

        
while True:
    print("\n1.Add 2.Search 3.Delete 4.View All 5.Exit")
    choice=input("Choose:")
    if choice =='1':
       add_contact()
    elif choice=='2':
       search_contact()
    elif choice=='3':
       delete_contact()
    elif choice=='4':
       for name,number in phonebook.items():
          print(f"{name}:{number}")
    elif choice=='5':
       print("Goodbye!")
       break
    else:
       print("Invalid Choice")   


       
     