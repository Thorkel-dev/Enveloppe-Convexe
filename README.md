# Envelope-Convex
<img src="https://img.shields.io/static/v1?style=flat&message=Python&logo=python&labelColor=FFD43B&color=FFD43B&logoColor=306998&label=%20"/> [![Codacy Badge](https://app.codacy.com/project/badge/Grade/d97a33e38cee4df8ba83c959b00b048d)](https://www.codacy.com/gh/EdouardGautier/Enveloppe-Convexe/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=EdouardGautier/Enveloppe-Convexe&amp;utm_campaign=Badge_Grade)[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/d97a33e38cee4df8ba83c959b00b048d)](https://www.codacy.com/gh/EdouardGautier/Enveloppe-Convexe/dashboard?utm_source=github.com&utm_medium=referral&utm_content=EdouardGautier/Enveloppe-Convexe&utm_campaign=Badge_Coverage) <img src="https://img.shields.io/github/v/tag/Edouardgautier/Enveloppe-Convexe"/> <img src="https://img.shields.io/github/last-commit/Edouardgautier/Enveloppe-Convexe"/>

<p align="center">
<img  src="images\logo.jpg" alt="ESEO Logo" width="400" height="">
</p>
<p align=center>
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=EdouardGautier&repo=Enveloppe-Convexe&theme=default_repocard&show_icons=true"/>
</p>

## Introduction ✏️
Math-Info project carried out in 2020, as part of studies in the engineering preparatory cycle.
The aim of the project is to calculate a convex envelope from a point cloud.
That is to say, an envelope which groups together all the points of a cloud of points, and which is as small as possible.

All scripts are written in UTF-8, the docstring and comments are in UTF-8
comply with the standard [_PEP 484_](https://www.python.org/dev/peps/pep-0484/) as follows
than the standard for Docstrings [_Google_](http://google.github.io/styleguide/pyguide.html).

The ``performances.py`` program only works if the [_openpyxl_](https://openpyxl.readthedocs.io/en/stable/) library is installed.


## Objectives ✔️
Three calculation methods are used for this purpose:
- Graham
- Jarvis
- Quickhull

These methods must be able to find the convex envelope for any point cloud.
Point clouds should be created randomly.

## Start the program 🏁

To do this, open the ``Main.py`` file in a terminal.
A graphical window opens :

<p align="center">
<img  src="images\Annotation 1.png" alt="Annotation 1" width="400" height="">
</p>

A point cloud is created if there is no point cloud registered. They can be found in the "Programs" folder, which is also created. 

*Any clouds that are created later will be saved in this directory.
All cloud files are saved under the name: ``Nuage_*.txt``.*

It is possible to take advantage of all the options.

### Envelope trace
To view the envelopes, simply check the boxes for the methods you are interested in. The envelope appears immediately after it has been calculated.

<p align="center">
<img  src="images\Annotation 2.png" alt="Annotation 2" width="400" height="" style="display:inline-block;">
<img  src="images\Annotation 3.png" alt="Annotation 3" width="400" height="" style="display:inline-block;">
</p>

You can see right next to the ticked box, the time needed to calculate the envelope and the number of iterations.

**When _several_ methods are selected, the envelopes _superimpose_ on each other.**

### Animations
In order to understand in part how the envelope calculations work, it is possible to watch the animation of these calculations.
Choose the animation of the method you want.
A new window will open. All that remains is to launch it.

<p align="center">
<img  src="images\Annotation 4.png" alt="Annotation 4" width="400" height="" style="display:inline-block;">
<img  src="images\Annotation 5.png" alt="Annotation 5" width="400" height="" style="display:inline-block;">
</p>

### Create a new cloud
You can create new clouds at any time.
By simply clicking on the ``Nuage suivant``, a cloud is created randomly with the default settings.
It is possible to create one according to your settings. To do so, enter them in the text boxes and click on the ``Créer`` button.

<p align="center">
<img  src="images\Annotation 6.png" alt="Annotation 6" width="400" height="" style="display:inline-block;">
</p>

Cloud creation is limited. See below.
Parameter | Default | Maximum | Minimun
------------ | ------------- | ------------ | ------------- |
Height | 500 | 1000 | 100
Width | 500 | 600 | 100
Number of stitches | 25 | Height x Width x 500 | 0

**As soon as a new cloud is created, the convex envelopes are _recalculated_ for the methods that are _selected_.**

### Add or remove a point
It is possible to remove a point from the cloud. To do this, a left click of the mouse at the desired place in the canvas will bring up a new point.

To remove a point, right click on it.

**As soon as a point is added or removed, the convex envelopes are _recalculated_ for the methods that are _selected_.**

### Limits ⚠️
The code is in French 🇫🇷.
