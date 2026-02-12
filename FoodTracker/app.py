# imports
from multiprocessing.dummy import connection
import mysql.connector

# Constant variables

db = mysql.connector.connect(host="localhost", user="root", password="", database="food app") # Connects to database



Choices = ["add", "view", "remove", "lookup", "exit"] # valid user choices


# Checks if connected to database
if db.is_connected():
    print("Successfully connected to the database.")
else:
    print("Failed to connect to the database.")


# Functions

# Exits program
def exit_program():
    print("Exiting the program.")
    db.close()
    return

# adds item to list
def add_item(item, amount):
    # item = input("Enter the item to add: ").strip().lower()            Only used for text based interface, not GUI
    # amount = input("Enter the amount of the item: ").strip()
    
    mycursor = db.cursor()
    mycursor.execute("SELECT 1 FROM fooditems WHERE Name = %s", (item,))
    exists = mycursor.fetchone() is not None

    if exists:
        mycursor.execute("SELECT * FROM `fooditems` WHERE Name = %s", (item,))
        for x in mycursor:
            amount = int(amount) + int(x[2])
            mycursor.execute("UPDATE fooditems SET Amount = %s WHERE Name = %s", (amount, item))
            db.commit()
            print(f"Updated item: {item}. New amount: {amount}")

    else:
        mycursor.execute(f"INSERT INTO fooditems (name, Amount) VALUES ('{item}', '{amount}')")
        db.commit()
        print(f"Added {amount} {item}")


# view items in list
def view_items():
    print("Existing items:")
    mycursor = db.cursor()
    mycursor.execute("SELECT Name, Amount FROM fooditems")
    for x in mycursor:
        print(x[1], x[0])    

# removes item from list
def remove_item(item, amount):
    # item = input("Enter the item to remove: ").strip().lower()            Only used for text based interface, not GUI
    # amount = input("Enter the amount to remove: ").strip()

    mycursor = db.cursor()
    mycursor.execute("SELECT 1 FROM fooditems WHERE Name = %s", (item,))
    exists = mycursor.fetchone() is not None

    if exists:
        mycursor.execute("SELECT * FROM `fooditems` WHERE Name = %s", (item,))
        for x in mycursor:
            amount = int(x[2]) - int(amount)

            if amount > 0:
                mycursor.execute("UPDATE fooditems SET Amount = %s WHERE Name = %s", (amount, item))
                db.commit()
                print(f"Updated item: {item}. New amount: {amount}")

            else:
                mycursor.execute("DELETE FROM fooditems WHERE Name = %s", (item,))
                db.commit()
                print(f"Removed item: {item}")
    else:
        print(f"Item {item} does not exist.")

# lookup item in list
def lookup_item():
    item = input("Name of item to lookup: ").strip().lower()
    mycursor = db.cursor()
    mycursor.execute("SELECT 1 FROM fooditems WHERE Name = %s", (item,))
    exists = mycursor.fetchone() is not None

    print(mycursor.fetchone())

    if exists:
        print(f"{item} exists in the list.")
    else:
        print(f"{item} does not exist in the list.")


# --------------------- Text basexd interface ---------------------
# Comment all of below out to use the text based interface instead of the GUI


# # Main program loop
# while True:

# # Gets user choice
#     while True:
#         choice = input("Enter your choice: Add, View, Remove, Lookup or Exit ").strip().lower()
#         if choice in Choices:
#             print(f"Choice: {choice}" )
#             break
#         else:
#             print("Invalid input, please choose again")

# # Executes user choice

#     if choice == "exit":
#         exit_program()
#         break
#     elif choice == "add":
#         add_item()
#     elif choice == "view":
#         view_items()
#     elif choice == "remove":
#         remove_item() 
#     elif choice == "lookup":
#         lookup_item()