# Enveloppe-Convexe

<p align="center">
<img  src="images\logo.jpg" alt="ESEO Logo" width="400" height="">
</p>

## Introduction
Projet Math-Info réalisé en 2020, dans le cadre des études en cycle préparatoire ingénieur.
Le but du projet est de calculer une enveloppe convexe à partir d’un nuage de points.
C'est à dire une enveloppe qui regroupe l'ensemble des points d'un nuage de points, et qui est la plus petite possible.

L'ensemble des scripts est rédigé en UTF-8, la docstring et les commentaires
respectent la norme [_PEP 484_](https://www.python.org/dev/peps/pep-0484/) ainsi
que la norme pour les Docstrings [_Google_](http://google.github.io/styleguide/pyguide.html).

Le programme ``performances.py`` ne fonctionne que si la bibliothèque [_openpyxl_](https://openpyxl.readthedocs.io/en/stable/) est instalée.


## Objectifs
Pour cela trois méthodes de calcul sont utilisées :
- Graham
- Jarvis
- Quickhull

Ces méthodes doivent pouvoir trouver l'enveloppe convexe pour n'importe quel nuage de points.
Les nuages de points doivent être créés de manière aléatoire.

## Lancer le programme

Pour cela ouvrez dans un terminal le fichier ``Main.py``.
Une fenêtre graphique s'ouvre :

<p align="center">
<img  src="images\Annotation 1.png" alt="Annotation 1" width="400" height="">
</p>

Un nuage de points est créé s'il n'y en a aucun d'enregistré. Il est possible de les retrouver dans le répertoire ``Programmes\Nuages`` qui est lui aussi créé. 

*Tous les nuages qui viendront à être créés par la suite seront enregistrés dans ce répertoire.
Tous les fichiers nuages sont enregistrés sous le nom: ``Nuage_*.txt``.*

Il est possible de profiter de toutes les options.

### Tracé de l'enveloppe
Pour afficher les enveloppes, il vous suffit de cocher les cases des méthodes qui vous intéressent. L'enveloppe apparait immédiatement après son calcul.

<p align="center">
<img  src="images\Annotation 2.png" alt="Annotation 2" width="400" height="" style="display:inline-block;">
<img  src="images\Annotation 3.png" alt="Annotation 3" width="400" height="" style="display:inline-block;">
</p>

On peut voir juste à côté de la case cochée, le temps nécessaire au calcul de l'enveloppe ainsi que le nombre d'itérations.

**Quand _plusieurs_ méthodes sont sélectionnées, les enveloppes se _superposent_ entre elles.**

### Animations
Afin de comprendre en partie comment fonctionnent les calculs de l'enveloppe, il est possible de regarder l'animation de ces calculs.
Choisissez l'animation de la méthode que vous souhaitez.
Une nouvelle fenêtre s'ouvre. Et il ne reste plus qu'à la lancer.

<p align="center">
<img  src="images\Annotation 4.png" alt="Annotation 4" width="400" height="" style="display:inline-block;">
<img  src="images\Annotation 5.png" alt="Annotation 5" width="400" height="" style="display:inline-block;">
</p>

### Créer un nouveau nuage
Vous avez la possibilité de créer de nouveaux nuages à tout moment.
En cliquant simplement sur le bouton ``Nuage suivant``, un nuage est créé aléatoirement avec les paramètres par défaut.
Il est possible d'un créer un selon vos paramètres. Pour cela rentrez les dans les zones de texte et cliquez sur le bouton ``Créer``.

<p align="center">
<img  src="images\Annotation 6.png" alt="Annotation 6" width="400" height="" style="display:inline-block;">
</p>

La création de nuage est limitée. Voir ci-dessous.
Paramètre | Default | Maximum | Minimun
------------ | ------------- | ------------ | ------------- |
Hauteur | 500 | 1000 | 100
Largueur | 500 | 600 | 100
Nombre de points | 25 | Hauteur x Largeur x 500 | 0

**Dès la création d'un nouveau nuage, les enveloppes convexes sont _recalculées_ pour les méthodes qui sont _sélectionnées_.**

### Ajouter ou retirer un point

Il est possible de retirer un point du nuage. Pour cela un clique gauche de la souris, à l'endroit voulu dans le canvas, fait apparaitre un nouveau point.

Pour retirer un point, faite un clique droit dessus.

**Dès l'ajout ou la suppression d'un point, les enveloppes convexes sont _recalculées_ pour les méthodes qui sont _sélectionnées_.**
