#main.py
from contact import Contact
from contact_book import ContactBook

def main():
    contact_book = ContactBook
    while True:
        print("\nContact Book Menu:")
        print("1.Add Contact")
        print("2.Display All Contacts")
        print("3.Search Contact")
        print("4.Exit")
        choice = input("Enter your choice(1/2/3/4):")
        if choice=='1':
            name =input("Enter name:")
            phone=input("Enter phone number:")
            email=("Enter email:")
            new_contact=Contact(name,phone,email)
            contact_book.add_contact(new_contact)
            print("Contact added successfully!")
        elif choice=='2':
            print("\nAll contact:")
            contact_book.display_all_contacts()
        elif choice=='3':
            name_to_search=input("Enter name to search:")
            found_contact=contact_book.search_contact(name_to_search)
            if found_contact:
                print("\nContact found:") 
                found_contact.display_contact()
            else:
                print("contact not found.")   
        elif choice=='4':
            print("Exiting Contact Book. Goodbye!")
            break   
        else:
            print("invalid choice.please enter a valid option")     
main()    



