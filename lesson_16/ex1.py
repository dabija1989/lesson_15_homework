"""
Create o programa python care va crea un fisier conform unui nume (sau path) introdus de la consola.
"""
# Solution
filename = input("Introduceti numele fisierului: ")
extension = input("Introduceti extensia fisierului (e.g., txt, csv, etc.): ")

# Concatinam numele fisierului cu extensia lui
filename_with_extension = f"{filename}.{extension}"

# Deschide fisierul in modul de editare sau il creaza daca nu exista
with open(filename_with_extension, 'w') as file:
    # Efectueaza operatiile necesare in file
    # De exemplu scrie continut in file
    file.write("Acesta este un nou fisier.")

print(f"Fisierul '{filename_with_extension}' a fost creat cu succes.")