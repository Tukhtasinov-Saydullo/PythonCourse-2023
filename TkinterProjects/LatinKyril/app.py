from transliterate import to_cyrillic
from tkinter import Tk, Label, Button, Radiobutton, Entry, messagebox

# Window
window = Tk()
window.title('LatinCyrillic App')
window.geometry('480x240')

# Input
label_input = Label(window, text='Input: ', padx=10, pady=10)
label_input.grid(row=1, column=0)
label_entry = Entry(window)
label_entry.grid(row=1, column=1)

cyrill = 'To Cyrillic'
latin = 'To Latin'
# Commands Func
def to_cyrillic_func():
    text = label_entry.get()
    if len(text) == 0:
        messagebox.showinfo('Error', 'Enter Letters!')
    else:
        result_ = to_cyrillic(text)
        result.config(text=result_)


def to_latin_func():
    text = label_entry.get()
    if len(text) == 0:
        messagebox.showinfo('Error', 'Enter Letters!')
    else:
        result_ = to_cyrillic(text)
        result.config(text=result_)


# Button
to_cyrillic_btn = Radiobutton(window, pady=10, padx=40, text=cyrill, command=to_cyrillic_func)
to_cyrillic_btn.grid(row=2, column=1)
to_latin_btn = Radiobutton(window, pady=10, padx=10, text=latin, command=to_latin_func)
to_latin_btn.grid(row=2, column=2)
# Output
label_output = Label(window, text='Output: ', padx=10, pady=10)
label_output.grid(row=3, column=0)
result = Label(window, text='', pady=10, padx=10)
result.grid(row=3, column=1)
if __name__ == '__main__':
    window.mainloop()
