from tkinter import Tk, Label, Button, Entry, OptionMenu, StringVar, Text
from conf import get_user_request

window = Tk()
window.geometry('480x480')
window.title('Exchange')


# Command Func
def exchange_online():
    have_currency = var
    exchange_to = var2

# Label
label_amount = Label(window, text='Amount:', padx=10, pady=10, font=('Arial', 16))
label_amount.grid(row=1, column=0)

# Entry
entry_amount = Entry(window, font=('Arial', 16))
entry_amount.grid(row=1, column=2)

# Menu
options = ['UZS', 'RUB', 'USD', 'KZT', 'TRY']
var = StringVar(window)
var.set('USD')
option_menu = OptionMenu(window, var, *options, )
option_menu.grid(row=1, column=3)

# Button Exchange
ex_button = Button(window, text='Exchange', pady=10, padx=100, font=('Arial', 14), command=exchange_online)
ex_button.grid(row=2, column=2)

# Label
label_v2 = Label(window, text='Amount:', pady=10, padx=10, font=('Arial', 16))
label_v2.grid(row=3, column=0)
amount_ex = Text(window, width=20, height=1, font=('Arial', 16))
amount_ex.grid(row=3, column=2)

# Menu v2
options2 = ['UZS', 'RUB', 'USD', 'KZT', 'TRY']
var2 = StringVar(window)
var2.set('USD')
option_menu2 = OptionMenu(window, var2, *options2, )
option_menu2.grid(row=3, column=3)

if __name__ == '__main__':
    window.mainloop()
