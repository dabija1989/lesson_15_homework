"""
Creati un program care va citi un fisier textual conform unui path, din input.
Programul va afisa linia din text care are cea mai mare lungime.
"""


# Solution
def find_longest_line(file_name):
    max_line = ''
    max_word_count = 0

    try:
        with open(file_name, 'r') as file:
            for line in file:
                word_count = len(line.split())
                if word_count > max_word_count:
                    max_word_count = word_count
                    max_line = line.rstrip('\n')

        if max_word_count > 0:
            print(f"Linia cea mai lunga are {max_word_count} cuvinte.\nAceasta este linia cu cele mai multe cuvinte:")
            print(max_line)
        else:
            print("Fisierul este gol.")
    except FileNotFoundError:
        print("Fisierul nu a fost gasit.")


# Example usage
file_name = "C:\\Users\dabij\OneDrive\Desktop\large_text_file.txt"
find_longest_line(file_name)
