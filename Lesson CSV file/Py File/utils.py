import csv


def reading_csv(file_path):
    with open(file_path) as f:
        data = [[value.strip() for value in row] for row in csv.reader(f)]
    return data
