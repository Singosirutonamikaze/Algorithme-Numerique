# Importation des modules nécessaires pour le calcul symbolique et les méthodes de résolution
from sympy import symbols, sympify, lambdify
from MethodeDeResolution import methode_de_dichotomie, methode_de_la_secante, methode_de_newton_raphson, methode_du_point_fixe
from AccueilEtMenus import rectangle_bienvenue_complexe, methode_resolution, saisir_fonction, saisir_tolerance_et_iterations

# Définition du symbole 'x' qui sera utilisé dans les fonctions mathématiques
x = symbols('x')

def demander_bornes():
    """Demande à l'utilisateur de saisir les bornes inférieure et supérieure de l'intervalle."""
    while True:  # Boucle infinie pour continuer à demander tant que l'utilisateur ne donne pas de valeurs valides
        try:
            # Demander la saisie des bornes de l'intervalle
            borne_inferieure = float(input("Entrez la borne inférieure de l'intervalle : "))
            borne_superieure = float(input("Entrez la borne supérieure de l'intervalle : "))
            
            # Vérifier que la borne inférieure est bien inférieure à la borne supérieure
            if borne_inferieure < borne_superieure:
                return borne_inferieure, borne_superieure  # Si les bornes sont valides, les retourner
            else:
                print("Erreur : la borne inférieure doit être inférieure à la borne supérieure.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre réel valide pour chaque borne.")  # Gérer les erreurs de conversion

def main():
    action = True  # Variable pour contrôler si l'utilisateur souhaite recommencer ou quitter

    # Présentation du programme
    rectangle_bienvenue_complexe()

    # Boucle principale pour recommencer ou terminer
    while action:
        # Affichage du menu principal pour choisir la méthode de résolution
        methode_resolution()

        # Boucle pour s'assurer que l'utilisateur saisit un entier valide entre 1 et 4 pour choisir la méthode
        while True:
            try:
                choix = int(input("Entrez le numéro de la méthode (1-4) : "))  # Demander à l'utilisateur de choisir une méthode
                if 1 <= choix <= 4:  # Vérifier que le choix est entre 1 et 4
                    break  # Sortir de la boucle si le choix est valide
                else:
                    print("Erreur : le numéro doit être un entier compris entre 1 et 4.\n")  # Si le choix n'est pas valide
            except ValueError:
                print("Erreur : veuillez entrer un nombre entier.\n")  # Si l'entrée n'est pas un entier

        # Affichage de la méthode choisie
        if choix == 1:
            print("***************METHODE DE DICHOTOMIE***************\n")
        elif choix == 2:
            print("***************METHODE DE LA SECANTE***************\n")
        elif choix == 3:
            print("***************METHODE DE NEWTON-RAPHSON***************\n")
        elif choix == 4:
            print("***************METHODE DU POINT FIXE***************\n")

        # Demander à l'utilisateur de saisir la fonction à résoudre
        fonction_str = saisir_fonction()
        try:
            # Convertir la fonction sous forme de chaîne en une expression sympy
            fonction_expr = sympify(fonction_str)
            fonction = lambdify(x, fonction_expr, 'math')  # Transformer la fonction sympy en fonction mathématique Python
            print("Fonction interprétée : f(x) =", fonction_expr)  # Afficher la fonction interprétée
        except Exception as e:
            print(f"Erreur lors de l'interprétation de la fonction : {e}")  # Si la fonction est invalide, afficher l'erreur
            continue  # Demander à nouveau la fonction si une erreur survient

        # Si la méthode choisie nécessite des bornes (Méthode de Dichotomie ou Sécante)
        if choix in [1, 2]:  # Vérifier si le choix est 1 ou 2
            borne_inferieure, borne_superieure = demander_bornes()  # Demander les bornes
            print(f"Votre intervalle est : [{borne_inferieure}, {borne_superieure}]")  # Afficher l'intervalle choisi

        # Définir la tolérance et le nombre maximal d'itérations
        tolerance, nombre_max_iterations = saisir_tolerance_et_iterations()  # Saisie de la tolérance et des itérations

        # Exécution de la méthode choisie par l'utilisateur
        racine = None  # Initialisation de la variable racine

        if choix == 1:
            # Exécution de la méthode de la dichotomie
            racine = methode_de_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        elif choix == 2:
            # Exécution de la méthode de la sécante
            racine = methode_de_la_secante(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        elif choix == 3:
            # Exécution de la méthode de Newton-Raphson
            derivee_fonction = lambdify(x, fonction_expr.diff(x), 'math')  # Calcul de la dérivée de la fonction
            x_initiale = float(input("Entrez une estimation initiale de la racine (exemple: 2) : Xo = "))
            racine = methode_de_newton_raphson(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations)
        elif choix == 4:
            # Exécution de la méthode du point fixe
            x_initiale = float(input("Entrez une estimation initiale de la racine (exemple: 2) : Xo = "))
            racine = methode_du_point_fixe(fonction, x_initiale, tolerance, nombre_max_iterations)

        # Affichage de la racine trouvée
        if racine is not None:
            print(f"La racine trouvée est : {racine}")  # Afficher la racine si elle a été trouvée
        else:
            print("Aucune racine n'a été trouvée.")  # Si aucune racine n'a été trouvée

        # Demander à l'utilisateur s'il veut recommencer ou quitter
        choix_recommencer_Terminer = input("Souhaitez-vous recommencer ? (oui/non) : ").lower()
        if choix_recommencer_Terminer == "oui":
            action = True  # Continuer si l'utilisateur veut recommencer
        else:
            action = False  # Quitter si l'utilisateur ne veut pas recommencer

# Appel de la fonction principale pour démarrer le programme
if __name__ == "__main__":
    main()  # Lancer le programme
