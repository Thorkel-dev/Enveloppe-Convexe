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
@pytest.mark.parametrize("origin", [[425, 308]])
@pytest.mark.parametrize("list_sort", [[[425, 308], [484, 308], [129, 484],
                                        [308, 361], [265, 315]]])
@pytest.mark.parametrize("envelope", [[[425, 308], [484, 308], [129, 484],
                                       [265, 315]]])
@pytest.mark.parametrize("angle", [2.605157195985062])
class Test_Graham():
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
        list_sort = list_sort
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


if __name__ == "__main__":
    pytest.main(["-v", "Programmes\\test\\Test_Graham.py", "--cov",
                 "--cov-report=html:Programmes\\test\\Graham Rapport"])
