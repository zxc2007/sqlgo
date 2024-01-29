import os
import sys
class ReadFile:
    def __init__(self,filename) -> None:
        self.filename = filename
    
    def __enter__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__)) 
        file_path = os.path.join(current_directory, self.filename) 

        with open(file_path, "r") as file: 
            payload = file.read()
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) 

            for file in sorted_payload.split("\n"):
                yield file
    
    def __exit__(self,exc_type,exc_value,traceback):
        pass

# with ReadFile("/Users/alimirmohammad/sqlgo-1/requirements.txt") as file:
#     files = file

#     for file in files:
#         print(file)