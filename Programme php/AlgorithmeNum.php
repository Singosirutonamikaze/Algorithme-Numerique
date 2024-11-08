<?php
// Importation des bibliothèques nécessaires
// PHP n'a pas d'équivalent direct à SymPy, donc les fonctions mathématiques seront manipulées différemment
require 'MethodeDeResolution.php';
require 'AcccueilEtMenus.php';

// Fonction principale pour gérer le menu et les choix de l'utilisateur
function main() {
    $choix_recommencer_Terminer = "";
    $action = true;

    // Appel de la fonction pour afficher le message de bienvenue
    rectangle_bienvenue_complexe();

    // Boucle principale pour permettre à l'utilisateur de recommencer ou terminer
    while ($action) {
        // Affichage du menu principal
        methode_resolution();

        // Boucle pour s'assurer que l'utilisateur entre un entier valide entre 1 et 4
        while (true) {
            $choix = readline("Entrez le numéro de la méthode (1-4) : ");
            $choix = intval($choix);

            if ($choix < 1 || $choix > 4) {
                echo "Erreur : le numéro doit être un entier compris entre 1 et 4.\n";
            } else {
                break;
            }
        }

        // Affichage du choix de l'utilisateur
        echo "Vous avez choisi la méthode numéro $choix.\n";
        switch ($choix) {
            case 1:
                echo "***************METHODE DE DICHOTOMIE***************\n";
                break;
            case 2:
                echo "***************METHODE DE LA SECANTE***************\n";
                break;
            case 3:
                echo "***************METHODE DE NEWTON-RAPHSON***************\n";
                break;
            case 4:
                echo "***************METHODE DU POINT FIXE***************\n";
                break;
        }

        // Saisie de la fonction mathématique par l'utilisateur
        $fonction_str = saisir_fonction();

        // Conversion de la chaîne de fonction en une fonction évaluable
        $fonction = create_function_from_string($fonction_str);

        // Vérifie si le choix de méthode nécessite des bornes (Méthode de la Dichotomie ou de la Sécante)
        if (in_array($choix, [1, 2])) {
            while (true) {
                $borne_inferieure = readline("Entrez la borne inférieure de l'intervalle : ");
                $borne_superieure = readline("Entrez la borne supérieure de l'intervalle : ");

                if (is_numeric($borne_inferieure) && is_numeric($borne_superieure) && $borne_inferieure < $borne_superieure) {
                    break;
                } else {
                    echo "Erreur : veuillez entrer des nombres valides pour les bornes et assurez-vous que la borne inférieure est inférieure à la borne supérieure.\n";
                }
            }
            echo "Votre intervalle est : [$borne_inferieure, $borne_superieure]\n";
        }

        // Définir la tolérance et le nombre maximal d'itérations
        while (true) {
            $tolerance = readline("Entrez la tolérance souhaitée (ex: 0.0001) : ");
            $nombre_max_iterations = readline("Entrez le nombre maximal d'itérations (ex: 100) : ");

            if (is_numeric($tolerance) && $tolerance > 0 && is_numeric($nombre_max_iterations) && $nombre_max_iterations > 0) {
                break;
            } else {
                echo "Erreur : les valeurs de tolérance et d'itérations doivent être supérieures à zéro.\n";
            }
        }
        echo "Votre tolérance est : $tolerance\n";
        echo "Votre nombre maximal d'itérations est : $nombre_max_iterations\n";

        // Exécution de la méthode choisie par l'utilisateur
        $racine = null;
        switch ($choix) {
            case 1:
                $racine = methode_de_dichotomie($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 2:
                $racine = methode_de_la_secante($fonction, $borne_inferieure, $borne_superieure, $tolerance, $nombre_max_iterations);
                break;
            case 3:
                $x_initiale = readline("Entrez une estimation initiale de la racine : ");
                $racine = methode_de_newton_raphson($fonction, $x_initiale, $tolerance, $nombre_max_iterations);
                break;
            case 4:
                $x_initiale = readline("Entrez une estimation initiale de la racine : ");
                $racine = methode_du_point_fixe($fonction, $x_initiale, $tolerance, $nombre_max_iterations);
                break;
        }

        // Affichage de la racine trouvée
        if ($racine !== null) {
            echo "La racine trouvée est : $racine\n";
        } else {
            echo "Aucune racine n'a été trouvée.\n";
        }

        // Demande à l'utilisateur s'il veut recommencer ou quitter
        $choix_recommencer_Terminer = strtolower(readline("Souhaitez-vous recommencer ? (oui/non) : "));
        $action = ($choix_recommencer_Terminer === "oui");
    }
}

// Fonction pour convertir une chaîne de caractères en une fonction exécutable
function create_function_from_string($fonction_str) {
    // Remplacer les exposants par PHP pow() et autres conversions si nécessaire
    // Par exemple : x**2 -> pow(x,2)
    $fonction_str = str_replace("**", "^", $fonction_str);
    // Retourner une fonction anonyme
    return function($x) use ($fonction_str) {
        // Evaluer l'expression
        eval('$result = ' . $fonction_str . ';');
        return $result;
    };
}

// Appel de la fonction principale
main();
