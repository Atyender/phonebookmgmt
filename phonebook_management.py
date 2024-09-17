import csv
import re
import os
from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, phone_number, email_address=None, address=None):
        # Initializes a new contact with the provided details.
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address
        self.created_at = datetime.now()  # Record the creation time of the contact
        self.updated_at = datetime.now()  # Record the last update time of the contact
        self.history = []  # A list to store the history of changes made to the contact

    def __str__(self):
        # Returns a string representation of the contact.
        return f"{self.first_name} {self.last_name}, {self.phone_number}, {self.email_address}, {self.address}"

    def add_history(self, operation):
        #Adds a history log for the contact, recording the operation and the timestamp.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"{timestamp} - {operation}")

    def view_history(self):
        #Prints the contact's change history.
        for entry in self.history:
            print(entry)

class PhoneBook:
    def __init__(self):
        #Initializes a PhoneBook with an empty contacts list and an empty log.
        self.contacts = []  # List to store all contacts
        self.log = []  # List to store the log of operations performed

    def add_contact(self, contact):
        #Adds a new contact to the phone book and logs the operation.
        self.contacts.append(contact)  # Add the contact to the contacts list
        contact.add_history("Contact created")  # Log the contact creation in the contact's history
        self.log_operation(f"Added contact: {contact}")  # Log the addition of the contact in the global log

    def view_contacts(self):
        #Displays all contacts in the phone book.
        for contact in self.contacts:
            print(contact)  # Print each contact in the list

    def search_contacts(self, query):
        #Searches for contacts by first name, last name, or phone number.
        results = [contact for contact in self.contacts if re.search(query, contact.first_name, re.IGNORECASE) or 
                                                      re.search(query, contact.last_name, re.IGNORECASE) or 
                                                      re.search(query, contact.phone_number)]
        if results:  # If matching contacts are found, print them
            for result in results:
                print(result)
        else:
            print("No contacts found matching your search query.")  # Notify if no results

    def search_by_time_frame(self, start_date, end_date):
        #Searches for contacts added within a specific date range.
        start = datetime.strptime(start_date, "%Y-%m-%d")  # Convert input string to date format
        end = datetime.strptime(end_date, "%Y-%m-%d")
        results = [contact for contact in self.contacts if start <= contact.created_at <= end]
        
        if results:  # If matching contacts are found, print them
            for result in results:
                print(result)
        else:
            print(f"No contacts found between {start_date} and {end_date}.")  # Notify if no results

    def update_contact(self, first_name, last_name, new_contact):
        #Updates an existing contact based on the first and last name.
        for i, contact in enumerate(self.contacts):  # Find the contact based on first and last name
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                self.contacts[i] = new_contact  # Replace the old contact with the updated one
                new_contact.add_history("Contact updated")  # Log the update in the contact's history
                self.log_operation(f"Updated contact: {new_contact}")  # Log the update in the global log
                break
        else:
            print(f"No contact found with the name {first_name} {last_name}")  # Notify if no contact is found

    def delete_contact(self, first_name, last_name):
    #Deletes a contact based on the first and last name.
        matching_contacts = [contact for contact in self.contacts if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower()]
        if not matching_contacts:
            print(f"No contact found with the name {first_name} {last_name}.")
            return
        # Delete the first matching contact
        contact_to_delete = matching_contacts[0]
        self.contacts.remove(contact_to_delete)
        self.log_operation(f"Deleted contact: {first_name} {last_name}")
        print(f"Contact {first_name} {last_name} deleted.")


    def delete_contacts_in_batch(self, names):
    #Deletes multiple contacts based on a list of first and last names.
        names_to_delete = [name.strip() for name in names]
        
        for name in names_to_delete:
            first_name, last_name = name.split()
            matching_contacts = [contact for contact in self.contacts if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower()]
            
            if not matching_contacts:
                print(f"No contact found with the name {first_name} {last_name}.")
                continue

            # Delete the first matching contact
            contact_to_delete = matching_contacts[0]
            self.contacts.remove(contact_to_delete)
            self.log_operation(f"Deleted contact: {contact_to_delete.first_name} {contact_to_delete.last_name}")
            print(f"Contact {contact_to_delete.first_name} {contact_to_delete.last_name} deleted.")


    def import_contacts_from_csv(self, file_path):
        #Imports contacts in bulk from a CSV file.
        if os.path.exists(file_path):  # Check if the CSV file exists
            with open(file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)  # Read the CSV file
                contacts_imported = 0
                for row in csv_reader:
                    # Create a contact from each row of the CSV file
                    contact = Contact(row['First Name'], row['Last Name'], row['Phone Number'], row.get('Email'), row.get('Address'))
                    self.add_contact(contact)  # Add the contact to the phone book
                    contacts_imported += 1
                print(f"Successfully imported {contacts_imported} contacts from {file_path}.")
        else:
            print(f"Error: File not found at {file_path}. Please check the file path.")  # Notify if the file is not found

    def sort_contacts(self, by="first_name"):
        #Sorts the contacts by the specified field (first_name or last_name).
        self.contacts = sorted(self.contacts, key=lambda x: getattr(x, by))  # Sort the contacts based on the given field
        print(f"Contacts sorted by {by}:")
        self.view_contacts()  # Display the sorted contacts

    def group_contacts_by_last_name(self):
        #Groups contacts alphabetically by the initial letter of their last names.
        grouped = {}
        for contact in self.contacts:  # Group contacts by the first letter of their last name
            first_letter = contact.last_name[0].upper()
            grouped.setdefault(first_letter, []).append(contact)
        for letter, group in grouped.items():  # Print each group of contacts
            print(f"\nContacts starting with {letter}:")
            for contact in group:
                print(contact)

    def log_operation(self, operation):
        #Logs an operation with a timestamp and stores it in the log.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
        self.log.append(f"{timestamp} - {operation}")  # Add the operation to the log

    def view_log(self):
        #Displays the log of all operations performed.
        for entry in self.log:
            print(entry)  # Print each log entry

    def validate_phone_number(self, phone_number):
        #Validates that the phone number matches the format (###) ###-####.
        pattern = re.compile(r"\(\d{3}\) \d{3}-\d{4}")  # Regex pattern for phone number validation
        return pattern.match(phone_number)  # Return whether the phone number is valid

    def validate_email(self, email):
        #Validates the email address using a basic regex pattern.
        pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")  # Regex pattern for email validation
        return pattern.match(email)  # Return whether the email is valid

