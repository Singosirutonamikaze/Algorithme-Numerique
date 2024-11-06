# Algorithme-Numerique

## Résolution Numérique - Méthodes de Recherche de Racines

Ce programme implémente plusieurs méthodes numériques pour résoudre des équations en trouvant leurs racines. Vous pouvez utiliser l'une des méthodes suivantes :

1. **Méthode de Dichotomie**
2. **Méthode de la Sécante**
3. **Méthode de Newton**
4. **Méthode du Point Fixe**

## Prérequis

Le programme nécessite **Python 3** et les bibliothèques suivantes :

- `math`
- `sympy`

Vous pouvez installer la bibliothèque `sympy` si elle n'est pas déjà installée avec la commande suivante :

pip install sympy

## Description des Méthodes

- **Méthode de Dichotomie** : Cette méthode consiste à diviser l'intervalle [a, b] en deux à chaque itération et à choisir la sous-intervallation qui contient la racine de la fonction.
  
- **Méthode de la Sécante** : Cette méthode consiste à utiliser une approximation linéaire de la fonction pour trouver la racine. Elle remplace l'évaluation de la dérivée par une différence finie.

- **Méthode de Newton** : Cette méthode repose sur l'utilisation de la dérivée de la fonction. À chaque itération, un point est calculé à partir de l'approximation actuelle en utilisant la formule de Newton.

- **Méthode du Point Fixe** : Cette méthode cherche la racine d'une fonction sous la forme `f(x) = 0` en reformulant le problème sous la forme `x = phi(x)` et en itérant à partir d'un point initial.

## Fonctionnement

1. **Lancer le programme :**
   Le programme vous permet de choisir la méthode que vous souhaitez utiliser, puis vous guide pour entrer les paramètres nécessaires (la fonction, les bornes, la tolérance, etc.).

2. **Entrée de la Fonction :**
   Vous devez entrer la fonction sous forme d'une expression mathématique, par exemple `x**2 - 2` pour trouver la racine carrée de 2.

3. **Bornes et Points Initiaux :**
   Pour certaines méthodes (comme la Dichotomie et la Sécante), vous devrez entrer les bornes de l'intervalle où vous pensez que la racine se trouve. Pour d'autres (comme la méthode de Newton et du Point Fixe), vous devrez entrer un point initial.

4. **Résultats :**
   Le programme affiche la racine estimée et vous indique si la méthode a convergé ou non.

## Exemple d'Utilisation

Voici comment lancer le programme dans un terminal ou un environnement Python interactif :

1.Exécution du programme :

python main.py

2.Sélectionnez la méthode (par exemple, **Méthode de Dichotomie**)

Choisissez la méthode de résolution :

1. La méthode de Dichotomie
2. La méthode de la Sécante
3. La méthode de Newton
4. La méthode du Point Fixe

3.Entrez une fonction, par exemple `x**2 - 2` pour trouver la racine carrée de 2.

4.Entrez les bornes (pour la méthode de Dichotomie) ou un point initial (pour Newton et Point Fixe).

5.Le programme affiche la racine approximative avec le nombre d'itérations effectuées.

## Paramètres

- **Tolérance** : La tolérance détermine la précision de la solution. Par exemple, une tolérance de `1.0e-9` signifie que le programme s'arrêtera lorsque la différence entre deux approximations successives sera inférieure à `1.0e-9`.
  
- **Nombre maximum d'itérations** : Le programme effectue un nombre d'itérations maximum pour éviter de tourner indéfiniment en cas de non-convergence. Vous pouvez ajuster ce paramètre en fonction de la précision souhaitée.

## Exemple de Calcul

Supposons que vous voulez résoudre l'équation `x^2 - 2 = 0` (chercher la racine carrée de 2). Le programme vous guidera pour entrer cette fonction, les bornes de recherche (par exemple, `[1, 2]` pour la méthode de Dichotomie), puis vous donnera la racine approximative.

### Exemple avec la méthode de Newton

Choisissez la méthode de résolution

1. La méthode de Dichotomie
2. La méthode de la Sécante
3. La méthode de Newton
4. La méthode du Point Fixe
Entrez le numéro de la méthode (1-4) : 3
Vous avez choisi la méthode numéro 3.
Entrez la fonction en termes de x (ex: x**2 - 2) : f(x) = x**2 - 2
Fonction interprétée :  x**2 - 2
Entrez le point de départ : 1.5
Entrez le nombre maximum d'itérations : 100
Entrez la tolérance (ex: 1.0e-9) : 1.0e-9
Méthode de Newton :
Résultat trouvé : 1.414213562373095

### Exemple avec la méthode de Dichotomie

Choisissez la méthode de résolution :

1. La méthode de Dichotomie
2. La méthode de la Sécante
3. La méthode de Newton
4. La méthode du Point Fixe
Entrez le numéro de la méthode (1-4) : 1
Vous avez choisi la méthode numéro 1.
Entrez la fonction en termes de x (ex: x**2 - 2) : f(x) = x**2 - 2
Fonction interprétée :  x**2 - 2
Entrez la borne inférieure de l'intervalle : 1
Entrez la borne supérieure de l'intervalle : 2
Entrez le nombre maximum d'itérations : 100
Entrez la tolérance (ex: 1.0e-9) : 1.0e-9
Méthode de Dichotomie :
Résultat trouvé : 1.414213562373095

## Conclusion

Ce programme est un excellent outil pour résoudre des équations non linéaires en utilisant différentes méthodes numériques classiques. Il offre une interface interactive pour choisir la méthode, entrer les paramètres, et obtenir rapidement une solution approximative avec des garanties de convergence.

## Contribution

Si vous souhaitez contribuer au projet, vous pouvez forker le repository et soumettre des pull requests avec de nouvelles fonctionnalités ou des améliorations.
