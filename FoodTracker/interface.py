# Imports
from tkinter import *
from tkinter import ttk
from app import add_item, exit_program, view_items, remove_item, lookup_item

window =Tk()
window.geometry("600x400")
window.title("Food Tracker")


def render_window():
    for widget in window.winfo_children():
        widget.destroy()

    itemDataList = view_items()

    title_label = Label(window, text="Current Items:", width=50, font=("Arial", 48),)
    title_label.pack(pady=20)
    for x in itemDataList:
        row_frame = Frame(window)
        row_frame.pack(pady=10)

        minus_btn = Button(row_frame, text="-", height=1, width=3, font=("Arial", 12), bg="red", fg="white", command=lambda item=x[0]: remove_and_refresh(item))
        minus_btn.pack(side=LEFT, padx=10)

        item_label = Label(row_frame, text=f"{x[1]}x {x[0]}", font=("Arial", 24),)
        item_label.pack(side=LEFT, padx=10)
        
        plus_btn = Button(row_frame, text="+", height=1, width=3, font=("Arial", 12), bg="green", fg="white", command=lambda item=x[0]: add_and_refresh(item))
        plus_btn.pack(side=LEFT, padx=10)
    
    new_item_input = Entry(window, width=20, font=("Arial", 12))
    new_item_input.pack(pady=(20,5))

    new_button = Button(window, text="Add New Item", height=1, width=15, font=("Arial", 12), bg="blue", fg="white", command=lambda: new_and_refresh(new_item_input.get()))
    new_button.pack(pady=5)

def add_and_refresh(item):
    add_item(item, 1)
    render_window()

def remove_and_refresh(item):
    remove_item(item, 1)
    render_window()

def new_and_refresh(item):
    add_item(item, 1)
    render_window()

render_window()

window.mainloop()