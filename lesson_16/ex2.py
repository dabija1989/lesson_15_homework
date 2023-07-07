"""
Create o programa python care deschide fiserul ex_2_file.txt gasit aici si va afisa ce contine
fisierul.
"""
# Solution
import os

# In dependenta de locatia fisierului specifici adresa sa.
desktop_path = os.path.expanduser("C:\\Users\dabij\OneDrive\Desktop")
file_path = os.path.join(desktop_path, "ex_2_file.txt")

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")