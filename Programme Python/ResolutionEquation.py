import math
import sys
from sympy import symbols, sympify, lambdify

# Fonction pour la méthode de dichotomie
def methode_de_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations):
    # On évalue la fonction f à la borne inférieure
    valeur_borne_inferieure = fonction(borne_inferieure)

    # Si f(a) est proche de 0, a est la racine
    if (math.fabs(valeur_borne_inferieure) <= tolerance):
        return borne_inferieure

    # On évalue la fonction f à la borne supérieure
    valeur_borne_superieure = fonction(borne_superieure)

    # Si f(b) est proche de 0, b est la racine
    if (math.fabs(valeur_borne_superieure) <= tolerance):
        return borne_superieure

    # Vérifie si la fonction a une racine entre a et b
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0):
        print("La racine n'est pas encadrée entre [", borne_inferieure, ";", borne_superieure, "]")
        sys.exit(0)

    # Calcul du nombre maximum d'itérations nécessaires
    nombre_iterations = int(math.ceil(math.log(math.fabs(borne_superieure - borne_inferieure) / tolerance) / math.log(2.0)))

    # On effectue la dichotomie
    for _ in range(min(nombre_iterations + 1, nombre_max_iterations)):
        point_milieu = (borne_inferieure + borne_superieure) * 0.5  # Point milieu
        valeur_point_milieu = fonction(point_milieu)  # Valeur de f au point milieu

        # Si f(c) est proche de 0, c est la racine
        if (valeur_point_milieu == 0.0 or (borne_superieure - borne_inferieure) < tolerance):
            return point_milieu

        # Mise à jour des bornes a ou b selon le signe de f(c)
        if (valeur_point_milieu * valeur_borne_superieure < 0.0):
            borne_inferieure = point_milieu
            valeur_borne_inferieure = valeur_point_milieu
        else:
            borne_superieure = point_milieu
            valeur_borne_superieure = valeur_point_milieu

    # Retourne la moyenne des bornes a et b comme approximation de la racine
    return (borne_inferieure + borne_superieure) * 0.5


# Fonction pour la méthode de la sécante
def methode_de_la_secante(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations):
    # Évaluation de la fonction à la borne inférieure
    valeur_borne_inferieure = fonction(borne_inferieure)

    # Si f(a) est proche de 0, a est la racine
    if (math.fabs(valeur_borne_inferieure) <= tolerance):
        return borne_inferieure

    # Évaluation de la fonction à la borne supérieure
    valeur_borne_superieure = fonction(borne_superieure)

    # Si f(b) est proche de 0, b est la racine
    if (math.fabs(valeur_borne_superieure) <= tolerance):
        return borne_superieure

    # Vérification que la racine est bien encadrée
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0):
        print("La racine n'est pas encadrée entre [", borne_inferieure, ";", borne_superieure, "]")
        sys.exit(0)

    compteur_iterations = 0
    # La méthode de la sécante s'applique en itérant jusqu'à ce que la tolérance soit atteinte
    while ((math.fabs(borne_superieure - borne_inferieure) > tolerance or math.fabs(valeur_borne_superieure) > tolerance) and (compteur_iterations < nombre_max_iterations)):
        compteur_iterations += 1
        estimation = borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure)
        valeur_estimation = fonction(estimation)

        # Si f(estimation) est proche de 0, on retourne l'estimation
        if (math.fabs(valeur_estimation) <= tolerance):
            return estimation

        # Mise à jour des bornes en fonction du signe de f(estimation)
        if (valeur_estimation * valeur_borne_superieure < 0.0):
            borne_inferieure = estimation
            valeur_borne_inferieure = valeur_estimation
        else:
            borne_superieure = estimation
            valeur_borne_superieure = valeur_estimation

    # Retourne l'estimation à partir de la méthode de la sécante
    return (borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure))


# Fonction pour la méthode de Newton
def methode_de_newton(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations):
    compteur_iterations = 0
    x = x_initiale
    valeur_x = fonction(x)

    # La méthode de Newton itère jusqu'à convergence ou dépassement des itérations maximales
    while ((math.fabs(valeur_x) > tolerance) and (compteur_iterations < nombre_max_iterations)):
        valeur_derivee_x = derivee_fonction(x)

        # Si la dérivée est nulle, la méthode échoue
        if (valeur_derivee_x == 0):
            print("Dérivée nulle. Méthode de Newton échoue.")
            return None

        x = x - valeur_x / valeur_derivee_x
        valeur_x = fonction(x)
        compteur_iterations += 1

    if (compteur_iterations == nombre_max_iterations):
        print("Pas de convergence avec la méthode de Newton.")
        return None
    else:
        return x


