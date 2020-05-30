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
@pytest.mark.parametrize("envelope", [[[425, 308], [265, 315], [129, 484],
                                       [484, 308]]])
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


if __name__ == "__main__":
    pytest.main(["-v", "Programmes\\test\\Test_Jarvis.py", "--cov",
                 "--cov-report=html:Programmes\\test\\Jarvis Rapport"])
