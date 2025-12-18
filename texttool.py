#!/usr/bin/env python3

"""
Ce module fournit une suite d'outils en ligne de commande pour la manipulation de texte.
Il permet d'effectuer des opérations telles que la mise en majuscules, en minuscules,
le calcul de longueur ou l'ajout de préfixes sur des chaînes de caractères.
"""


def process_line(line):
    """
    Traite une ligne de texte, extrait la commande et l'argument, 
    puis retourne le résultat de l'opération demandée.
    """
    if " " not in line:
        return "No command or no argument given"

    cmd, text = line.split(" ", maxsplit=1)

    if cmd == "uppercase":
        return text.upper()
    if cmd == "lowercase":
        return text.lower()
    if cmd == "length":
        return len(text)
    if cmd == "prefix":
        return text[:10]

    # >>> AJOUT DE L'UTILISATEUR A (length)
    if cmd == "length": # L'utilisateur A rajoute une commande length
        return len(text)
    # <<<

    return "Unknown command " + cmd

def main():
    while True:
        try:
            line = input("commade> ")
        except EOFError:
            break

        print(process_line(line))


if __name__ == "__main__":
    main()
