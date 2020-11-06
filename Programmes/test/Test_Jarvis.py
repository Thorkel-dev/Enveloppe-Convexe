# -*- coding: utf-8 -*-
import pytest   # Bibiliotheque de test unitaire
from pathlib import Path    # Appel systeme des paths
import sys  # Gestion de l interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l interpreteur
sys.path.append(str(DIRECTORY))


@pytest.mark.parametrize(
    "cloud, origin, envelope",
    [([[129, 484], [265, 315], [484, 308], [308, 361], [425, 308]],  # cloud
      [425, 308],   # origin
      [[425, 308], [265, 315], [129, 484], [484, 308]]),    # envelope
     ([[299, 269], [78, 121], [294, 452], [197, 425], [440, 310]],
      [78, 121],
      [[78, 121], [197, 425], [294, 452], [440, 310], [78, 121]]),
     ([[419, 480], [177, 398], [273, 407], [145, 309], [20, 444]],
      [145, 309],
      [[145, 309], [20, 444], [419, 480], [145, 309]]),
     ([[41, 272], [156, 310], [341, 218], [488, 278], [348, 444], [447, 471],
       [330, 308], [52, 467], [229, 176], [194, 77], [313, 215], [287, 432],
       [285, 296], [299, 54], [465, 160], [314, 292], [75, 311], [11, 109],
       [253, 412], [428, 95], [235, 203], [271, 296], [164, 140], [309, 244],
       [218, 409]],
      [299, 54],
      [[299, 54], [11, 109], [52, 467], [447, 471], [488, 278], [465, 160],
       [428, 95], [299, 54]])])
class Test_Jarvis():

    def setup_method(self, method):
        """
        On recréer la classe pour eviter toute interaction entre les tests
        """
        import Class.Jarvis as Jarvis
        self.J = Jarvis.Jarvis()

    def test_origin(self, cloud, origin, envelope):
        """
        Test de la recherche de l origine
        """
        self.J.cloud = cloud
        assert self.J.find_origin() == origin

    def test_distance(self, cloud, origin, envelope):
        """
        Test du calcul de la distance
        """
        assert self.J.distance([80, 27], [472, 52], [118, 485]) == [472, 52]
        assert self.J.distance([80, 27], [42, 52], [11, 4]) == [80, 27]

    def test_convex_hull(self, cloud, origin, envelope):
        """
        Test global de la recherche de l'enveloppe convexe
        """
        self.J.cloud = cloud
        self.J.origin = origin
        assert self.J.convex_hull(self.J.cloud) == envelope
