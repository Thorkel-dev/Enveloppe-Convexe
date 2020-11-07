# -*- coding: utf-8 -*-
import math as mt   # Fonction mathematique


class Graham():
    """
    Methode de Graham pour trouver une enveloppe convexe
    """

    def __init__(self) -> None:
        self.envelope = list()
        self.itteration = int()

    def find_origin(self) -> list:
        """
        Recherche du point avec la plus petite ordonnee et abscisse
        """
        self.origin = [mt.inf, 0]
        min_y = mt.inf
        for point in self.cloud:
            self.itteration += 1
            if point[1] < min_y:
                min_y = point[1]
                self.origin = point
            elif point[1] == min_y:
                self.origin = min(self.origin, point, key=lambda p: p[0])
        return self.origin

    def angle(self, point: list) -> float:
        """
        Calcul de l angle entre un point et l origine

        Args:
            point (list): Point a analyser

        Returns:
            float: angle forme entre le point et l origine
        """
        # Methode de la tangente
        delta_x = point[0] - self.origin[0]
        delta_y = point[1] - self.origin[1]
        angle = mt.atan2(delta_y, delta_x)
        self.itteration += 1
        return angle

    def sorting_fusion(self, list_fusion: list) -> list:
        """
        Tri d une liste par la methode du tri fusion

        Args:
            list_fusion (list): Liste a trier

        Returns:
            list: Liste trie
        """
        self.itteration += 1
        if len(list_fusion) <= 1:
            return list_fusion
        else:
            middle = len(list_fusion)//2
            return self.fusion(
                self.sorting_fusion(list_fusion[:middle]),
                self.sorting_fusion(list_fusion[middle:]))

    def fusion(self, list_a: list, list_b: list) -> list:
        """
        Permet la fusion de deux listes triees

        Args:
            list_a (list): premiere liste
            list_b (list): deuxieme liste

        Returns:
            list: Liste triee apres fusion de list_a et list_b
        """
        num_point_a = num_point_b = int()
        len_list_a = len(list_a)
        len_list_b = len(list_b)
        list_sort = list()
        self.itteration += 1
        if len(list_a) == 0:
            return list_b
        if len(list_b) == 0:
            return list_a
        while num_point_a < len_list_a and num_point_b < len_list_b:
            # On parcourt l ensemble des listes
            self.itteration += 1
            # Le tri se fait en fonction de l angle du point et de l origine
            # dans l ordre croissant
            if self.angle(list_a[num_point_a]) < self.angle(
                    list_b[num_point_b]):
                list_sort.append(list_a[num_point_a])
                num_point_a += 1
            else:
                list_sort.append(list_b[num_point_b])
                num_point_b += 1
        list_sort = (list_sort + list_a[num_point_a:] +
                     list_b[num_point_b:])  # Fusion des listes
        return list_sort

    def vectorial_product(self, point_a: list, point_b: list, point_c: list) \
            -> bool:
        """
        Determine si un point est a gauche d un segment

        Args:
            point_a (list): Premier point du segment
            point_b (list): Deuxieme point du segment
            point_c (list): point a analyser

        Returns:
            bool: True si a gauche, False si a droite
        """
        self.itteration += 1
        # Calcul du produit vectoriel
        if (point_b[0] - point_a[0]) * (point_c[1] - point_a[1]) - \
                (point_c[0] - point_a[0]) * (point_b[1] - point_a[1]) <= 0:
            return True
        else:
            return False

    def convex_hull(self, cloud: list) -> list:
        """
        Recherche des points de l enveloppe convexe

        Args:
            cloud (list): Liste des points du nuage
        """
        self.envelope = list()
        self.itteration = int()
        self.cloud = cloud
        self.find_origin()
        self.point_sort = self.sorting_fusion(self.cloud)
        self.envelope.extend([self.point_sort[0], self.point_sort[1]]
                             )  # Ajout des points qui sont sur l enveloppe
        for point in self.point_sort[2:]:
            # On teste tous les points
            self.itteration += 1
            while (self.vectorial_product(
                    self.envelope[-2], self.envelope[-1], point) is True and
                    len(self.envelope) >= 3):
                # Le point test est plus a l exterieur que le precedent point
                self.envelope.pop()  # On retire le point en trop
                self.itteration += 1
            self.envelope.append(point)
        return self.envelope


if __name__ == "__main__":
    from pathlib import Path    # Appel système des paths
    import sys  # Gestion de l interpreteur

    # Recuperation du chemin d execution du programme
    DIRECTORY = Path(__file__).parents[1]
    # Ajout du chemin dans la liste des imports de l interpreteur
    sys.path.append(str(DIRECTORY))

    import Script.data as data

    cloud, path, a = data.data()
    G = Graham()
    G.convex_hull(cloud[0])
