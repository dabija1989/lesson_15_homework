"""
Creati un program python care va citi numele unui fisier de la consola.
Programul va crea un fisierl cu numele fisierului citit de la consola, apoi va intreba utilizatorul sa scrie un text.
Textul introdus de utilizator trebuie adaugat in fisier.
Apoi cititi din fisier textul introdus de utilizator.
"""
# Solution
def crearea_fisierului_text():
    file_name = input("Introduceti numele fisierului:\n")

    # Crearea fisierului
    with open(file_name, 'w') as file:
        text = input("Introduceti continutul dorit:\n")
        file.write(text)

    # Citirea fisierului si printatea continutului
    with open(file_name, 'r') as file:
        file_contents = file.read()
        print("Continutul fisierului:\n", file_contents)


# Apelarea funtiei pentru executia programului
crearea_fisierului_text()
