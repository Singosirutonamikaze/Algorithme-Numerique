#Importation des modules necessaires
from sympy import symbols, sympify, sin, cos, tan, log, sqrt
import re

# Fonction pour afficher un message de bienvenue avec un cadre de texte
def rectangle_bienvenue_complexe():
    # Définir la phrase à afficher et calculer la largeur du rectangle
    phrase = " BIENVENUE "  # Texte à afficher
    largeur = len(phrase) + 6  # Largeur du rectangle (avec une marge de 3 caractères de chaque côté)
    hauteur = 5  # Hauteur du rectangle (fixée à 5 lignes)

    # Dessiner la première ligne du rectangle (bordure supérieure avec des étoiles)
    print('*' * largeur)

    # Ligne avec une bordure interne et des espaces à l'intérieur
    print('*' + ' ' * (largeur - 2) + '*')

    # Ligne du milieu avec le texte "BIENVENUE" centré
    print('* *' + phrase.center(largeur - 6) + '* *')

    # Ligne avec une bordure interne et des espaces à l'intérieur
    print('*' + ' ' * (largeur - 2) + '*')

    # Dernière ligne (bordure inférieure avec des étoiles)
    print('*' * largeur)

# Fonction permettant de choisir la méthode de résolution parmi plusieurs options
def methode_resolution():
    print("*******************Choisissez la méthode de résolution *******************\n")
    print("                     1. La méthode de Dichotomie")
    print("                     2. La méthode de la Sécante")  
    print("                     3. La méthode de Newton-raphson")
    print("                     4. La méthode du Point Fixe\n")

# Initialisation de 'x' pour pouvoir l'utiliser comme symbole dans les expressions mathématiques
x = symbols('x')

# Fonction générique pour permettre à l'utilisateur de saisir une fonction mathématique
def saisir_fonction():
    # Affichage du menu pour choisir le type de fonction
    print("*******************Menus de choix de fonction *******************\n")
    print("Choisissez le type de fonction que vous souhaitez entrer :\n")
    print("     1. Polynôme (ex: x**2 + 3*x - 8)")
    print("     2. Trigonométrique (ex: sin(x), cos(x) + x)")
    print("     3. Logarithmique (ex: ln(x), log(x) + x**2)")
    print("     4. Racine carrée (ex: sqrt(x) + x/2)")
    print("     5. Rationnelle (ex: (x + 1) / (x - 2))")
    print("     6. Fonction générale\n")

    # Dictionnaire contenant les types de fonction disponibles avec des exemples
    types_fonction = {
        "1": "Polynôme (ex: x**2 + 3*x - 8)",
        "2": "Trigonométrique (ex: sin(x), cos(x) + x)",
        "3": "Logarithmique (ex: ln(x), log(x) + x**2)",
        "4": "Racine carrée (ex: sqrt(x) + x/2)",
        "5": "Rationnelle (ex: (x + 1) / (x - 2))",
        "6": "Fonction générale (ex: x**3 - sin(x) + log(x))"
    }

    # Boucle principale pour permettre à l'utilisateur de choisir un type de fonction
    while True:
        # Demander à l'utilisateur de choisir un type de fonction
        type_fonction = input("Entrez le numéro du type de fonction : ").strip()

        # Vérifier si le choix est valide
        if type_fonction not in types_fonction:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.\n")
            continue

        # Demander à l'utilisateur de saisir la fonction mathématique
        while True:
            # Supprimer les espaces et mettre tout en minuscules pour faciliter l'analyse
            fonction = input("Entrez votre fonction mathématique : ").replace(" ", "").lower()

            # Expression régulière pour valider la fonction mathématique
            pattern = r"^([-+]?[0-9]*\.?[0-9]+(?:\*?\*?[xX](?:\^?[0-9]+)?)?|[a-zA-Z]+\([^\)]*\))(?:[+\-*/^]([-+]?[0-9]*\.?[0-9]+(?:\*?\*?[xX](?:\^?[0-9]+)?)?|[a-zA-Z]+\([^\)]*\)))*$"

            
            # Vérification si la fonction correspond au modèle
            if re.fullmatch(pattern, fonction):
                try:
                    # Essayer de convertir la fonction en une expression sympy
                    fonction_sympy = sympify(fonction)
                    # Afficher un message de confirmation si la fonction est valide
                    print(f"Votre fonction saisie '{fonction}' est correcte.\n")
                    return fonction_sympy
                except:
                    # En cas d'erreur de parsing, afficher un message d'erreur
                    print("Erreur : Impossible de parser la fonction. Veuillez vérifier votre saisie.\n")
            else:
                # Si la fonction ne correspond pas au modèle, afficher un message d'erreur
                print("Erreur : La fonction saisie n'est pas valide. Essayez à nouveau.\n")

# Fonction pour demander la tolérance et le nombre d'itérations
def saisir_tolerance_et_iterations():
    while True:
        try:
            # Demander la tolérance avec prise en charge des notations scientifiques
            tolerance_input = input("Entrez la tolérance souhaitée (ex: 0.0001, 1.0e-5, 1e-6) : \n")
            # Convertir l'entrée en nombre flottant
            tolerance = float(tolerance_input)

            # Demander le nombre maximal d'itérations
            nombre_max_iterations = int(input("Entrez le nombre maximal d'itérations (ex: 100) : \n"))
            
            # Vérifier que la tolérance et le nombre d'itérations sont valides (supérieurs à zéro)
            if tolerance > 0 and nombre_max_iterations > 0:
                print(f"Votre tolérance est : {tolerance}")
                print(f"Votre nombre maximal d'itérations est : {nombre_max_iterations}\n")
                return tolerance, nombre_max_iterations
            else:
                print("Erreur : la tolérance et le nombre d'itérations doivent être supérieurs à zéro.")
        
        except ValueError:
            print("Erreur : veuillez entrer des valeurs numériques valides pour la tolérance (flottant) et un entier pour le nombre d'itérations.")





