# -*- coding: utf-8 -*-
import unittest
from pathlib import Path    # Appel système des paths
import sys  # Gestion de l'interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l'interpreteur
sys.path.append(str(DIRECTORY))


class test_Quickhull(unittest.TestCase):
    def setUp(self):
        import Class.Quickhull as Quickhull
        self.Q = Quickhull.Quickhull()
        self.Q.cloud = [[447, 468], [42, 455], [424, 159], [441, 215],
                        [455, 41], [312, 187], [222, 276], [197, 85],
                        [64, 249], [243, 225], [111, 228], [96, 30],
                        [118, 485], [222, 91], [77, 192], [80, 27], [63, 273],
                        [432, 139], [135, 58], [115, 260], [472, 52],
                        [111, 450], [229, 390], [286, 114], [163, 201]]

    def test_fin_origin(self):
        self.assertTupleEqual(self.Q.find_origin(),
                              ([80, 27], [118, 485]), "Mauvais origines")

    def test_position_point(self):
        self.assertTrue(self.Q.position_point([80, 27], [118, 485],
                        [42, 455]), "Le point est à gauche du segment")
        self.assertFalse(self.Q.position_point([118, 485], [80, 27],
                         [42, 455]), "Le point est à droite du segment")

    def test_distance_point(self):
        self.assertEqual(self.Q.distance_point([118, 485], [80, 27],
                         [42, 455]), 15472927.854242455,
                         "Mauvais calcul de la distance")

    def test_point_set(self):
        list_test = [[222, 91], [77, 192], [80, 27], [63, 273],
                     [432, 139], [135, 58], [115, 260], [472, 52]]
        list_right_true = [[222, 91], [432, 139],
                           [135, 58], [115, 260], [472, 52]]
        list_left_true = [[77, 192], [80, 27], [63, 273]]
        self.assertTupleEqual(self.Q.point_set(list_test, [80, 27],
                              [118, 485]), (list_left_true, list_right_true))

    def test_convex_hull(self):
        hull_true = [[42, 455], [80, 27], [455, 41],
                     [472, 52], [447, 468], [118, 485]]
        self.assertListEqual(self.Q.convex_hull(self.Q.cloud), hull_true,
                             "Mauvais calcul de l'enveloppe")


if __name__ == "__main__":
    unittest.main()
