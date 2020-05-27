# -*- coding: utf-8 -*-
import unittest
from pathlib import Path    # Appel systeme des paths
import sys  # Gestion de l interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l interpreteur
sys.path.append(str(DIRECTORY))


class test_Jarvis(unittest.TestCase):

    def setUp(self):
        """
        On recréer la classe pour eviter toute interaction entre les tests
        """
        import Class.Jarvis as Jarvis
        self.J = Jarvis.Jarvis()
        self.J.cloud = [[447, 468], [42, 455], [424, 159], [441, 215],
                        [455, 41], [312, 187], [222, 276], [197, 85],
                        [64, 249], [243, 225], [111, 228], [96, 30],
                        [118, 485], [222, 91], [77, 192], [80, 27], [63, 273],
                        [432, 139], [135, 58], [115, 260], [472, 52],
                        [111, 450], [229, 390], [286, 114], [163, 201]]

    def test_origin(self):
        """
        Test de la recherche de l origine 
        """
        self.assertListEqual(self.J.find_origin(), [80, 27],
                             "Mauvaise origine")

    def test_distance(self):
        """
        Test du calcul de la distance
        """
        self.assertEqual(self.J.distance([80, 27], [472, 52], [118, 485]),
                         [472, 52], "Ne retourne pas le point B")
        self.assertEqual(self.J.distance([80, 27], [42, 52], [11, 4]),
                         [80, 27], "Ne retourne pas le point A")

    def test_convex_hull(self):
        """
        Test global de la recherche de l'enveloppe convexe
        """
        hull_true = [[80, 27], [42, 455], [118, 485],
                     [447, 468], [472, 52], [455, 41], [80, 27]]
        self.assertListEqual(self.J.convex_hull(self.J.cloud), hull_true,
                             "Mauvais calcul de l'enveloppe")


if __name__ == "__main__":
    unittest.main()
