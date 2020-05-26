# -*- coding: utf-8 -*-
import math as mt   # Methode mathematique


class Jarvis():
    """
    Methode de Jarvis pour trouver une enveloppe convexe
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
        self.envelope.append(self.origin)
        return self.origin

    def distance(self, point_a: list, point_b: list, point_c: list) -> list:
        """
        Calcule la distance de deux points par rapport a un troisieme point

        Args:
            point_a (list): Premier point
            point_b (list): Deuxieme point
            point_c (list): Point de reference

        Returns:
            list: Le point le plus eloigne
        """
        self.itteration += 1
        distA = (point_a[0] - point_c[0]) ** 2 + (point_a[1] - point_c[1]) ** 2
        distB = (point_b[0] - point_c[0]) ** 2 + (point_b[1] - point_c[1]) ** 2
        if distA > distB:
            return point_a
        else:
            return point_b

    def find_next_point(self, previous_point_1: list, previous_point_2: list) \
            -> None:
        """
        Recherche les points de l enveloppe convexe

        Args:
            previous_point_1 (list): Dernier point ajoute a l enveloppe
            previous_point_2 (list): Avant dernier point ajoute a l enveloppe

        Returns:
            list: Ensemble des points de l enveloppe convexe
        """
        self.itteration += 1
        if previous_point_1 == self.origin and len(self.envelope) >= 3:
            # Si le dernier point est l origine alors on a fait le tour de
            # l enveloppe
            return
        min_angle = mt.inf
        previous_delta_x = previous_point_1[0] - previous_point_2[0]
        previous_delta_y = previous_point_1[1] - previous_point_2[1]
        previous_angle = mt.atan2(previous_delta_y, previous_delta_x)
        for point in self.list_points:
            self.itteration += 1
            next_delta_x = point[0] - previous_point_1[0]
            next_delta_y = point[1] - previous_point_1[1]
            next_angle = mt.atan2(next_delta_y, next_delta_x)
            # Recherche du point qui fait le plus petit angle
            if abs(next_angle - previous_angle) <= min_angle:
                self.itteration += 1
                if previous_angle != next_angle:  # Si les points ne sont pas
                    # alignes
                    min_angle = abs(next_angle - previous_angle)
                    next_point = point
                else:
                    next_point = self.distance(
                        point, previous_point_1, previous_point_2)
                    self.envelope[-1] = next_point
        # Si le point est aligne en ordonnee par rapport a l origine
        if next_point[1] == self.origin[1]:
            self.envelope.append(next_point)
            return  # On a fait le tour
        else:
            self.list_points.remove(next_point)
            self.envelope.append(next_point)
            # Recherche du point suivant
            return self.find_next_point(self.envelope[-1], self.envelope[-2])

    def convex_hull(self, cloud: list) -> list:
        """
        Recherche des points de l enveloppe convexe

        Args:
            cloud (list): Liste des points du nuage
        """
        self.envelope = list()
        self.itteration = int()
        self.cloud = cloud
        self.list_points = self.cloud.copy()
        self.find_origin()
        self.find_next_point(
            self.origin, [self.origin[0] + mt.inf, self.origin[1]])
        return self.envelope


if __name__ == "__main__":
    from pathlib import Path    # Appel systeme des paths
    import sys  # Gestion de l interpreteur

    # Recuperation du chemin du programme
    DIRECTORY = Path(__file__).parents[1]
    # Ajout du chemin dans la liste des imports de l interpreteur
    sys.path.append(str(DIRECTORY))

    import Script.data as data

    cloud, path, a = data.data()
    J = Jarvis()
    J.convex_hull(cloud[0])
    print(J.envelope, len(J.envelope), J.itteration)
    print("FIN")
