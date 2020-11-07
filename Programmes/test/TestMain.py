# -*- coding: utf-8 -*-
import pytest   # Bibiliotheque de test unitaire
from pathlib import Path    # Appel systeme des paths
import sys  # Gestion de l interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l interpreteur
sys.path.append(str(DIRECTORY))


@pytest.mark.parametrize(
    "cloud, origin, list_sort, envelope, angle",
    [([[129, 484], [265, 315], [484, 308], [308, 361], [425, 308]],  # cloud
      [425, 308],   # origin
      # list_sort
      [[425, 308], [484, 308], [129, 484], [308, 361], [265, 315]],
      [[425, 308], [484, 308], [129, 484], [265, 315]],  # envelope
      2.605157195985062),  # angle
     ([[299, 269], [78, 121], [294, 452], [197, 425], [440, 310]],
      [78, 121],
      [[78, 121], [440, 310], [299, 269], [294, 452], [197, 425]],
      [[78, 121], [440, 310], [294, 452], [197, 425]],
      0.5900881062591957),
     ([[419, 480], [177, 398], [273, 407], [145, 309], [20, 444]],
      [145, 309],
      [[145, 309], [419, 480], [273, 407], [177, 398], [20, 444]],
      [[145, 309], [419, 480], [20, 444]],
      0.5579429321099642),
     ([[41, 272], [156, 310], [341, 218], [488, 278], [348, 444],
       [447, 471], [330, 308], [52, 467], [229, 176], [194, 77], [313, 215],
       [287, 432], [285, 296], [299, 54], [465, 160], [314, 292], [75, 311],
       [11, 109], [253, 412], [428, 95], [235, 203], [271, 296], [164, 140],
       [309, 244], [218, 409]],
      [299, 54],
      [[299, 54], [428, 95], [465, 160], [488, 278], [447, 471], [341, 218],
       [348, 444], [330, 308], [313, 215], [314, 292], [309, 244], [287, 432],
       [285, 296], [271, 296], [253, 412], [218, 409], [235, 203], [156, 310],
       [229, 176], [52, 467], [75, 311], [41, 272], [164, 140], [194, 77],
       [11, 109]],
      [[299, 54], [428, 95], [465, 160], [488, 278], [447, 471], [52, 467],
       [11, 109]],
      2.4400311322607595)])
class TestGraham():
    """
    Test de l ensemble des fonctions de la classe Graham
    """

    def setup_method(self, method):
        """
        On recréer la classe pour eviter toute interaction entre les tests
        """
        import Class.Graham as Graham
        self.G = Graham.Graham()

    def test_origin(self, cloud, origin, angle, list_sort, envelope):
        """
        Test de la recherche de l origine
        """
        self.G.cloud = cloud
        assert self.G.find_origin() == origin

    def test_sorting_fusion(self, cloud, origin, list_sort, angle, envelope):
        """
        Test de a methode de tri fusion
        """
        self.G.cloud = cloud
        self.G.origin = origin
        list_tets = self.G.sorting_fusion(self.G.cloud)
        assert list_tets == list_sort

    def test_angle(self, cloud, origin, list_sort, angle, envelope):
        """
        Test du calcul de l angle
        """
        self.G.cloud = cloud
        self.G.origin = origin
        assert self.G.angle(cloud[0]) == angle

    def test_convex_hull(self, cloud, origin, list_sort, angle, envelope):
        """
        Test global de la recherche de l'enveloppe convexe
        """
        assert self.G.convex_hull(cloud) == envelope


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
class TestJarvis():

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


@pytest.mark.parametrize(
    "cloud, origin_min, origin_max, envelope, list_left, list_right",
    [([[129, 484], [265, 315], [484, 308], [308, 361], [425, 308]],  # cloud
      [425, 308],   # origin_min
      [129, 484],   # origin_max
      [[265, 315], [425, 308], [484, 308], [129, 484]],  # envelope
      [[129, 484], [265, 315], [308, 361], [425, 308]],  # list_left
      [[484, 308]]),    # list_right
     ([[299, 269], [78, 121], [294, 452], [197, 425], [440, 310]],
      [78, 121],
      [294, 452],
      [[197, 425], [78, 121], [440, 310], [294, 452]],
      [[78, 121], [294, 452], [197, 425]],
      [[299, 269], [440, 310]]),
     ([[419, 480], [177, 398], [273, 407], [145, 309], [20, 444]],
      [145, 309],
      [419, 480],
      [[20, 444], [145, 309], [419, 480]],
      [[419, 480], [177, 398], [273, 407], [145, 309], [20, 444]],
      []),
     ([[41, 272], [156, 310], [341, 218], [488, 278], [348, 444], [447, 471],
       [330, 308], [52, 467], [229, 176], [194, 77], [313, 215], [287, 432],
       [285, 296], [299, 54], [465, 160], [314, 292], [75, 311], [11, 109],
       [253, 412], [428, 95], [235, 203], [271, 296], [164, 140], [309, 244],
       [218, 409]],
      [299, 54],
      [447, 471],
      [[52, 467], [11, 109], [299, 54], [428, 95], [465, 160], [488, 278],
       [447, 471]],
      [[41, 272], [156, 310], [341, 218], [348, 444], [447, 471], [330, 308],
       [52, 467], [229, 176], [194, 77], [313, 215], [287, 432], [285, 296],
       [299, 54], [314, 292], [75, 311], [11, 109], [253, 412], [235, 203],
       [271, 296], [164, 140], [309, 244], [218, 409]],
      [[488, 278], [465, 160], [428, 95]])])
class TestQuickhull():

    def setup_method(self, method):
        """
        On recréer la classe pour eviter toute interaction entre les tests
        """
        import Class.Quickhull as Quickhull
        self.Q = Quickhull.Quickhull()

    def test_fin_origin(self, cloud, origin_min, origin_max, envelope,
                        list_right, list_left):
        """
        Test de la recherche de l origine
        """
        self.Q.cloud = cloud
        assert self.Q.find_origin() == (origin_min, origin_max)

    def test_position_point(self, cloud, origin_min, origin_max, envelope,
                            list_right, list_left):
        """
        Test de la position du point par rapport a un segment
        """
        assert self.Q.position_point([80, 27], [118, 485], [42, 455]) is True
        assert self.Q.position_point([118, 485], [80, 27], [42, 455]) is False

    def test_distance_point(self, cloud, origin_min, origin_max, envelope,
                            list_right, list_left):
        """
        Test du calcul de la distance entre un point et un segment
        """
        assert self.Q.distance_point([118, 485], [80, 27], [
                                     42, 455]) == 15472927.854242455

    def test_point_set(self, cloud, origin_min, origin_max, envelope,
                       list_right, list_left):
        """
        Test du calcul de la position des points par rapport a un segment
        """
        assert self.Q.point_set(cloud, origin_min, origin_max) == (
            list_left, list_right)

    def test_convex_hull(self, cloud, origin_min, origin_max, envelope,
                         list_right, list_left):
        """
        Test global de la recherche de l'enveloppe convexe
        """
        self.Q.cloud = cloud
        assert self.Q.convex_hull(self.Q.cloud) == envelope


if __name__ == "__main__":
    pytest.main(["-r chars", "Programmes\\test\\TestMain.py", "--cov",
                 "--cov-report=html:Programmes\\test\\Main Rapport"])
