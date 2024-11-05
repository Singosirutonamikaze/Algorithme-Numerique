import math
import sys
from sympy import symbols, sympify, lambdify

# Fonction pour la méthode de dichotomie
def methode_dichotomie(fonction, borne_inferieure, borne_superieure, tolerence, nombre_max_iterations):
    # On évalue la fonction f à la borne inférieure
    valeur_borne_inferieure = fonction(borne_inferieure)
    # Si f(a) est proche de 0, a est la racine
    if (math.fabs(valeur_borne_inferieure) <= tolerence):
        return borne_inferieure
    
    # On évalue la fonction f à la borne supérieure
    valeur_borne_superieure = fonction(borne_superieure)
    # Si f(b) est proche de 0, b est la racine
    if (math.fabs(valeur_borne_superieure) <= tolerence):
        return borne_superieure
    
    # On vérifie que la fonction a une racine entre a et b
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0):
        print("La racine n'est pas encadrée entre", borne_inferieure, "et", borne_superieure)
        sys.exit(0)

    # On calcule le nombre maximum d'itérations nécessaires
    nombre_iterations = int(math.ceil(math.log(math.fabs(borne_superieure - borne_inferieure) / tolerence) / math.log(2.0)))

    # On effectue la dichotomie
    for _ in range(min(nombre_iterations + 1, nombre_max_iterations)):
        point_milieu = (borne_inferieure + borne_superieure) * 0.5  # Point milieu

        valeur_point_milieu = fonction(point_milieu)  # Valeur de f au point milieu
        # Si f(c) est proche de 0, c est la racine
        if (valeur_point_milieu == 0.0 or (borne_superieure - borne_inferieure) < tolerence):
            return point_milieu
        
        # On met à jour les bornes a ou b selon le signe de f(c)
        if (valeur_point_milieu * valeur_borne_superieure < 0.0):
            borne_inferieure = point_milieu
            valeur_borne_inferieure = valeur_point_milieu
        else:
            borne_superieure = point_milieu
            valeur_borne_superieure = valeur_point_milieu
    # Retourne la moyenne des bornes a et b comme approximation de la racine
    return (borne_inferieure + borne_superieure) * 0.5


# Fonction pour la méthode de Lagrange
def methode_lagrange(fonction, borne_inferieure, borne_superieure, tolerence, nombre_max_iterations):
    valeur_borne_inferieure = fonction(borne_inferieure)
    if (math.fabs(valeur_borne_inferieure) <= tolerence):
        return borne_inferieure
    
    valeur_borne_superieure = fonction(borne_superieure)
    if (math.fabs(valeur_borne_superieure) <= tolerence):
        return borne_superieure
    
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0):
        print("La racine n'est pas encadrée entre", borne_inferieure, "et", borne_superieure)
        sys.exit(0)
    
    compteur_iterations = 0
    while ((math.fabs(borne_superieure - borne_inferieure) > tolerence or math.fabs(valeur_borne_superieure) > tolerence) and (compteur_iterations < nombre_max_iterations)):
        compteur_iterations += 1
        estimation = borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure)
        valeur_estimation = fonction(estimation)
        
        if (math.fabs(valeur_estimation) <= tolerence):
            return estimation
        
        if (valeur_estimation * valeur_borne_superieure < 0.0):
            borne_inferieure = estimation
            valeur_borne_inferieure = valeur_estimation
        else:
            borne_superieure = estimation
            valeur_borne_superieure = valeur_estimation
    
    return (borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure))


# Fonction pour la méthode de Newton
def methode_newton(fonction, derivee_fonction, x_initiale, tolerence, nombre_max_iterations):
    compteur_iterations = 0
    x = x_initiale
    valeur_x = fonction(x)
    
    while ((math.fabs(valeur_x) > tolerence) and (compteur_iterations < nombre_max_iterations)):
        valeur_derivee_x = derivee_fonction(x)
        
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


# Fonction pour la méthode de point fixe
def methode_point_fixe(phi, x_initiale, tolerence, nombre_max_iterations):
    compteur_iterations = 0
    x = x_initiale
    
    while ((math.fabs(phi(x) - x) > tolerence) and (compteur_iterations < nombre_max_iterations)):
        x = phi(x)
        compteur_iterations += 1
    
    if (compteur_iterations == nombre_max_iterations):
        print("Pas de convergence avec la méthode de point fixe.")
        return None
    else:
        return x



