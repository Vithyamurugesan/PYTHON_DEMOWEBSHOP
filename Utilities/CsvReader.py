import csv
import os

class CsvReader:

    @staticmethod
    def _resolve_path(file_path):
        if os.path.isabs(file_path):
            return file_path

        base_dir = os.path.dirname(os.path.dirname(__file__))
        return os.path.join(base_dir, file_path)

    @staticmethod
    def get_data(file_path):
        data = []

        with open(CsvReader._resolve_path(file_path), mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        return data

    @staticmethod
    def get_wishlist_data(file_path, testcase):
        data = []

        with open(CsvReader._resolve_path(file_path), newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["testcase"] == testcase:
                    data.append(row["product"])

        return data