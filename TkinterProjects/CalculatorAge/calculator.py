from tkinter import Tk, Button, Label, messagebox, Entry
from tkcalendar import DateEntry
import datetime

window = Tk()
window.title('Age Calculator')
window.geometry('480x360')


def calculator_age():
    try:
        birthdate = datetime.datetime.strptime(dob_entry.get(), '%Y-%m-%d')
        today = datetime.datetime.now()
        age = birthdate.year - today.year
        messagebox.showinfo("Age", f"Your Age {age}")
    except ValueError:
        messagebox.showinfo('Error', ' Invalid Date ')


central_label = Label(window, text='Age Calculator', fg='red')
central_label.grid(padx=190)

birth_of_day = Label(window, text="Birth of Day[YYYY-M-D]: ", fg='black')
birth_of_day.grid(padx=10, pady=10)
dob_entry = Entry(window, width=30, borderwidth=3)
dob_entry.grid(padx=20, pady=5)

calc_button = Button(window, text='check', width=28, command=calculator_age)
calc_button.grid(padx=30, pady=5)
if __name__ == '__main__':
    window.mainloop()
