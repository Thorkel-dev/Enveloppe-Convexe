# -*- coding: utf-8 -*-
import math as mt


class Quickhull():
    """
    Methode de Quickhull pour trouver une enveloppe convexe
    """

    def __init__(self) -> None:
        self.envelope = list()
        self.itteration = int()

    def find_origin(self) -> (list, list):
        """
        Recherche du point avec la plus petite ordonnee et abscise et du point
        avec la plus grande ordonnee et abscisse
        """
        self.origin_min = [mt.inf, 0]
        self.origin_max = [0, 0]
        min_y = mt.inf
        max_y = int()
        for point in self.cloud:
            self.itteration += 1
            if point[1] < min_y:
                min_y = point[1]
                self.origin_min = point
            elif point[1] == min_y:
                self.origin_min = min(
                    self.origin_min, point, key=lambda p: p[0])
            if point[1] > max_y:
                max_y = point[1]
                self.origin_max = point
            elif point[1] == max_y:
                self.origin_max = max(
                    self.origin_max, point, key=lambda p: p[0])
        return self.origin_min, self.origin_max

    def position_point(self, point_a: list, point_b: list, point_c: list) \
            -> bool:
        """
        Donne la posistion d un point par rapport a un segment

        Args:
            point_a (list): Premier point du segment
            point_b (list): Deuxieme point du segment
            point_c (list): Point da analyser

        Returns:
            bool: True si a gauche, False si a droite
        """
        self.itteration += 1
        # Calcul du produit vectoriel
        position = (point_b[0] - point_a[0]) * (point_c[1] - point_a[1]) - \
            (point_b[1] - point_a[1]) * (point_c[0] - point_a[0])
        if position >= 0:
            return True  # Est a gauche
        else:
            return False  # Est a droite

    def distance_point(self, point_a: list, point_b: list, point_c: list) \
            -> float:
        """
        Donne la distance entre un point et un segment

        Args:
            point_a (list): Premier point du segment
            point_b (list): Deuxieme point du segment
            point_c (list): Point da analyser

        Returns:
            float: distance entre le point et le segment
        """
        self.itteration += 1
        # Produit vectoriel divise par la longeur du segment
        distance = (abs((point_b[0] - point_a[0]) * (point_c[1] - point_a[1]) -
                        (point_b[1] - point_a[1]) * (point_c[0] - point_a[0]))
                    * mt.sqrt((point_a[0] - point_b[0]) ** 2 +
                    (point_a[1] - point_b[1]) ** 2))
        return distance

    def point_set(self, list_point: list, point_a: list, point_b: list) \
            -> (list, list):
        """
        Analyse de la position d un ensemble de point par rapport a un segment

        Args:
            list_point (list): Ensemble de point
            point_a (list): Premier point du segment
            point_b (list): Deuxieme point du segment

        Returns:
            list: Point a gauche du segment
            list: Point a droite du segment
        """
        list_point_right = list()
        list_point_left = list()
        for point in list_point:
            self.itteration += 1
            # Si le pointest a gauche
            if self.position_point(point_a, point_b, point) is True:
                list_point_left.append(point)
            else:  # Si le point est a droite
                list_point_right.append(point)
        return list_point_left, list_point_right

    def convex_hull(self, cloud: list) -> list:
        """
        Recherche des points de l enveloppe convexe

        Args:
            cloud (list): Liste des points du nuage de points
        """
        self.envelope = list()
        self.itteration = int()
        self.cloud = cloud
        # Lancement de la recherche de l'enveloppe convexe
        self.list_point = self.cloud.copy()
        self.find_origin()
        self.list_point.remove(self.origin_min)
        self.list_point.remove(self.origin_max)
        self.envelope.extend([self.origin_min, self.origin_max])
        list_point_left, list_point_right = self.point_set(
            self.list_point, self.origin_min, self.origin_max)
        self.find_hull(list_point_right, self.origin_min, self.origin_max)
        self.find_hull(list_point_left, self.origin_max, self.origin_min)
        return self.envelope

    def find_hull(self, list_point: list, point_a: list, point_b: list) \
            -> None:
        """
        Recherche le prochain point de l enveloppe a parti d un ensemble de
        points et un segment

        Args:
            list_point (list): Ensemble de point
            point_a (list): Premier point du segment
            point_b (list): Deuxieme point du segment
        """
        self.itteration += 1
        distance_max = int()
        if len(list_point) == 0:
            return
        # Recherche du point le plus eloigne du segement
        for point in list_point:
            self.itteration += 1
            distance = self.distance_point(point_a, point_b, point)
            if distance >= distance_max:
                distance_max = distance
                point_c = point
        list_point.remove(point_c)
        # On reorganise la liste de point de l enveloppe pour un bon affichage
        if self.position_point(point_a, point_b, point_c) is True:
            # Si a gauche
            self.envelope.append(point_c)  # A la suite
        else:
            index_b = self.envelope.index(
                point_b, 0, len(self.envelope))  # Si a droite
            self.envelope.insert(index_b, point_c)  # Entre le point A et B
        # Recherche des sous ensemble par rapport au nouveau segment
        list_point_left, list_point_right = self.point_set(
            list_point, point_a, point_c)
        self.find_hull(list_point_right, point_a, point_c)
        list_point_left, list_point_right = self.point_set(
            list_point, point_c, point_b)
        self.find_hull(list_point_right, point_c, point_b)


if __name__ == "__main__":
    from pathlib import Path    # Appel système des paths
    import sys  # Gestion de l'interpreteur

    # Recuperation du chemin du programme
    DIRECTORY = Path(__file__).parents[1]
    # Ajout du chemin dans la liste des imports de l'interpreteur
    sys.path.append(str(DIRECTORY))

    import Script.data as data

    cloud, path, a = data.data()
    Q = Quickhull()
    Q.convex_hull(cloud[0])
    print(Q.envelope, len(Q.envelope), Q.itteration)
    print("FIN")
