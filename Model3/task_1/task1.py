import csv


class CSVManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        try:
            with open(self.file_path) as csv_file:
                csv_reader = csv.reader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)

    def get_dict_version(self):
        try:
            with open(self.file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)


csv_obj = CSVManager('files/Employee_Information.csv')

print(csv_obj.get_dict_version())
