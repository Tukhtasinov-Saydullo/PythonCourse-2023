from transliterate import to_cyrillic
from tkinter import Tk, Label, Button, Radiobutton, Text, Entry, messagebox

# Window
window = Tk()
window.title('To Cyrillic')
window.geometry('480x240')

# Input
label_input = Label(window, text='Input: ', padx=10, pady=10)
label_input.grid(row=1, column=0)
label_entry = Entry(window)
label_entry.grid(row=1, column=1)


# Command
def to_cyrillic_app():
    text = label_entry.get()
    result_ = to_cyrillic(text)
    result.config(text=result_)


# Button
to_cyrillic_btn = Button(window, pady=10, padx=40, text='To Cyrillic', command=to_cyrillic_app)
to_cyrillic_btn.grid(row=2, column=1)

# Output
label_output = Label(window, text='Output: ', padx=10, pady=10)
label_output.grid(row=3, column=0)
result = Label(window, text='', pady=10, padx=10)
result.grid(row=3, column=1)
if __name__ == '__main__':
    window.mainloop()
