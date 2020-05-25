# -*- coding: utf-8 -*-
import os as os  # Gestion des chemins vers les fichiers
import random as rd  # Gestion du pseudo aléatoire
import json as js  # Ecriture et récupération de liste dans les fichiers
from pathlib import Path  # Appel système des paths
import sys  # Gestion de l'interpreteur

# Chemin vers le répertoire "Nuages"
DIRECTORY = Path(__file__).parents[1] / "Nuages"
# Ajout du chemin dans la liste des imports de l'interpreteur
sys.path.append(str(Path(__file__).parents[1]))

# Import des Classes necessaires
import Main as Main

# Recuperation des valeurs par default
WIDTH_CAN_DEFAULT = Main.WIDTH_CAN_DEFAULT
HEIGT_CAN_DEFAULT = Main.HEIGT_CAN_DEFAULT
POINT_DEFAULT = Main.POINT_DEFAULT


def writing_default() -> object:
    """
    Recherche du fichier à écrire

    Returns:
        pathlib: chemin du fichier à écrire
    """
    counter = 1
    try:
        # On créer le chemin du répertoire si il n'existe pas
        os.makedirs(DIRECTORY)
    except OSError:
        # On liste l'ensemble des fichier dans le répertoire
        for entry in os.scandir(DIRECTORY):
            counter += 1
    # Création du nouveau chemin du fichier
    path = DIRECTORY / ("Nuage_" + str(counter) + ".txt")
    return path


def writing(target_point_num: int = POINT_DEFAULT,
            can_dim: tuple = (WIDTH_CAN_DEFAULT, HEIGT_CAN_DEFAULT),
            path: object = None, list_points: list = list()) -> object:
    """
    Ecriture ou modification d'un fichier avec nuage de point

    Args:
        target_point_num (int, optional): Nombre de point dans le nuage.
        Defaults to 25.
        can_dim (tuple, optional): Dimension du Canvas. Defaults to (500, 500).
        path (pathlib, optional): chemin du fichier à écrire. Defaults to None.
        list_points (list, optional): Liste des points du nuage.
        Defaults to list().

    Returns:
        pathlib: Chemin du fichier écrit
    """
    if path is None:  # Si le fichier n'existe pas
        path = writing_default()  # On le créé
        list_points = [creation_nuage(can_dim, target_point_num)]
    if len(list_points) == 0:
        list_points = [creation_nuage(can_dim, target_point_num)]
    with open(path, 'w') as file:  # On écrit le fichier
        list_points.append(can_dim)  # Ajout des dimensions du Canvas
        js.dump(list_points, file)  # On écrit toute la liste avec Json
    return path


def creation_nuage(can_dim: tuple, target_point_num: int) -> list:
    """
    Création d'un nuage de point alèatoire

    Returns:
        list: Liste des points du nuage
    """
    # Distance avec le bord du Canvas
    MARGIN_CAN_X = Main.MARGIN_CAN_X_DEFAULT
    MARGIN_CAN_Y = Main.MARGIN_CAN_Y_DEFAULT
    # Distance entre les points
    MARGIN_POINT_X = Main.MARGIN_POINT_X_DEFAULT
    MARGIN_POINT_Y = Main.MARGIN_POINT_Y_DEFAULT
    list_points = list()
    num_point = int()
    while num_point < target_point_num:
        too_close = bool()
        point_x = rd.randint(MARGIN_CAN_X, can_dim[0] - MARGIN_CAN_X)
        point_y = rd.randint(MARGIN_CAN_Y, can_dim[1] - MARGIN_CAN_Y)
        for point in list_points:
            if (abs(point[0] - point_x) <= MARGIN_POINT_X
                    and abs(point[1] - point_y) <= MARGIN_POINT_Y):
                too_close = True  # Les points sont trop proche
                break  # On passe à un autre point
        if too_close is False:
            # Ajout du point dans le nuage
            list_points.append((point_x, point_y))
            num_point += 1
    return list_points


if __name__ == "__main__":
    writing()
    print("FIN")
