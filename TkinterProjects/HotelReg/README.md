# Hotel Registrator App

> base.py
> 
Bu asosiy Frontend ko'rinishi Tkinter Packedidan foydalanilgan

> client.py
>
Bu fileda client class obyekt qabul qiladi 
```python
class Client:
    def __init__(self, full_name, email, dob, gender, address, phone, room, doj):
        self.full_name = full_name
        self.email = email
        self.dob = dob
        self.gender = gender
        self.address = address
        self.phone = phone
        self.room = room
        self.doj = doj
```
> journal.csv

Bu filega malumotlar yoziladi
