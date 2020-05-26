# Enveloppe-Convexe

<p align="center">
<img  src="images\logo.jpg" alt="ESEO Logo" width="600" height="">
</p>

## Introduction
Projet Math-Info réalisé en 2020, dans le cadre des études en cycle préparatoire ingénieur.
Le but du projet est de calculer une enveloppe convexe à partir d’un nuage de point.
C'est à dire une enveloppe qui regroupe l'ensemble des points d'un nuage de point, et qui est la plus petite possible.

Réalisé avec Anaîs Gallerand, @EdouardGautier, et Antoine Orvain.

## Objectifs
Pour cela trois méthodes de calcul sont utilisées :
- Graham
- Jarvis
- Quickhull

Ces méthodes doivent pouvoir trouver l'enveloppe convexe pour n'importe quel nuage de point.
Les nuages de point doivent être créés de manière aléatoire.

## Lancer le programme

Pour cela ouvrez dans un terminal le fichier ``Main.py``.
Une fenêtre graphique s'ouvre :

<p align="center">
<img  src="images\Annotation 1.png" alt="Annotation 1" width="600" height="">
</p>

Un nuage de point est crée s'il n'en a aucun d'enregistré. Il est possible de les retrouver dans le répertoire ``Programmes\Nuages`` qui est lui aussi créé.

Il est possible de profiter de toutes les options.

### Tracé de l'enveloppe
Pour affichier les enveloppes il vous suffit de cocher les cases des méthodes qui vous intéresse. L'enveloppe apparait immédiatement après son calcul.

<p align="center">
<img  src="images\Annotation 2.png" alt="Annotation 2" width="600" height="" style="display:inline-block;">
<img  src="images\Annotation 3.png" alt="Annotation 3" width="600" height="" style="display:inline-block;">
</p>

On peut voir juste à côté de la case coché, le temps nécessaire au calcul de l'enveloppe ainsi que le nombre d'itérrations.

**Quand _plusieurs_ méthodes sont sélectionnés, les enveleppes se _supperposent_ entre elles.**

### Animations
Afin de comprendre en partie comment fonctionne les calculs de l'enveloppes, il est possible de regarder l'animations de ces calculs.
Choisiez l'animation de la méthode que vous souhaitez.
Une nouvelle fenêtre souvre. Et il ne reste plus qu'à la lancer.

<p align="center">
<img  src="images\Annotation 4.png" alt="Annotation 4" width="600" height="" style="display:inline-block;">
<img  src="images\Annotation 5.png" alt="Annotation 5" width="600" height="" style="display:inline-block;">
</p>

### Créer un nouveau nuage

Vous avez la possibilité de créer de nouveaux nuages à tout moment.
En clickant simplement le boutons ``Nuage suivant``, un nuage est créer alèatoirement avec les paramètres par défaut.
Il est possile d'un créer un celon vos paramètres. Pour cela rentré les dans les zones de textes et cliqué sur le bouton ``Créer``.

<p align="center">
<img  src="images\Annotation 6.png" alt="Annotation 6" width="600" height="" style="display:inline-block;">
</p>

La création de nuage est limité. Voir ci-dessous.
Paramètre | Défault | Maximum | Minimun
------------ | ------------- | ------------ | ------------- |
Hauteur | 500 | 1000 | 100
Largueur | 500 | 600 | 100
Nombre de point | 25 | Hauteur x Largeur x 500 | 0

Dés la création d'un nouveau nuage, les enveloppes convexes sont recalculer pour les méthodes qui sont sélectionnées.

### Ajouter ou retirer un point

Il est possible de retirer un point du nuage. Pour cela un click gauche de la souris, à l'endroit voulu dans le canvas, fait apparaitre un nouveau point.

Pour retirer un point, faite un click droit dessus.

Dès l'ajout ou la suppression d'un point, l'enveloppe convexe est recalculé pour les méthodes qui sont sélectionnées.