# Menu pour choisir la méthode et tester les fonctions

def main():
    
    #Variable
    choix_recommencer_Terminer = ""
    action = bool

    action = True
    while (action) :

        print("Choisissez la méthode de résolution :")
        print("1. La méthode de Dichotomie")
        print("2. La méthode de la Sécante")  
        print("3. La méthode de Newton")
        print("4. La méthode du Point Fixe")

        # Boucle pour s'assurer que l'utilisateur saisit un entier valide entre 1 et 4
        while True:
            try:
                choix = int(input("Entrez le numéro de la méthode (1-4) : "))
                if (choix < 1 or choix > 4):
                    print("Erreur : le numéro doit être un entier compris entre 1 et 4.")
                else:
                    break  # Sortir de la boucle si le choix est valide
            except ValueError:
                print("Erreur : veuillez entrer un nombre entier.")

        # Affichage du choix de l'utilisateur
        print(f"Vous avez choisi la méthode numéro {choix}.")

        x = symbols('x')
        fonction_str = input("Entrez la fonction en termes de x (ex: x**2 - 2) : f(x) = ")

        try:
            fonction_expr = sympify(fonction_str)
            print("Fonction interprétée : ", fonction_expr)
        except Exception as e:
            print("Erreur dans l'entrée de la fonction : ", e)
            return

        fonction = lambdify(x, fonction_expr, 'math')
        
        if choix in [1, 2]:  # Vérifie si la méthode choisie nécessite des bornes
            while True:
                try:
                    borne_inferieure = float(input("Entrez la borne inférieure de l'intervalle : "))
                    borne_superieure = float(input("Entrez la borne supérieure de l'intervalle : "))
                    
                    # Vérification que la borne inférieure est inférieure à la borne supérieure
                    if (borne_inferieure < borne_superieure):
                        print("Votre intervalle est : [", borne_inferieure, ";", borne_superieure, "].")
                        break  # Sortie de la boucle si la condition est satisfaite
                    else:
                        print("Erreur : La borne inférieure doit être inférieure à la borne supérieure. Veuillez réessayer.")
                
                except ValueError:
                    print("Erreur : Veuillez entrer des nombres valides pour les bornes.")

        elif (choix == 3):
            x_initiale = float(input("Entrez le point de départ : "))
            derivee_expr = fonction_expr.diff(x)
            derivee_fonction = lambdify(x, derivee_expr, 'math')
        elif (choix == 4):
            phi_str = input("Entrez la fonction de point fixe phi(x) : ")
            try:
                phi_expr = sympify(phi_str)
                phi = lambdify(x, phi_expr, 'math')
            except Exception as e:
                print("Erreur dans l'entrée de la fonction phi(x) : ", e)
                return
            x_initiale = float(input("Entrez le point de départ (Le point initial) : "))
        else:
            print("Choix non valide")
            return

        nombre_max_iterations = int(input("Entrez le nombre maximum d'itérations : "))
        tolerence = float(input("Entrez la tolérance (ex: 1.0e-9) : "))

        if (choix == 1):
            print("Méthode de dichotomie :")
            resultat = methode_dichotomie(fonction, borne_inferieure, borne_superieure, tolerence, nombre_max_iterations)
        elif (choix == 2):
            print("Méthode de Lagrange :")
            resultat = methode_lagrange(fonction, borne_inferieure, borne_superieure, tolerence, nombre_max_iterations)
        elif (choix == 3):
            print("Méthode de Newton :")
            resultat = methode_newton(fonction, derivee_fonction, x_initiale, tolerence, nombre_max_iterations)
        elif (choix == 4):
            print("Méthode de point fixe :")
            resultat = methode_point_fixe(phi, x_initiale, tolerence, nombre_max_iterations)

        print("Résultat trouvé :", resultat)

        choix_recommencer_Terminer = str(input("Voulez-vous recommencer la résolution (oui/non) : ")).lower()

        if(choix_recommencer_Terminer  == "oui"):
            action = True
        else:
            action = False


if (__name__ == "__main__"):
    main()
