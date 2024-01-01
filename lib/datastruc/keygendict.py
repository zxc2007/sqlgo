import os
import sys

sys.path.append(os.getcwd())

class Keygendict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.caps = {}

    def rm_None(self):
        keys_to_remove = []
        for key, value in self.caps.items():
            if value is None:
                keys_to_remove.append(key)

        for key in keys_to_remove:
            del self.caps[key]
    

# Create an instance of Keygendict
diction = Keygendict()

# Add key-value pairs to the dictionary
diction.caps['A'] = 1234567890
diction.caps['B'] = None

# Remove 'None' items
diction.rm_None()

# Print the dictionary contents after removal
print(diction.caps)