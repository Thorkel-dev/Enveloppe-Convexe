# -*- coding: utf-8 -*-
from pathlib import Path    # Appel systeme des paths
import sys  # Gestion de l interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l interpreteur
sys.path.append(str(DIRECTORY))

# Donnees par defaut
INFORMATION = "Réalisé par:\
                \nAnaïs Gallerand,\
                \nEdouard Gautier,\
                \nAntoine Orvain\
                \nProjet Maths-Info,    \tAnnée 2020"
SYMBOLE = "X"
WIDTH_FRAME_DEFAULT = 250
WIDTH_CAN_DEFAULT = 500
HEIGT_CAN_DEFAULT = 500
POINT_DEFAULT = 25
WIDTH_CAN_MIN = 100
WIDTH_CAN_MAX = 1000
HEIGT_CAN_MIN = 100
HEIGT_CAN_MAX = 600
POINT_MIN = 0
POINT_MAX = 1200
MARGIN_CAN_X_DEFAULT = 10
MARGIN_CAN_Y_DEFAULT = 10
MARGIN_POINT_X_DEFAULT = 10
MARGIN_POINT_Y_DEFAULT = 10
COLOR_GRAHAM = "red"
COLOR_JARVIS = "blue"
COLOR_QUICHKULL = "green"

if __name__ == "__main__":
    # Import des classes necessaires
    import Class.Window as Window
    Win = Window.Window()


"""
@author = "Edouard Gautier, Anais Gallerand, et Antoine Orvain"
@copyright = "Copyright 2020, ESEO"
@credits = ["Edouard Gautier", "Anais Gallerand", "Antoine Orvain"]
@version = "2.2"
@email = "edouard_gautier@reseau.eseo.fr, anais.gallerand@reseau.eseo.fr,\
          antoine.orvain@reseau.eseo.fr"
@status = "Production"
@date = "26 mai 2020"
"""
