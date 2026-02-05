# imports
from multiprocessing.dummy import connection
import mysql.connector

# Constant variables

db = mysql.connector.connect(host="localhost", user="root", password="", database="food app") # Connects to database



Choices = ["add", "view", "remove", "exit"] # valid user choices


# Checks if connected to database
if db.is_connected():
    print("Successfully connected to the database.")
else:
    print("Failed to connect to the database.")


mycursor = db.cursor()
mycursor.execute(f"SELECT Name FROM fooditems WHERE Name = 'apple'")
result = mycursor.fetchone()

if result:
    print("Item exists in the database.")
else:
    print("Item does not exist in the database.")

# Functions

# Exits program
def exit_program():
    print("Exiting the program.")
    db.close()
    return

# adds item to list
def add_item():
    item = input("Enter the item to add: ").strip().lower()
    mycursor = db.cursor()
    mycursor.execute(f"INSERT INTO fooditems (Name) VALUES ('{item}')")
    db.commit()
    print(f"Added item: {item}")

# view items in list
def view_items():
    print("Existing items:")
    mycursor = db.cursor()
    mycursor.execute("SELECT Name FROM fooditems")
    for x in mycursor:
        print(x[0])    

# removes item from list
def remove_item():
    item = input("Enter the item to remove: ").strip().lower()
    mycursor = db.cursor()
    mycursor.execute(f"SELECT Name FROM fooditems WHERE Name = '{item}'")
    result = mycursor.fetchone()
    if result:
        mycursor.execute(f"DELETE FROM fooditems WHERE Name = '{item}'")
        db.commit()
        print(f"Removed item: {item}")
    else:
        print(f"Item '{item}' does not exist in the database.")

    
# Main program loop
while True:

# Gets user choice
    while True:
        choice = input("Enter your choice: Add, View, Remove or Exit ").strip().lower()
        if choice in Choices:
            print(f"Choice: {choice}" )
            break
        else:
            print("Invalid input, please choose again")

# Executes user choice

    if choice == "exit":
        exit_program()
        break
    elif choice == "add":
        add_item()
    elif choice == "view":
        view_items()
    elif choice == "remove":
        remove_item() 