# Importation des modules
from sympy import symbols, sympify, lambdify
from MethodeDeResolution import methode_de_dichotomie 
from MethodeDeResolution import methode_de_la_secante
from MethodeDeResolution import methode_de_newton_raphson
from MethodeDeResolution import methode_du_point_fixe
from AccueilEtMenus import rectangle_bienvenue_complexe
from AccueilEtMenus import methode_resolution
from AccueilEtMenus import saisir_fonction

#Implementation de la x
x = symbols('x')

# Menu pour choisir la méthode et tester les fonctions
def main():
    choix_recommencer_Terminer = ""
    action = True

    #Presentation du programme
    rectangle_bienvenue_complexe()

    # Boucle principale pour recommencer ou terminer
    while action:

        # Affichage du menu principal
        methode_resolution()

        # Boucle pour s'assurer que l'utilisateur saisit un entier valide entre 1 et 4
        while True:
            try:
                choix = int(input("Entrez le numéro de la méthode (1-4) : "))
                if (choix < 1 or choix > 4):
                    print("Erreur : le numéro doit être un entier compris entre 1 et 4.\n")
                else:
                    break  # Sortir de la boucle si le choix est valide
            except ValueError:
                print("Erreur : veuillez entrer un nombre entier.\n")

        # Affichage du choix de l'utilisateur
        print(f"Vous avez choisi la méthode numéro {choix}.\n")
        if (choix == 1):
            print("***************METHODE DE DICHOTOMIE***************\n")
        elif (choix == 2):
           print("***************METHODE DE LA SECANTE***************\n")
        elif choix == 3:
           print("***************METHODE DE NEWTON-RAPHSON***************\n")
        elif (choix == 4):
           print("***************METHODE DU POINT FIXE***************\n")
        else:
            print("votre choix est incorrecte.")

        
        while True:
            fonction_str = saisir_fonction()

            try:
                fonction_expr = sympify(fonction_str)
                print("Fonction interprétée : f(x) = ", fonction_expr)
                fonction = lambdify(x, fonction_expr, 'math')
                break
            except Exception as e:
                print("Il faut que fonction soit une fonction mathématique.", e)
                # Permettre a l'utilisateur de recommencer
                continue

        # Vérifie si le choix nécessite des bornes (Méthode de la Dichotomie ou de la Sécante)
        if (choix in [1, 2]):  # Vérifie si le choix est 1 ou 2
            while True:  # Boucle infinie pour continuer à demander jusqu'à ce que l'entrée soit valide
                try:
                    # Demander à l'utilisateur de saisir la borne inférieure et supérieure
                    try:
                        borne_inferieure = float(input("Entrez la borne inférieure de l'intervalle : "))  # Saisie de la borne inférieure
                        borne_superieure = float(input("Entrez la borne supérieure de l'intervalle : "))  # Saisie de la borne supérieure
                    except ValueError:
                        # Si l'utilisateur entre une valeur qui ne peut pas être convertie en float
                        print("Veuillez entrer un nombre entier ou réel (Exemple : 2 ou 2.56)")

                    # Vérifier que la borne inférieure est bien inférieure à la borne supérieure
                    if (borne_inferieure < borne_superieure):
                        break  # Si la condition est remplie, sortir de la boucle
                    else:
                        # Si la borne inférieure est supérieure ou égale à la borne supérieure
                        print("Erreur : la borne inférieure doit être inférieure à la borne supérieure.")

                except ValueError:
                    # Si une erreur se produit lors de la conversion en float
                    print("Erreur : veuillez entrer un nombre réel pour chaque borne.")
            
            # Présentation de l'intervalle une fois les entrées validées
            print(f"Votre intervalle est : [{borne_inferieure}; {borne_superieure}]")

        # Définir la tolérance et le nombre maximal d'itérations
        while True:
            try:
                tolerance = float(input("Entrez la tolérance souhaitée (ex: 0.0001 ou 1.0e-5 ou 1Oe-6 ou 10^-6) : \n"))
                nombre_max_iterations = int(input("Entrez le nombre maximal d'itérations (ex: 100) : \n"))
                
                if (tolerance > 0 and nombre_max_iterations > 0):
                    break
                else:
                    print("Erreur : les valeurs de tolérance et d'itérations doivent être supérieures à zéro.")

            except ValueError:
                print("Erreur : veuillez entrer des valeurs numériques pour la tolérance et un entier pour les itérations.")
            
            #Présentation de la tolérance et du nombre maximal d'itérations
            print(f"Votre tolérance est : {tolerance}\n")
            print(f"Votre nombre maximal d'itérations est : {nombre_max_iterations}\n")
        
        # Exécution de la méthode choisie par l'utilisateur
        if (choix == 1):
            racine = methode_de_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        elif (choix == 2):
            racine = methode_de_la_secante(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        elif choix == 3:
            derivee_fonction = lambdify(x, fonction_expr.diff(x), 'math')
            x_initiale = float(input("Entrez une estimation initiale de la racine (exemple: 2): Xo = "))
            racine = methode_de_newton_raphson(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations)
        elif (choix == 4):
            try:
                x_initiale = float(input("Entrez une estimation initiale de la racine  (exemple: 2): Xo = "))
                racine = methode_du_point_fixe(fonction, x_initiale, tolerance, nombre_max_iterations)
            except Exception as e:
                print("Erreur dans l'entrée de la fonction : ", e)
                continue

        # Affichage de la racine
        if (racine is not None):
            print("La racine trouvée est : ", racine)
        else:
            print("Aucune racine n'a été trouvée.")

        # Demande à l'utilisateur s'il veut recommencer ou quitter
        choix_recommencer_Terminer = input("Souhaitez-vous recommencer ? (oui/non) : \n").lower()

        if (choix_recommencer_Terminer == "oui"):
            action = True
        else:
            action = False

# Appel de la fonction principale
main()
