# -*- coding: utf-8 -*-
import tkinter as tk
from pathlib import Path    # Appel système des paths
import sys  # Gestion de l'interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l'interpreteur
sys.path.append(str(DIRECTORY))

# Import des Classes necessaires
import Class.Quickhull as Quickhull
import Main as main

# Recuperation des valeurs par default
SYMBOLE = main.SYMBOLE
WIDTH_CAN_DEFAULT = main.WIDTH_CAN_DEFAULT
HEIGT_CAN_DEFAULT = main.HEIGT_CAN_DEFAULT
COLOR_QUICHKULL = main.COLOR_QUICHKULL

class QuickhullAnimation(tk.Tk, Quickhull.Quickhull):
    """
    Fenetre pour afficher l animation de Quickhull
    """

    def __init__(self) -> None:
        # Heritage des classes
        Quickhull.Quickhull.__init__(self)

    def win_creat(self, cloud, width=500, heigh=500) -> None:
        """
        Creation de l interface graphique

        Args:
            cloud (list): Liste des point du nuage de point
            width (int, optional): Largeur du Canvas. Defaults to 500.
            heigh (int, optional): Hauteur du Canvas. Defaults to 500.
        """
        tk.Tk.__init__(self)
        self.cloud = cloud
        self.can_dim = [width, heigh]
        self.title("Quickhull")
        self.geometry("-0+85")
        # Canvas principal avec le nuage de points
        self.can = tk.Canvas(
            self, width=self.can_dim[0], heigh=self.can_dim[1], bg="white")
        self.can.pack(side=tk.RIGHT)

        # Frame principal
        frm = tk.Frame(self, heigh=self.can_dim[1])
        frm.pack(side=tk.RIGHT)

        # Label indiquant les etapes de realises
        self.text_label = tk.Label(frm, text="", wraplength=100)
        self.text_label.pack(side=tk.BOTTOM)

        # Bouton pour demarer l animation
        self.start_button = tk.Button(
            frm, text='Start', command=self.animation,  width=15)
        self.start_button.pack(side=tk.TOP)

        # Affichage des points du nuage
        for point in self.cloud:
            self.can.tag_raise(self.can.create_text(
                point, text=SYMBOLE, tag="Point", fill='black'))

        self.resizable(width=False, height=False)
        self.mainloop()

    def animation(self) -> None:
        """
        Initialise l animation et permet son demarage
        """
        global counter, distance_max
        global list_point
        self.start_button['state'] = tk.DISABLED
        self.envelope_anim = list()
        counter = distance_max = int()
        self.list_point = self.cloud.copy()
        self.find_origin()
        self.list_point.remove(self.origin_min)
        self.list_point.remove(self.origin_max)
        self.envelope_anim.extend([self.origin_min, self.origin_max])
        # On s assure qu il n y a rien
        self.can.delete("envelope_anim_convexe",
                        "point_convexe", "point_origin")
        # Element de base
        self.can.create_line(
            0, 0, self.can_dim[0], 0, tag=("abscisse_min"), cap="round")
        self.can.create_line(
            0, 0, 0, self.can_dim[1], tag=("ordonnee_min"), cap="round")
        self.can.create_line(
            0, 0, self.can_dim[0], 0, tag=("abscisse_max"), cap="round")
        self.can.create_line(
            0, 0, 0, self.can_dim[1], tag=("ordonnee_max"), cap="round")
        # On lance le debut
        self.find_origin_animation()

    def find_origin_animation(self) -> None:
        """
        Animation de la recherche du point avec la plus petite ordonnee et
        abscise
        """
        self.text_label["text"] = "Recherche des origines"
        coord_absc_min = self.can.coords("abscisse_min")
        coord_ord_min = self.can.coords("ordonnee_min")
        coord_absc_max = self.can.coords("abscisse_max")
        coord_ord_max = self.can.coords("ordonnee_max")
        # On deplace jusqu a etre a l origine
        if coord_absc_min[1] < self.origin_min[1]:
            self.can.move("abscisse_min", 0, 1)
            self.can.after(1, self.find_origin_animation)    # On recommence
        elif coord_ord_min[0] < self.origin_min[0]:
            self.can.move("ordonnee_min", 1, 0)
            self.can.after(1, self.find_origin_animation)  # On recommence
        elif coord_absc_max[1] < self.origin_max[1]:
            self.can.move("abscisse_max", 0, 1)
            self.can.after(1, self.find_origin_animation)    # On recommence
        elif coord_ord_max[0] < self.origin_max[0]:
            self.can.move("ordonnee_max", 1, 0)
            self.can.after(1, self.find_origin_animation)  # On recommence
        else:  # On affiche un rectagle sur les origines
            self.can.create_rectangle(self.origin_min[0] - 5,
                                      self.origin_min[1] - 5,
                                      self.origin_min[0] + 5,
                                      self.origin_min[1] + 5,
                                      fill=COLOR_QUICHKULL,
                                      tag="point_origin")
            self.can.create_rectangle(self.origin_max[0] - 5,
                                      self.origin_max[1] - 5,
                                      self.origin_max[0] + 5,
                                      self.origin_max[1] + 5,
                                      fill=COLOR_QUICHKULL,
                                      tag="point_origin")
            self.can.create_line(self.origin_min, self.origin_max,
                                 fill=COLOR_QUICHKULL,
                                 tag="envelope_anim_convexe")
            self.can.delete("abscisse_min", "ordonnee_min",
                            "abscisse_max", "ordonnee_max")
            list_point_left, list_point_right = self.point_set(
                self.list_point, self.origin_min, self.origin_max)
            # On lance l animation pour les autres points
            self.find_next_point_animation(
                list_point_right, self.origin_min, self.origin_max)
            self.find_next_point_animation(
                list_point_left, self.origin_max, self.origin_min)

    def find_next_point_animation(self, list_point: list, point_a: list,
                                  point_b: list, point_c: list = list(),
                                  counter: int = int(),
                                  distance_max: int = int()) -> None:
        """
        Animation de la recherhce des points de l enveloppe convexe

        Args:
            list_point (list): Liste des points de l ensemble de point a
            analyser
            point_a (list): Premier point du segment
            point_b (list): Deuxieme point du segment
            point_c (list, optional): Troisieme point que l on recherchce.
            Defaults to list().
            counter (int, optional): compteur pour parcourir list_point.
            Defaults to int().
            distance_max (int, optional): plus grande distance entre le segment
            et un point. Defaults to int().
        """
        self.text_label["text"] = "Recherche des autres points"
        if len(list_point) == 0:
            # Fin de la recherche
            self.text_label["text"] = "Enveloppe convexe complète"
            self.start_button['state'] = tk.NORMAL
            return
        if counter < len(list_point):
            # Recherche du point le plus elogner du segement
            point = list_point[counter]
            distance = self.distance_point(point_a, point_b, point)
            self.can.delete("point_anim_right", "envelope_anim_anim_right")
            self.can.create_polygon(point, point_a, point_b, fill="",
                                    outline="red",
                                    tag=("envelope_anim_anim_right"))
            self.can.create_oval(point[0] - 5, point[1] - 5, point[0] + 5,
                                 point[1] + 5, fill="red",
                                 tag="point_anim_right")
            if distance >= distance_max:
                distance_max = distance
                point_c = point
            counter += 1
            self.can.after(100, self.find_next_point_animation, list_point,
                           point_a, point_b, point_c, counter, distance_max)
        else:
            list_point.remove(point_c)
            # On reorganise la liste de point de l enveloppe pour un bon
            # affichage
            if self.position_point(point_a, point_b, point_c) is True:
                # Si a gauche
                self.envelope_anim.append(point_c)  # A la suite
            else:
                index_b = self.envelope_anim.index(
                    point_b, 0, len(self.envelope_anim))  # Si a droite
                # Entre le point A et B
                self.envelope_anim.insert(index_b, point_c)
            # On redessine l enveloppe
            self.can.delete("envelope_anim_convexe",
                            "point_anim_right", "envelope_anim_anim_right")
            self.can.create_oval(point_c[0] - 5, point_c[1] - 5,
                                 point_c[0] + 5, point_c[1] + 5,
                                 fill=COLOR_QUICHKULL,
                                 tag="point_convexe")
            self.can.create_polygon(self.envelope_anim, fill="",
                                    outline=COLOR_QUICHKULL,
                                    tag=("envelope_anim_convexe"))
            # On recommence les recherches
            list_point_left, list_point_right = self.point_set(
                list_point, point_a, point_c)
            self.can.after(1000, self.find_next_point_animation,
                           list_point_right, point_a, point_c)
            list_point_left, list_point_right = self.point_set(
                list_point, point_c, point_b)
            self.can.after(1000, self.find_next_point_animation,
                           list_point_right, point_c, point_b)


if __name__ == "__main__":
    import Script.data as data

    data, path, a = data.data()
    Win = QuickhullAnimation()
    Win.win_creat(data[0])
    print("FIN")
