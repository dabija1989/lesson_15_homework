"""
Creati un program care va primi ca input o cale (path) de fisiere din calculator: ex: C:\Program Files\.
Programul va trebui sa afiseze o lista de toate fisierele din mapa introdusa in input (doar fisierele, si nu alte mape).
Daca calea introdusa nu este o mapa, programul trebuie sa arate urmatoarea eroare: Calea introdusa nu este o mapa.
Daca calea introdusa nu exista, programul va trebuie sa arate urmatoare eroare: Calea introdusa nu exista.

"""
import os

def list_files_in_folder(path):
    if not os.path.exists(path):
        print("Error: Provided path does not exist.")
        return

    if not os.path.isdir(path):
        print("Error: Provided path is not a folder.")
        return

    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            files.append(item)

    return files

# Get the path from the user
path = input("Enter the folder path: ")

# Call the function to list files
for path in list_files_in_folder(path):
    print(path)