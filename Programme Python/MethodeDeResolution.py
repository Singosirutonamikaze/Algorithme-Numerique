# Importation des modules
import math
import sys

#  Fonction pour la méthode de dichotomie avec affichage des intervalles
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
    for i in range(min(nombre_iterations + 1, nombre_max_iterations)):
        point_milieu = (borne_inferieure + borne_superieure) * 0.5  # Point milieu
        valeur_point_milieu = fonction(point_milieu)  # Valeur de f au point milieu

        # Affichage de l'intervalle actuel
        print(f"Iteration {i + 1}: Intervalle actuel = [{borne_inferieure}, {borne_superieure}]")

        # Si f(c) est proche de 0, c est la racine
        if (valeur_point_milieu == 0.0 or (borne_superieure - borne_inferieure) < tolerance):
            print(f"Solution trouvée : x = {point_milieu} après {i + 1} itérations")
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
def methode_de_newton_raphson(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations):
    compteur_iterations = 0
    x = x_initiale
    valeur_x = fonction(x)

    # La méthode de Newton itère jusqu'à convergence ou dépassement des itérations maximales
    while ((math.fabs(valeur_x) > tolerance) and (compteur_iterations < nombre_max_iterations)):
        valeur_derivee_x = derivee_fonction(x)

        # Si la dérivée est nulle, la méthode échoue
        if (valeur_derivee_x == 0):
            print("La dérivée nulle.L'impléméntation de la Méthode de Newton échoue.")
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


