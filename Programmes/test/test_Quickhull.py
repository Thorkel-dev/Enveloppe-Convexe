# -*- coding: utf-8 -*-
import pytest   # Bibiliotheque de test unitaire
from pathlib import Path    # Appel systeme des paths
import sys  # Gestion de l interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l interpreteur
sys.path.append(str(DIRECTORY))


@pytest.mark.parametrize("cloud", [[[129, 484], [265, 315], [484, 308],
                                    [308, 361], [425, 308]]])
@pytest.mark.parametrize("origin_min, origin_max", [([425, 308], [129, 484])])
@pytest.mark.parametrize("envelope", [[[265, 315], [425, 308], [484, 308],
                                       [129, 484]]])
@pytest.mark.parametrize("list_left, list_right", [([[129, 484], [265, 315],
                                                    [308, 361], [425, 308]],
                                                    [[484, 308]])])
class Test_Quickhull():

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
    pytest.main(["-v", "Programmes\\test\\Test_Quickhull.py", "--cov",
                 "--cov-report=html:Programmes\\test\\Quickhull Rapport"])
