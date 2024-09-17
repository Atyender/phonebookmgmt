**Phone Book Management System**

This is a Python-based command-line application that allows a user to manage a list of contacts.
User can perform several operations like adding, viewing, searching, updating, deleting contacts, and importing them from a CSV file.
The system stores each contact’s first name, last name, phone number, email address, and physical address.

**Classes:**

Contact Class:

This class represents an individual contact. It stores the contact's first name, last name, phone number, email address, and physical address.
Each Contact object also keeps track of when it was created and updated.
It also stores a history of changes made to the contact (e.g., if it was updated), along with timestamps for each operation.

PhoneBook Class:

This is the main class that manages the collection of contacts. It provides all the functionalities like adding, updating, deleting, searching, and importing contacts.
The PhoneBook class also maintains a log of operations, such as when a contact is added or deleted. This helps the user keep track of all the changes made.

**Data Structures**


Contacts List:

The contacts are stored in a list. Each contact is an instance of the Contact class, which stores the details of a person, such as their name, phone number, and other details.

Log List:

Operations such as adding, updating, or deleting a contact are recorded in another list called log. This list stores a history of actions performed, including a timestamp for when the action took place.

**Functionalities:**

1. Add Contact: User can add new contacts by providing a first name, last name, phone number, and optionally an email address and physical address.
2. View Contacts: User can view all the contacts in the phone book. Each contact is displayed with its name, phone number, email address, and address.
3. Search Contacts: User can search for contacts using the first name, last name, or phone number. The search works even if the user types only part of the name or number.
4. Search by Time Frame: User can search for contacts that were added within a certain date range.
5. Update Contact: User can update a contact by entering the first and last name of the contact they want to update. After finding the contact, they can change any of the details, such as name, phone number, email, or address.
6. Delete Contact: User can delete a contacy by entering the first and last name. The first matching contact is deleted from the list.
7. Batch Delete Contacts: User can delete multiple contacts at once by entering a list of names.
8. Import Contacts from CSV: User can import contacts from a CSV file. Each row in the CSV becomes a new contact in the phone book.
9. Sort Contacts: User can sort the contacts either by first name or last name in alphabetical order.
10. Group Contacts by Last Name: User can group contacts by the first letter of their last name.
11. View Log: The system keeps track of every action (like adding or deleting a contact) and stores it in the log. The user can view this log to see the history of operations.
