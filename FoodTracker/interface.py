from tkinter import *
from app import add_item, exit_program, view_items, remove_item, lookup_item

window =Tk()
window.geometry("600x400")
window.title("Food Tracker")
window.config(background="black")

food_counter = 0




label = Label(window, text="Food Tracker", font=("Arial", 48), bg="black", fg="white")
label.pack()

view_btn = Button(window, text="View Items", font=("Arial", 24), bg="green", fg="white", command=view_items)
view_btn.pack(pady=20)

exit_btn = Button(window, text="Exit", font=("Arial", 24), bg="red", fg="white", command=lambda: [exit_program(), window.quit()])
exit_btn.pack(pady=20)

add_btn = Button(window, text="Add Item", font=("Arial", 24), bg="blue", fg="white", command=lambda: add_item("apple", 1))
add_btn.pack(pady=20)

remove_btn = Button(window, text="Remove Item", font=("Arial", 24), bg="orange", fg="white", command=lambda: remove_item("apple", 1))
remove_btn.pack(pady=20)



window.mainloop()