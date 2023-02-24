class Student:
    def __init__(self, chat_id, full_name):
        self.chat_id = chat_id
        self.full_name = full_name

    def get_attrs(self):
        return {
            'chat_id': self.chat_id,
            'full_name': self.full_name,
        }
