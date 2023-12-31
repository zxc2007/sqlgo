import os
import sys


def common_column():
    filename = "commonc.txt" 
    current_directory = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(current_directory, filename) 

    with open(file_path, "r") as file: 
        payload = file.read()
        rows = payload.split("\n") 
        sorted_rows = sorted(rows) 
        sorted_payload = "\n".join(sorted_rows)
        for column in sorted_payload.split("\n"):
            if column.startswith("#"):
                continue

            yield column

