
def dire_bonjour(nom):
    print(f"Bonjour, {nom} !")

def addition(a, b):
    resultat = a + b
    print(f"La somme de {a} et {b} est {resultat}")

def afficher_liste(liste):
    print("Voici la liste :")
    for element in liste:
        print(f"- {element}")

if __name__ == "__main__":
    dire_bonjour("Youcef")
    addition(3, 7)
    afficher_liste(["pomme", "banane", "orange"])
    print("Programme terminé.")