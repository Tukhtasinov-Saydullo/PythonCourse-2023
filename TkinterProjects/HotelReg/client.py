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

    def get_attrs(self, as_dict=False):
        if as_dict:
            return {
                'FullName': self.full_name,
                'Email': self.email,
                'DOB': self.dob,
                'Gender': self.gender,
                'Address': self.address,
                'Phone': self.phone,
                'Room': self.room,
                'DOJ': self.doj

            }
        return {
            self.full_name,
            self.dob,
            self.gender,
            self.phone,
            self.email,
            self.room,
            self.doj,
        }
