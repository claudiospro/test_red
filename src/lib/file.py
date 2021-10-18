import csv
import os


def save(file_path, data, header):
    """save file."""
    exist_file = True
    if not os.path.exists(file_path):
        exist_file = False
        with open(file_path, 'w'):
            pass

    with open(file_path, mode='a') as csv_file:
        writer = csv.writer(csv_file)
        if not exist_file:
            writer.writerow(header)
        writer.writerow(data)

