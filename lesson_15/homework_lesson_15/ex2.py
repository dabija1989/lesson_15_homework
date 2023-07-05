"""
Utilizand functiile dezvolatate in exercitiu 1 (de mai sus) creaza un program care va lua ca input un path
 la un folder.
ATENTIE: Folositi o mapa pentru test, cu fisiere incluse acolo doar pentru test, nu folositi mape personale
 sa nu fie afectate fisierele.
Programul va trebui sa redenumeasca toate fisierele in acea mapa in numere (de la 1 la n), ordonate dupa data
de create a acelor fisiere. os.path.getctime(file_path) - va intoarce data de creare a fisierului.
Programul nu trebuie sa rescrie extensia fisierului. fisier.extensie - De exemplu document.docx va
trebuie sa fie re-scris ca 1.docx.
Adaugati optiunea de a specifica un prefix: De exemplu, prefixul doc va redenumi toate fisierele in
urmatorul mod doc1.docx, doc2.png, doc3.pdf, doc4.docx....
"""
import os
import shutil

def rename_files_in_folder(path, prefix=None):
    if not os.path.exists(path):
        print("Error: Provided path does not exist.")
        return

    if not os.path.isdir(path):
        print("Error: Provided path is not a folder.")
        return

    def list_files_in_folder(path):
        files = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                files.append(item)

        return files

    files = list_files_in_folder(path)
    files.sort(key=lambda x: os.path.getctime(os.path.join(path, x)))

    sorted_files = []
    for i, file_name in enumerate(files, start=1):
        file_extension = os.path.splitext(file_name)[1]
        new_file_name = str(i)

        if prefix:
            new_file_name = f"{prefix}{new_file_name}"

        new_file_name += file_extension

        sorted_files.append((file_name, new_file_name))

    for old_file_name, new_file_name in sorted_files:
        old_file_path = os.path.join(path, old_file_name)
        new_file_path = os.path.join(path, new_file_name)

        shutil.move(old_file_path, new_file_path)
        print(f"Renamed {old_file_name} to {new_file_name}")

# Take folder path input from console
folder_path = input("Enter the path to the folder: ")

# Example usage
rename_files_in_folder(folder_path, prefix="doc")
