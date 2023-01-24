import csv


class CSVManager:
    def __init__(self, file_path, ):
        self.file_path = file_path

    def get_data(self):
        try:
            with open(self.file_path, ) as file:
                csv_reader = csv.reader(file)
                return [row for row in csv_reader]
        except FileNotFoundError as e:
            print(e)

    def get_language_info(self, programming_lang):
        data = self.get_data()
        header = [item.lower() for item in data.pop(0)]
        if programming_lang.lower() not in header:
            return "Language not found."

        target_index = None
        for index, item in enumerate(header):
            if programming_lang == item:
                target_index = index

        result = f"{programming_lang.title()}\n"
        for row in data:
            result += f"{row[0]}: {row[target_index]}\n"

            return result


csv_obj = CSVManager('files/Most Popular Programming Languages from 2004 to 2022.csv')
print(csv_obj.get_data)
