# Importation des modules
from sympy import symbols
import re

# Fonction pour la bienvenue du programme
def rectangle_bienvenue_complexe():
    # Définir la phrase et la largeur du rectangle
    phrase = " BIENVENUE "
    largeur = len(phrase) + 6  # Largeur avec marges supplémentaires pour le cadre
    hauteur = 5  # Hauteur du rectangle

    # Dessiner la première ligne (double bordure d'étoiles)
    print('*' * largeur)

    # Ligne avec bordure interne et espace
    print('*' + ' ' * (largeur - 2) + '*')

    # Ligne du milieu avec la phrase entourée de marges et bordure interne
    print('* *' + phrase.center(largeur - 6) + '* *')

    # Ligne avec bordure interne et espace
    print('*' + ' ' * (largeur - 2) + '*')

    # Dernière ligne (double bordure d'étoiles)
    print('*' * largeur)



#Fonction permettant le choix de la methode
def methode_resolution():
    print("*******************Choisissez la méthode de résolution *******************\n")
    print("")
    print("                     1. La méthode de Dichotomie")
    print("                     2. La méthode de la Sécante")  
    print("                     3. La méthode de Newton-raphson")
    print("                     4. La méthode du Point Fixe\n")



#Implementation de la x
x = symbols('x')


# Fonction pour la saisie de la fonction
def saisir_fonction():
    
    # Affichage des options de type de fonction à l'utilisateur
    print("*******************Menus de choix de fonction *******************\n")
    print("Choisissez le type de fonction que vous souhaitez entrer :\n")
    print("     1. Polynôme (ex: x**2 + 3*x - 8)")
    print("     2. Trigonométrique (ex: sin(x), cos(x) + x)")
    print("     3. Logarithmique (ex: ln(x), log(x) + x**2)")
    print("     4. Racine carrée (ex: sqrt(x) + x/2)")
    print("     5. Rationnelle (ex: (x + 1) / (x - 2))\n")
    
    # Boucle principale pour choisir le type de fonction
    while True:
        # Demande à l'utilisateur de saisir le numéro correspondant au type de fonction
        type_fonction = input("Entrez le numéro du type de fonction : ").strip()
        
        # Vérification que le choix est bien un numéro entre 1 et 5
        if type_fonction not in {"1", "2", "3", "4", "5"}:
            # Message d'erreur si le choix est invalide
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.\n")
            continue  # Retourne au début de la boucle pour demander un choix valide

        # Boucle pour demander à l'utilisateur de saisir la fonction mathématique
        while True:
            # Demande la fonction mathématique et supprime les espaces, puis met en minuscules
            fonction = input("Entrez votre fonction mathématique : ").replace(" ", "").lower()
            
            # Définition de l'expression régulière et du message d'erreur selon le type de fonction
            if type_fonction == "1":  # Pour une fonction polynomiale
                pattern = r'[-+]?(\d+)?(x(\*\*\d+)?)?([+\-*/]?\d*(x(\*\*\d+)?)?)*'
                message_erreur = "Erreur : Veuillez entrer un polynôme valide en fonction de 'x' (ex: x**2 + 3*x - 8).\n"
            
            elif type_fonction == "2":  # Pour une fonction trigonométrique
                pattern = r'[-+]?((sin|cos|tan)\(?x\)?)?([+\-*/]\d*(sin|cos|tan)\(?x\)?)*'
                message_erreur = "Erreur : Veuillez entrer une fonction trigonométrique valide en fonction de 'x' (ex: sin(x) + cos(x)).\n"
            
            elif type_fonction == "3":  # Pour une fonction logarithmique
                pattern = r'[-+]?((ln|log)\(?x\)?)?([+\-*/]\d*(ln|log)\(?x\)?)*'
                message_erreur = "Erreur : Veuillez entrer une fonction logarithmique valide en fonction de 'x' (ex: ln(x), log(x) + x**2).\n"
            
            elif type_fonction == "4":  # Pour une fonction de racine carrée
                pattern = r'[-+]?sqrt\(?x\)?([+\-*/]\d*sqrt\(?x\)?)*'
                message_erreur = "Erreur : Veuillez entrer une fonction de racine carrée valide en fonction de 'x' (ex: sqrt(x) + x/2).\n"
            
            elif type_fonction == "5":  # Pour une fonction rationnelle
                pattern = r'[-+]?(\(?\d*(x)?\)?[+\-*/]?\(?\d*(x)?\)?)*'
                message_erreur = "Erreur : Veuillez entrer une fonction rationnelle valide en fonction de 'x' (ex: (x + 1) / (x - 2)).\n"
            
            # Vérification de la fonction saisie par l'utilisateur à l'aide de l'expression régulière
            if re.fullmatch(pattern, fonction):
                # Si la fonction est valide, affichage d'un message de confirmation
                print(f"Votre fonction saisie '{fonction}' est correcte.\n")
                return fonction  # Retourne la fonction valide et termine la fonction
            else:
                # Si la fonction est invalide, affichage d'un message d'erreur spécifique
                print(message_erreur)






















