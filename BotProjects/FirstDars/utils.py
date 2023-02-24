import csv
import os


def write_csv(student):
    with open('students.csv', 'a', newline='\n') as file:
        header = ['chat_id', 'full_name']
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("students.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerows(student.get_attrs_for_csv_writer())
        print('Student Added!')
