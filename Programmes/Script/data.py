# -*- coding: utf-8 -*-
import os as os  # Gestion des chemins vers les fichiers
import json as js   # Ecriture et recuperation de liste dans les fichiers
from pathlib import Path    # Appel systeme des paths
import sys  # Gestion de l interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l interpreteur
sys.path.append(str(DIRECTORY))

# Import des scripts necessaires
import Script.cloud_of_points as clouds


def data(num_cloud: int = int(), path: object = None) -> (list, object, str):
    """
    Recuperation des donnees dans les fichiers nuages de points

    Args:
        num_cloud (int, optional): Numero du nuage voulu. Defaults to 0.
        path (pathlib, optional): Chemin vers le fichier nuage.
        Defaults to None.

    Returns:
        list: Ensemble des donnees
        pathlib: Chemin du fichier lu
        str: Nom du fichier lu
    """
    list_data = list()
    # Liste des fichiers dans le repertoire
    try:
        # Liste des fichiers dans le repertoire
        liste_file = os.listdir(str(DIRECTORY) + "/Nuages")
    except FileNotFoundError:
        # Creation du repertoire
        os.mkdir(str(DIRECTORY) + "/Nuages")
        liste_file = os.listdir(str(DIRECTORY) + "/Nuages")
    if path is None:
        try:  # Si le chemin existe
            path = str(DIRECTORY) + "/Nuages/" + liste_file[num_cloud]
        except IndexError:  # Sinon on le cree
            path = clouds.writing()
    with open(path, "r") as file:
        list_data = js.load(file)  # Chargement de la liste des points du nuage
    file_name = os.path.basename(path)  # Recuperation du nom du fichier
    return list_data, path, file_name


if __name__ == "__main__":
    data()
    print("FIN")
