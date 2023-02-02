import csv
from tkinter import Tk, Label, Entry, Button
import class_task
import datetime
import os

window = Tk()
window.title('Todo App')
window.geometry('400x500')


def add():
    file_path = 'tasks.csv'
    task = class_task.Task(name=task_entry.get(), created_at=datetime.datetime.now())
    with open(file_path, "a", newline="\n") as f:
        header = ["id", "name", "created_at", "updated_at"]
        dict_writer = csv.DictWriter(f, header)
        if os.path.getsize(file_path) == 0:
            dict_writer.writeheader()
        dict_writer.writerow(task.get_attrs_as_dict())


def clear_csv():
    file_path = 'tasks.csv'
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])


task_name = Label(window, text='Task Name: ')
task_name.place(x=10, y=10)
task_entry = Entry(window, width=15)
task_entry.place(x=100, y=10)

add_button = Button(window, text='Add', width=28, command=add)
add_button.place(x=60, y=40)

clear_btn = Button(window, text='Clear', width=28, command=clear_csv)
clear_btn.place(x=60, y=80)
if __name__ == '__main__':
    window.mainloop()