def main():
    #Main function to run the phone book management system.
    phonebook = PhoneBook()

    while True:
        # Menu for user options
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contacts\n4. Search by Time Frame\n5. Update Contact\n6. Delete Contact\n7. Batch Delete Contacts\n8. Import Contacts from CSV\n9. Sort Contacts\n10. Group Contacts by Last Name\n11. View Log\n12. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new contact
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone_number = input("Phone Number (###) ###-####: ")
            if not phonebook.validate_phone_number(phone_number):
                print("Invalid phone number format.")
                continue
            email_address = input("Email Address (Optional): ")
            if email_address and not phonebook.validate_email(email_address):
                print("Invalid email address.")
                continue
            address = input("Address (Optional): ")
            contact = Contact(first_name, last_name, phone_number, email_address, address)
            phonebook.add_contact(contact)

        elif choice == '2':
            # View all contacts
            phonebook.view_contacts()

        elif choice == '3':
            # Search contacts by name or phone number
            query = input("Enter search query: ")
            phonebook.search_contacts(query)

        elif choice == '4':
            # Search contacts by the date they were added
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            phonebook.search_by_time_frame(start_date, end_date)

        elif choice == '5':
            # Update a contact by name
            first_name = input("Enter first name of the contact to update: ")
            last_name = input("Enter last name of the contact to update: ")
            new_first_name = input("New First Name: ")
            new_last_name = input("New Last Name: ")
            new_phone_number = input("New Phone Number (###) ###-####: ")
            if not phonebook.validate_phone_number(new_phone_number):
                print("Invalid phone number format.")
                continue
            new_email_address = input("New Email Address (Optional): ")
            if new_email_address and not phonebook.validate_email(new_email_address):
                print("Invalid email address.")
                continue
            new_address = input("New Address (Optional): ")
            new_contact = Contact(new_first_name, new_last_name, new_phone_number, new_email_address, new_address)
            phonebook.update_contact(first_name, last_name, new_contact)

        elif choice == '6':
            # Delete a contact by name
            first_name = input("Enter first name of the contact to delete: ")
            last_name = input("Enter last name of the contact to delete: ")
            phonebook.delete_contact(first_name, last_name)


        elif choice == '7':
            # Delete multiple contacts by name
            names = input("Enter names to delete (comma-separated, e.g., John Cena, Tom Cruise): ").split(',')
            phonebook.delete_contacts_in_batch(names)


        elif choice == '8':
            # Import contacts from a CSV file
            file_path = input("Enter CSV file path: ")
            phonebook.import_contacts_from_csv(file_path)

        elif choice == '9':
            # Sort contacts by first or last name
            by = input("Sort by (first_name/last_name): ")
            phonebook.sort_contacts(by)

        elif choice == '10':
            # Group contacts by the first letter of the last name
            phonebook.group_contacts_by_last_name()

        elif choice == '11':
            # View the operation log
            phonebook.view_log()

        elif choice == '12':
            # Exit the program
            break

        else:
            print("Invalid choice. Please try again.")  # Notify for invalid menu choice

if __name__ == "__main__":
    main()
