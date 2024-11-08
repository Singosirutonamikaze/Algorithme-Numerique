<?php
// Fonction pour la bienvenue du programme
function rectangle_bienvenue_complexe()
{
    // Definir la phrase et la largeur du rectangle
    $phrase = " BIENVENUE ";
    $largeur = strlen($phrase) + 6; // Largeur avec marges supplementaires pour le cadre
    $hauteur = 5; // Hauteur du rectangle

    //Dessiner la première ligne (double bordure d'étoiles)
    echo str_repeat('*', $largeur);

    // Ligne avec bordure interne et espace
    echo str_repeat('*', $largeur - 2) . '*';

    //Ligne du milieu avec la phrase entourée de marges et bordure interne
    echo '* ' . str_repeat(' ', $largeur - 6) . ' *';

    //ligne avec bordure interne et espace
    echo str_repeat('*', $largeur - 2) . '*';

    //Derniere ligne (double bordure d'étoiles)
    echo str_repeat('*', $largeur);
}

//Fonction permettant le choix de la methode
function methode_resolution()
{
    echo "Choisissez une methode de resolution : ";
    echo "\n";
    echo "      1. Methode de dichotomie";
    echo "\n";
    echo "      2. Methode de la secante";
    echo "\n";
    echo "      3. Methode de newton-raphson";
    echo "\n";
    echo "      4. Methode du point fixe";
    echo "\n";
}


//Fonction pour la saisie de la fonction
function saisir_fonction()
{
    //Affichage des options  de type de fonction à l'utilisateur
    echo "*******************Menus de choix de fonction *******************\n";
    echo "Choisissez le type de fonction que vous souhaitez entrer :\n";
    echo "     1. Polynème (ex: x**2 + 3*x - 8)\n";
    echo "     2. Trigonométrique (ex: sin(x), cos(x) + x)\n";
    echo "     3. Logarithmique (ex: ln(x), log(x) + x**2)\n";
    echo "     4. Racine carrée (ex: sqrt(x) + x/2)\n";
    echo "     5. Rationnelle (ex: (x + 1) / (x - 2))\n";
    echo "\n";
    //Boucle principale pour choisir le type de fonction
    while (true) {
        //Demande à l'utilisateur de saisir le numéro correspondant au type de fonction
        $type_fonction = readline("Entrez le numéro du type de fonction : ");
        //Vérification que le choix est bien un numéro entre 1 et 5
        if ($type_fonction >= 1 && $type_fonction <= 5) {
            //Message d'erreur si le choix est invalide
            echo "Choix invalide. Veuillez entrer un nombre entre 1 et 5.\n";
            continue;
        }
        //Boucle pour demander à l'utilisateur de saisir la fonction mathématique
        while (true) {
            //Demande la fonction mathématique et supprime les espaces, puis met en minuscules
            $fonction = readline("Entrez votre fonction mathématique : ");
            //Définition de l'expression régulière et du message d'erreur selon le type de fonction
            if ($type_fonction == 1) {
                $pattern = '/^[-+]?(\d+)?(x(\*\*\d+)?)?([+\-*/]?\d*(x(\*\*\d+)?)?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction polynomiale.";
            } elseif ($type_fonction == 2) {
                $pattern = '/^[-+]?(\d+)?(sin(\*\*\d+)?)?([+\-*/]?\d*(sin(\*\*\d+)?)?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction trigonometrique.";
            } elseif ($type_fonction == 3) {
                $pattern = '/^[-+]?(\d+)?(ln(\*\*\d+)?)?([+\-*/]?\d*(ln(\*\*\d+)?)?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction logarithmique.";
            } elseif ($type_fonction == 4) {
                $pattern = '/^[-+]?(\d+)?(sqrt(\*\*\d+)?)?([+\-*/]?\d*(sqrt(\*\*\d+)?)?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction racine carrée.";
            } elseif ($type_fonction == 5) {
                $pattern = '/^[-+]?(\d+)?(x(\*\*\d+)?)?([+\-*/]?\d*(x(\*\*\d+)?)?)*\/[-+]?(\d+)?(x(\*\*\d+)?)?([+\-*/]?\d*(x(\*\*\d+)?)?)*$/';
                $message = "Veuillez entrer une expression mathématique valide pour la fonction rationnelle.";
            }
            //Vérification de la validité de la fonction mathématique
            if (preg_match($pattern, $fonction)) {
                break;
            } else {
                echo $message . "\n";
                continue;
            }
        }
    }
}





































