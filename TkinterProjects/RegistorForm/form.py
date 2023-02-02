from tkinter import messagebox, END, Label, Entry, Button, Tk, Radiobutton, StringVar
from student import Student
from tkcalendar import DateEntry
from datetime import datetime
import os
import csv

window = Tk()

students = []
window.title("Student Registration")
window.geometry("480x480")


def add():
    student = Student(
        fullname_entry.get(),
        email_entry.get(),
        dob_entry.get(),
        gender.get(),
        phone_entry.get(),
        course_entry.get(),
        datetime.now()
    )
    students.append(student.get_attrs(as_dict=True))
    messagebox.showinfo("Information", "The data has been added successfully")


def save():
    with open("students.csv", "a", newline="\n") as file:
        header = ["Fullname", "Email", "DOB", "Gender", "Phone", "Course", "DOJ"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("students.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerows(students)
        messagebox.showinfo("Information", "Saved successfully")


def clear():
    fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    course_entry.delete(0, END)


# FullName
fullname_label = Label(window, text="Fullname: ", padx=20, pady=10)
fullname_label.grid(row=0, column=1)
fullname_entry = Entry(window, width=30, borderwidth=3)
fullname_entry.grid(row=0, column=2)

# Email
email_label = Label(window, text="Email: ", padx=20, pady=10)
email_label.grid(row=1, column=1)
email_entry = Entry(window, width=30, borderwidth=3)
email_entry.grid(row=1, column=2)

# Date of Brith
dob_label = Label(window, text="Date of Brith: ", padx=20, pady=10)
dob_label.grid(row=2, column=1)
dob_entry = DateEntry(window, width=30, borderwidth=3)
dob_entry.grid(row=2, column=2)

# Gender
gender = StringVar()
GENDER_TYPES = {"male": "Male", "female": "Female"}
gender_label = Label(window, text="Gender: ", padx=20, pady=10)
gender_label.grid(row=3, column=1)
male_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("male"), value="male", variable=gender
)
male_radio_btn.place(x=110, y=125)
female_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("female"), value="female", variable=gender
)
female_radio_btn.place(x=180, y=125)

# Phone
phone_label = Label(window, text="Phone: ", padx=20, pady=10)
phone_label.grid(row=4, column=1)
phone_entry = Entry(window, width=30, borderwidth=3)
phone_entry.grid(row=4, column=2)

# Course
course_label = Label(window, text="Course: ", padx=20, pady=20)
course_label.grid(row=5, column=1)
course_entry = Entry(window, width=30, borderwidth=3)
course_entry.grid(row=5, column=2)

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
    window.mainloop()
