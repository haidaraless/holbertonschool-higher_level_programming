#!/usr/bin/python3
"""
CSV to JSON conversion
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    convert CSV data to JSON format and save to data.json
    """
    try:
        data_list = []

        with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data_list.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
