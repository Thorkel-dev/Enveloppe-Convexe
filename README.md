# Enveloppe-Convexe

<p align="center">
<img  src="images\logo.jpg" alt="ESEO Logo" width="300" height="">
</p>

## Introduction
Projet Math-Info réalisé en 2020, dans le cadre des études en cycle préparatoire ingénieur.
Le but de ce programme est de calculer une enveloppe convexe à partir d’un nuage de point.
C'est à dire une envellope qui regroupe l'ensemble des points d'un nuage de point, et qui est la plus petite possible.

Réalisé avec Anaîs Gallerand, @EdouardGautier, et Antoine Orvain.
## Objectifs
Pour cela trois méthodes de calcul sont utilisées :
- Graham
- Jarvis
- Quickhull

Ces méthodes doivent pouvoir trouver l'enveloppe convexe pour n'importe quel nuage de point.
Les nuages de point sont créés de manière aléatoire.

## Lancer le programme
Vous souhaitez voir le programme fonctionner
Pour cela ouvrez dans un terminal le fichier Main.py.
Une fenêtre graphique s'ouvre :

<p align="center">
<img  src="images\Annotation 1.png" alt="Annotation 1" width="300" height="">
</p>

Un nuage de point est crée s'il n'en a aucun d'enregistré. Il est possible de les retrouver dans le répertoire ``Programmes\Nuages`` qui est crée lui aussi créé.

Il est possible de profiter de toutes les options.

### Tracé de l'enveloppe
Pour affichier les enveloppes il vous suffit de cocher les cases des méthodes qui vous intéresse. L'enveloppe apparait immédiatement après son calcul.

<p align="center">
<img  src="images\Annotation 2.png" alt="Annotation 2" width="300" height="" style="display:inline-block;">
<img  src="images\Annotation 3.png" alt="Annotation 3" width="300" height="" style="display:inline-block;">
</p>

On peut voir juste à côté de la case coché, le temps nécessaire au calcul de l'enveloppe ainsi que le nombre d'itérrations.

**Quand __plusieurs__ méthodes sont sélectionnés, les enveleppes se __supperposent__ entre elles.**

### Animations
Afin de comprendre en partie comment fonctionne les calculs de l'enveloppes, il est possible de regarder l'animations de ces calculs.
Choisiez l'animation que de la méthode que vous souhaitez.
Une nouvelle fenêtre souvre. Et il ne reste plus qu'à la lancer.

<p align="center">
<img  src="images\Annotation 4.png" alt="Annotation 4" width="300" height="" style="display:inline-block;">
<img  src="images\Annotation 5.png" alt="Annotation 5" width="300" height="" style="display:inline-block;">
</p>

### Créer un nouveau nuage

Vous avez la possibilité de créer de nouveaux nuages à tout moment.
En clikant simplement le boutons ``Nuage suivant``, un nuage est créer alèatoirement avec les paramètres de bases.
Il est possile d'un créer un celon vos paramètres. Pour cela rentrée les dans les zones de textes et cliqué sur le bouton ``Créer``.


La création de nuage est limité. Voir ci-dessous.
Paramètre | Défault | Maximum | Minimun
------------ | ------------- | ------------ | ------------- |
Hauteur | 500 | 1000 | 100
Largueur | 500 | 600 | 100
Nombre de point | 25 | Hauteur x Largeur x 500 | 0