# Fonction pour la méthode du point fixe
def methode_du_point_fixe(phi, x_initiale, tolerance, nombre_max_iterations):
    compteur_iterations = 0
    x = x_initiale

    # Itère jusqu'à ce que la différence entre x et phi(x) soit inférieure à la tolérance
    while ((math.fabs(phi(x) - x) > tolerance) and (compteur_iterations < nombre_max_iterations)):
        x = phi(x)
        compteur_iterations += 1

    # Vérification de la convergence
    if (compteur_iterations == nombre_max_iterations):
        print("Pas de convergence avec la méthode du point fixe.\n")
        return None
    else:
        return x


# Menu pour choisir la méthode et tester les fonctions
def main():
    choix_recommencer_Terminer = ""
    action = True

    # Boucle principale pour recommencer ou terminer
    while action:

        print("Choisissez la méthode de résolution :")
        print("1. La méthode de Dichotomie")
        print("2. La méthode de la Sécante")  
        print("3. La méthode de Newton")
        print("4. La méthode du Point Fixe\n")

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

        x = symbols('x')
        fonction_str = input("Entrez la fonction en termes de x (ex: x**2 - 2) : f(x) = ")

        try:
            fonction_expr = sympify(fonction_str)
            print("Fonction interprétée : f(x) = ", fonction_expr)
        except Exception as e:
            print("Il faut que fonction soit une fonction mathématique.", e)
            continue

        fonction = lambdify(x, fonction_expr, 'math')
        
        # Vérifie si le choix nécessite des bornes (Méthode de la Dichotomie ou de la Sécante)
        if (choix in [1, 2]):
            while True:
                try:
                    borne_inferieure = float(input("Entrez la borne inférieure de l'intervalle : "))
                    borne_superieure = float(input("Entrez la borne supérieure de l'intervalle : "))
                    pas = float(input("Entrez le pas de balayage : "))
                    
                    if (borne_inferieure < borne_superieure):
                        #Présentation de l'intervalle
                        print(f"Votre intervalle est : [{borne_inferieure}; {borne_superieure}]")
                        break
                    else:
                        print("Erreur : la borne inférieure doit être inférieure à la borne supérieure.")

                    # Balayage de l'intervalle
                    x = borne_inferieure
                    while (x <= borne_superieure):
                        print(f"f({x}) = {fonction(x)}")
                        x += pas

                except ValueError:
                    print("Erreur : veuillez entrer un nombre réel.")

        # Définir la tolérance et le nombre maximal d'itérations
        while True:
            try:
                tolerance = float(input("Entrez la tolérance souhaitée : "))
                nombre_max_iterations = int(input("Entrez le nombre maximal d'itérations : "))
                
                if (tolerance > 0 and nombre_max_iterations > 0):
                    break
                else:
                    print("Erreur : les valeurs de tolérance et d'itérations doivent être supérieures à zéro.")
            except ValueError:
                print("Erreur : veuillez entrer des valeurs numériques pour la tolérance et un entier pour les itérations.")
        
        # Exécution de la méthode choisie par l'utilisateur
        if (choix == 1):
            racine = methode_de_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        elif (choix == 2):
            racine = methode_de_la_secante(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations)
        elif choix == 3:
            derivee_fonction = lambdify(x, fonction_expr.diff(x), 'math')
            x_initiale = float(input("Entrez une estimation initiale de la racine : "))
            racine = methode_de_newton(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations)
        elif (choix == 4):
            phi_str = input("Entrez la fonction de point fixe (ex: sqrt(2+x)) : ")
            try:
                phi_expr = sympify(phi_str)
                phi = lambdify(x, phi_expr, 'math')
                x_initiale = float(input("Entrez une estimation initiale de la racine : "))
                racine = methode_du_point_fixe(phi, x_initiale, tolerance, nombre_max_iterations)
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

        if choix_recommencer_Terminer == "non":
            action = False

# Appel de la fonction principale
main()
