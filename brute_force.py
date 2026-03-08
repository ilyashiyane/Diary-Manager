import itertools
import time
import json

def brute_force(name):
    #mot_secret = input("Entrez le mot secret (lettres et chiffres) : ")
    essais = 0
    longueur = 1  # commencer à 1
    caracteres = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&~"#'{[(-|`\_^@)]}=$*%<>?,.;/:!'''
    start = time.time()
    with open(r"C:/Users/Lenovo/Desktop/Mydiary/Users.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for user in data :
            if user["name"] == name :
               mot_secret = user["password"][0]

    while True:
        for combinaison in itertools.product(caracteres, repeat=longueur):
            essais += 1
            mot_teste = ''.join(combinaison)
            #return mot_teste
            if mot_teste == mot_secret:
                temps = time.time() - start
                print(f"\nLe mot '{mot_secret}' a été deviné !")
                print(f"Nombre d'essais : {essais}")
                print(f"Temps écoulé : {temps:.2f} secondes")
                #print("cc")
                return mot_teste, temps, essais
        longueur += 1  # on passe à la longueur suivante après avoir testé toutes les combinaisons de la longueur courante

#if __name__ == "__main__":
    #jeux()