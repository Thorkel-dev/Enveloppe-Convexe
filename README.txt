# Envelope-Convex

## Introduction ✏
Math-Info project carried out in 2020, as part of studies in the engineering 
preparatory cycle.
The aim of the project is to calculate a convex envelope from a point cloud.
That is to say, an envelope which groups together all the points of a cloud of 
points, and which is as small as possible.

All scripts are written in UTF-8, the docstring and comments are in UTF-8
comply with the standard PEP 484(https://www.python.org/dev/peps/pep-0484/) as 
follows than the standard for Docstrings 
Google(http://google.github.io/styleguide/pyguide.html).

The ``performances.py`` program only works if the openpyxl
(https://openpyxl.readthedocs.io/en/stable/) library is installed.


## Objectives ✔
Three calculation methods are used for this purpose:
- Graham
- Jarvis
- Quickhull

These methods must be able to find the convex envelope for any point cloud.
Point clouds should be created randomly.

## Start the program 🏁

To do this, open the ``Main.py`` file in a terminal.
A graphical window opens :

A point cloud is created if there is no point cloud registered. They can be 
found in the "Programs" folder, which is also created. 

Any clouds that are created later will be saved in this directory.
All cloud files are saved under the name: ``Nuage_*.txt``.

It is possible to take advantage of all the options.

### Envelope trace
To view the envelopes, simply check the boxes for the methods you are 
interested in. The envelope appears immediately after it has been calculated.

You can see right next to the ticked box, the time needed to calculate the 
envelope and the number of iterations.

When _several_ methods are selected, the envelopes _superimpose_ on each other.

### Animations
In order to understand in part how the envelope calculations work, it is 
possible to watch the animation of these calculations.
Choose the animation of the method you want.
A new window will open. All that remains is to launch it.

### Create a new cloud
You can create new clouds at any time.
By simply clicking on the ``Nuage suivant``, a cloud is created randomly with 
the default settings.
It is possible to create one according to your settings. To do so, enter them 
in the text boxes and click on the ``Créer`` button.

Cloud creation is limited. See below.
Parameter           | Default | Maximum              | Minimun
Height              | 500     | 1000                 | 100
Width               | 500     | 600                  | 100
Number of stitches  | 25      | Height x Width x 500 | 0

As soon as a new cloud is created, the convex envelopes are recalculated for 
the methods that are selected.

### Add or remove a point
It is possible to remove a point from the cloud. To do this, a left click of 
the mouse at the desired place in the canvas will bring up a new point.

To remove a point, right click on it.

As soon as a point is added or removed, the convex envelopes are recalculated
for the methods that are selected.

### Limits ⚠
The code is in French 🇫🇷.
