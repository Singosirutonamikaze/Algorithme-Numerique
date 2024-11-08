<?php
    // Fonction pour la bienvenue du programme
    function rectangle_bienvenue_complexe() {
        // Definir la phrase et la largeur du rectangle
        $phrase = " BIENVENUE ";
        $largeur = strlen($phrase) + 6; // Largeur avec marges supplementaires pour le cadre
        $hauteur = 5; // Hauteur du rectangle

        //Dessiner la première ligne (double bordure d'étoiles)
        echo str_repeat('*', $largeur);

        // Ligne avec bordure interne et espace
        echo str_repeat('*', $largeur - 2) . '*';

        //ligne avec bordure interne et espace
        echo '* ' . str_repeat(' ', $largeur - 6) . ' *';

        //
    }








































