class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"New owner: {new_owner} for vehicle with registration number {self.registration_number}")

if __name__ == "__main__":
    vehicle1 = Vehicle("ABC123", "Car", "Yuki")
    vehicle2 = Vehicle("DEF456", "Truck", "Otto")
    
    print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")
    
    vehicle1.update_owner("Nina T.")
    vehicle2.update_owner("Nico T.")
    
    print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")



# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and a method get_participant_count to retrieve the 
# current count.

# Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        return self.participant_count
    
event = Event("Conference", "2024-07-24")
event.add_participant()
event.add_participant()
print(event.get_participant_count())

import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="library_management_system"
    )
    return connection

class Book:
    def __init__(self, title, author_id, isbn, publication_date):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = True

    @staticmethod
    def add_book(book):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (book.title, book.author_id, book.isbn, book.publication_date, book.availability))
        connection.commit()
        cursor.close()
        connection.close()

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    @staticmethod
    def add_user(user):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        cursor.execute(query, (user.name, user.library_id))
        connection.commit()
        cursor.close()
        connection.close()

def main_menu():
    while True:
        print("Welcome to the Library Management System with Database Integration!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_operations()
        elif choice == "2":
            user_operations()
        elif choice == "3":
            author_operations()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    # Implement the book operations menu
    pass

def user_operations():
    # Implement the user operations menu
    pass

def author_operations():
    # Implement the author operations menu
    pass

if __name__ == "__main__":
    main_menu()