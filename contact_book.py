from contact import Contact

class ContactBook:
    def __init__(self):
        self.contact=[]
    def add_contact(self,contact):
        self.contacts.append(contact)    
    def display_all_contacts(self):
        for contact in self.contacts:
            contact.display_contact()
            print("..................")
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower()==name.lower():
                return contact
        else:
            return None            