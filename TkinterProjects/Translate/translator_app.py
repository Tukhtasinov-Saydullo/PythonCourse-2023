from tkinter import Tk, Button, Label, StringVar, Entry, OptionMenu, messagebox
import requests


def translate():
    source_text = text_entry.get()
    target_language = select_lang.get()
    response = requests.get(
        f"https://translate.google.com/translate_a/single?client=gtx&sl=auto&tl={target_language}&dt=t&q={source_text}")
    result = response.json()[0][0][0]
    result_entry.config(text=result)


window = Tk()
window.title('Alternative Google Translator')
window.geometry('480x480')

# Text Label
text_label = Label(window, text='Text:')
text_label.grid(row=0, column=0, padx=10, pady=10)

# Text Entry
text_entry = Entry(window, width=30, font=('Arial', 12))
text_entry.grid(row=0, column=1, pady=10, padx=10)

# Select Label
select_lang = StringVar()
select_lang.set('en')
select_label = Label(window, text='Select Language:')
select_label.grid(row=1, column=0, padx=10, pady=10)

# Select Menu
code_lang = ['uz', 'ru', 'en']
select_menu = OptionMenu(window, select_lang, *code_lang)
select_menu.grid(row=1, column=1, padx=10, pady=10)

# Button Command
translate_button = Button(window, text='Translate', padx=75, pady=10, command=translate)
translate_button.grid(row=2, column=1, pady=10, padx=10)

# Result Label
result_label = Label(window, text='Result:')
result_label.grid(row=6, column=0)
result_entry = Label(window, text='', width=30, font=('Arial', 12))
result_entry.grid(row=6, column=1, pady=30, padx=10)

if __name__ == '__main__':
    window.mainloop()
