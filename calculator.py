print("=== Calculatrice ===")

a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))

print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choix = input("Votre choix : ")

if choix == "1":
    print("Résultat :", a + b)
elif choix == "2":
    print("Résultat :", a - b)
elif choix == "3":
    print("Résultat :", a * b)
elif choix == "4":
    if b != 0:
        print("Résultat :", a / b)
    else:
        print("Erreur : division par zéro.")
else:
    print("Choix invalide.")
