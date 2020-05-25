# -*- coding: utf-8 -*-
import unittest
from pathlib import Path    # Appel système des paths
import sys  # Gestion de l'interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l'interpreteur
sys.path.append(str(DIRECTORY))


class test_Graham(unittest.TestCase):

    def setUp(self):
        import Class.Graham as Graham
        self.G = Graham.Graham()
        self.G.cloud = [[447, 468], [42, 455], [424, 159], [441, 215],
                        [455, 41], [312, 187], [222, 276], [197, 85],
                        [64, 249], [243, 225], [111, 228], [96, 30],
                        [118, 485], [222, 91], [77, 192], [80, 27], [63, 273],
                        [432, 139], [135, 58], [115, 260], [472, 52],
                        [111, 450], [229, 390], [286, 114], [163, 201]]
    def test_origin(self):
        self.assertListEqual(self.G.find_origin(), [80, 27],
                             "Mauvaise origine")

    def test_sorting_fusion(self):
        list_true = [[80, 27], [455, 41], [472, 52], [96, 30], [432, 139],
                     [424, 159], [286, 114], [222, 91], [197, 85], [441, 215],
                     [135, 58], [312, 187], [447, 468], [243, 225], [222, 276],
                     [163, 201], [229, 390], [111, 228], [115, 260],
                     [118, 485], [111, 450], [77, 192], [63, 273],
                     [64, 249], [42, 455]]
        self.G.origin = [80, 27]
        list_tets = self.G.sorting_fusion(self.G.cloud)
        self.assertListEqual(list_tets, list_true, "Trie de liste faux")

    def test_angle(self):
        self.G.origin = [80, 27]
        self.assertEqual(self.G.angle([42, 455]), 1.6593491796085054,
                         "Erreur de calcul d'angle")

    def test_vectorial_product(self):
        self.assertTrue(self.G.vectorial_product(
            [472, 52], [96, 30], [432, 139]), "Le point C est à gauche de AB")
        self.assertFalse(self.G.vectorial_product(
            [80, 27], [455, 41], [472, 52]), "Le point C est à droite de AB")

    def test_fusion(self):
        self.G.origin = [80, 27]
        list_a_test = [[229, 390], [111, 450]]
        list_b_test = [[286, 114], [163, 201]]
        list_fusion_true = [[286, 114], [163, 201], [229, 390], [111, 450]]
        self.assertListEqual(self.G.fusion(list_a_test, list_b_test),
                             list_fusion_true, "Mauvaise fusion des listes")
        self.assertListEqual(self.G.fusion([], list_b_test), list_b_test,
                             "Doit renvoyer la liste B")
        self.assertListEqual(self.G.fusion(list_a_test, []), list_a_test,
                             "Doit renvoyer la liste A")
        self.assertListEqual(self.G.fusion([], []), [],
                             "Doit renvoyer une liste vide")

    def test_convex_hull(self):
        hull_true = [[80, 27], [455, 41], [472, 52],
                     [447, 468], [118, 485], [42, 455]]
        self.assertListEqual(self.G.convex_hull(self.G.cloud), hull_true,
                             "Mauvais calcul de l'enveloppe")


if __name__ == "__main__":
    unittest.main()
