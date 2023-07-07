"""
Creati un program care va avea 2 optiuni:
• Afiseaza toate bucatele
   • Va afisa toate bucatele stocate intr-un fisier
• Adauga bucata
   • Va adauga o bucata in lista din fisier
Daca utilizatorul re-porneste programul, la afisarea bucatelor, trebuie sa fie
afisate toate elementele salvate anterior.
"""
# Solution
import json


def incarca_bucatele():
    try:
        with open("meniu.json", "r") as file:
            meniu = json.load(file)
    except FileNotFoundError:
        meniu = []

    return meniu


def meniu_salvat(meniu):
    with open("meniu.json", "w") as file:
        json.dump(meniu, file)


def list_dishes():
    meniu = incarca_bucatele()
    if not meniu:
        print("Nu am gasit nici un meniu!")
    else:
        print("Lista cu meniul:")
        for bucate in meniu:
            print("- " + bucate)


def add_dish():
    bucate = input("Enter the name of the dish: ")
    meniu = incarca_bucatele()
    meniu.append(bucate)
    meniu_salvat(meniu)
    print("Dish added successfully.")


def main():
    while True:
        print("\nOptiuni:")
        print("1. Lista cu meniul")
        print("2. Adauga bucate")
        print("3. Finisare")

        choice = input("Alege optiunea dorita:\n\tTasteaza 1 - pentru lista cu meniul."
                       "\n\tTasteaza 2 - pentru a adauga noi bucate."
                       "\n\tTasteaza 3 - pentru a finisa.\n")

        if choice == "1":
            list_dishes()
        elif choice == "2":
            add_dish()
        elif choice == "3":
            break
        else:
            print("Optiune invalida. Te rog mai incearca odata.")

    print("La revedere!")


if __name__ == "__main__":
    main()
