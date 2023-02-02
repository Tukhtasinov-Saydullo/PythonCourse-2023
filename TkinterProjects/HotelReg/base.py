from tkinter import Tk, Button, Label, messagebox, Entry, Radiobutton, StringVar, END
from tkcalendar import DateEntry
import os
import csv
from client import Client
import datetime

window = Tk()
window.title('Hotel')
window.geometry('480x480')
clients = []


def add():
    student = Client(
        fullname_entry.get(),
        email_entry.get(),
        dob_entry.get(),
        gender.get(),
        address_entry.get(),
        phone_entry.get(),
        room_entry.get(),
        datetime.datetime.now()
    )
    clients.append(student.get_attrs(as_dict=True))
    messagebox.showinfo("Information", "The data has been added successfully")


def clear():
    fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    room_entry.delete(0, END)


def save():
    with open("journal.csv", "a", newline="\n") as file:
        header = ['FullName', "Email", "DOB", "Gender", "Address", "Phone", "Room", "DOJ"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("journal.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerows(clients)
        messagebox.showinfo("Information", "Saved successfully")


# Fullname
fullname_label = Label(window, text="Fullname: ", padx=20, pady=10)
fullname_label.grid(row=0, column=0)
fullname_entry = Entry(window, width=30, borderwidth=3)
fullname_entry.grid(row=0, column=1)

# Email
email_label = Label(window, text="Email: ", padx=20, pady=10)
email_label.grid(row=1, column=0)
email_entry = Entry(window, width=30, borderwidth=3)
email_entry.grid(row=1, column=1)

# DOB - Date of birth
dob_label = Label(window, text="DOB: ", padx=20, pady=10)
dob_label.grid(row=2, column=0)
dob_entry = DateEntry(window)
dob_entry.grid(row=2, column=1)

# Gender
gender = StringVar()
GENDER_TYPES = {"male": "Male", "female": "Female"}
gender_label = Label(window, text="Gender: ", padx=20, pady=10)
gender_label.grid(row=3, column=0)
male_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("male"), value="male", variable=gender
)
male_radio_btn.place(x=110, y=125)
female_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("female"), value="female", variable=gender
)
female_radio_btn.place(x=180, y=125)
# Address
address_label = Label(window, text='Address: ', padx=20, pady=10)
address_label.grid(row=4, column=0)
address_entry = Entry(window, width=30, borderwidth=3)
address_entry.grid(row=4, column=1)
# Phone
phone_label = Label(window, text="Phone: ", padx=20, pady=10)
phone_label.grid(row=5, column=0)
phone_entry = Entry(window, width=30, borderwidth=3)
phone_entry.grid(row=5, column=1)

# Room
room_label = Label(window, text="Room: ", padx=20, pady=10)
room_label.grid(row=6, column=0)
room_entry = Entry(window, width=30, borderwidth=3)
room_entry.grid(row=6, column=1)
# Buttons

# Add
add_btn = Button(window, text="Add", padx=20, pady=10, command=add)
add_btn.place(x=40, y=265)

# Save
save_btn = Button(window, text="Save", padx=20, pady=10, command=save)
save_btn.place(x=120, y=265)

# Clear
clear_btn = Button(window, text="Clear", padx=20, pady=10, command=clear)
clear_btn.place(x=205, y=265)

# Quit
quit_btn = Button(window, text="Quit", padx=20, pady=10, command=window.quit)
quit_btn.place(x=290, y=265)
if __name__ == '__main__':
    try:
        window.mainloop()
    except KeyboardInterrupt as e:
        print("Dastur To'xtadi")
