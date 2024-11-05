#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <locale.h>

#define TOLERANCE 1e-9 // Définition d'une constante pour la tolérance

// Prototypes de fonctions
double fonction(double x);
double derivee_fonction(double x);
double methode_dichotomie(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerance, int nombre_max_iterations);
double methode_lagrange(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerance, int nombre_max_iterations);
double methode_newton(double (*fonction)(double), double (*derivee_fonction)(double), double x_initiale, double tolerance, int nombre_max_iterations);
double methode_point_fixe(double (*phi)(double), double x_initiale, double tolerance, int nombre_max_iterations);
double phi(double x); // Exemple pour la méthode de point fixe

int main() {
    setlocale(LC_CTYPE, "");

    int choix;
    double borne_inferieure, borne_superieure, x_initiale, tolerance;
    int nombre_max_iterations;

    // Affichage des options de méthodes
    printf("Choisissez la méthode de résolution en saisissant juste le chiffre:\n");
    printf("1. La méthode de Dichotomie\n");
    printf("2. La méthode de Lagrange\n");
    printf("3. La méthode de Newton\n");
    printf("4. La méthode du Point Fixe\n");
    printf("La méthode choisie est (1-4) : ");
    scanf("%d", &choix);

    // Lecture des bornes ou du point de départ selon la méthode choisie
    if (choix == 1 || choix == 2) {
        printf("Entrez la borne inférieure de l'intervalle : ");
        scanf("%lf", &borne_inferieure);
        printf("Entrez la borne supérieure de l'intervalle : ");
        scanf("%lf", &borne_superieure);
    } else if (choix == 3 || choix == 4) {
        printf("Entrez le point de départ : ");
        scanf("%lf", &x_initiale);
    } else {
        printf("Choix non valide\n");
        return 1; // Sortie en cas de choix non valide
    }

    // Lecture du nombre maximum d'itérations et de la tolérance
    printf("Entrez le nombre maximum d'itérations : ");
    scanf("%d", &nombre_max_iterations);
    printf("Entrez la tolérance : ");
    scanf("%lf", &tolerance);

    double resultat;

    // Appel de la méthode choisie
    switch (choix) {
        case 1:
            resultat = methode_dichotomie(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations);
            break;
        case 2:
            resultat = methode_lagrange(fonction, borne_inferieure, borne_superieure, tolerance, nombre_max_iterations);
            break;
        case 3:
            resultat = methode_newton(fonction, derivee_fonction, x_initiale, tolerance, nombre_max_iterations);
            break;
        case 4:
            resultat = methode_point_fixe(phi, x_initiale, tolerance, nombre_max_iterations);
            break;
        default:
            printf("Choix non valide\n");
            return 1;
    }

    // Affichage du résultat
    printf("Résultat trouvé : %lf\n", resultat);
    return 0;
}

// Fonction exemple f(x) = x^2 - 2
double fonction(double x) {
    return x * x - 2;
}

// Dérivée de la fonction exemple
double derivee_fonction(double x) {
    return 2 * x;
}

// Méthode de Dichotomie
double methode_dichotomie(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerance, int nombre_max_iterations) {
    double valeur_borne_inferieure = fonction(borne_inferieure);
    double valeur_borne_superieure = fonction(borne_superieure);

    // Vérification des valeurs aux bornes
    if (fabs(valeur_borne_inferieure) <= tolerance) {
        return borne_inferieure;
    }
    if (fabs(valeur_borne_superieure) <= tolerance) {
        return borne_superieure;
    }
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0) {
        fprintf(stderr, "Erreur : La racine n'est pas encadrée entre %.2f et %.2f\n", borne_inferieure, borne_superieure);
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < nombre_max_iterations; i++) {
        double point_milieu = (borne_inferieure + borne_superieure) / 2;
        double valeur_point_milieu = fonction(point_milieu);

        // Vérification de la convergence
        if (fabs(valeur_point_milieu) <= tolerance || (borne_superieure - borne_inferieure) < tolerance) {
            return point_milieu;
        }

        // Mise à jour des bornes
        if (valeur_point_milieu * valeur_borne_superieure < 0.0) {
            borne_inferieure = point_milieu;
            valeur_borne_inferieure = valeur_point_milieu;
        } else {
            borne_superieure = point_milieu;
            valeur_borne_superieure = valeur_point_milieu;
        }
    }

    return (borne_inferieure + borne_superieure) / 2; // Retourne le milieu si pas encore convergé
}

// Méthode de Lagrange
double methode_lagrange(double (*fonction)(double), double borne_inferieure, double borne_superieure, double tolerance, int nombre_max_iterations) {
    double valeur_borne_inferieure = fonction(borne_inferieure);
    double valeur_borne_superieure = fonction(borne_superieure);

    // Vérification des valeurs aux bornes
    if (fabs(valeur_borne_inferieure) <= tolerance) {
        return borne_inferieure;
    }
    if (fabs(valeur_borne_superieure) <= tolerance) {
        return borne_superieure;
    }
    if (valeur_borne_inferieure * valeur_borne_superieure > 0.0) {
        fprintf(stderr, "Erreur : La racine n'est pas encadrée entre %.2f et %.2f\n", borne_inferieure, borne_superieure);
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < nombre_max_iterations; i++) {
        // Estimation de la nouvelle valeur
        double estimation = borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure);
        double valeur_estimation = fonction(estimation);

        // Vérification de la convergence
        if (fabs(valeur_estimation) <= tolerance) {
            return estimation;
        }

        // Mise à jour des bornes
        if (valeur_estimation * valeur_borne_superieure < 0.0) {
            borne_inferieure = estimation;
            valeur_borne_inferieure = valeur_estimation;
        } else {
            borne_superieure = estimation;
            valeur_borne_superieure = valeur_estimation;
        }
    }

    return borne_inferieure - valeur_borne_inferieure * (borne_superieure - borne_inferieure) / (valeur_borne_superieure - valeur_borne_inferieure);
}

// Méthode de Newton
double methode_newton(double (*fonction)(double), double (*derivee_fonction)(double), double x_initiale, double tolerance, int nombre_max_iterations) {
    double x = x_initiale;
    double valeur_x = fonction(x);

    for (int i = 0; i < nombre_max_iterations; i++) {
        double valeur_derivee_x = derivee_fonction(x);

        // Vérification de la dérivée nulle
        if (valeur_derivee_x == 0) {
            fprintf(stderr, "Erreur : Dérivée nulle. Méthode de Newton échoue.\n");
            return NAN;
        }

        // Mise à jour de la valeur
        x = x - valeur_x / valeur_derivee_x;
        valeur_x = fonction(x);

        // Vérification de la convergence
        if (fabs(valeur_x) <= tolerance) {
            return x;
        }
    }

    fprintf(stderr, "Erreur : Pas de convergence avec la méthode de Newton.\n");
    return NAN;
}

// Méthode du Point Fixe
double phi(double x) {
    return sqrt(2); // Exemple pour phi(x) = sqrt(2)
}

double methode_point_fixe(double (*phi)(double), double x_initiale, double tolerance, int nombre_max_iterations) {
    double x = x_initiale;

    for (int i = 0; i < nombre_max_iterations; i++) {
        double x_nouveau = phi(x);

        // Vérification de la convergence
        if (fabs(x_nouveau - x) <= tolerance) {
            return x_nouveau;
        }

        x = x_nouveau; // Mise à jour de x pour la prochaine itération
    }

    fprintf(stderr, "Erreur : Pas de convergence avec la méthode de point fixe.\n");
    return NAN;
}
