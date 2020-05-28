# -*- coding: utf-8 -*-
import tkinter as tk
from pathlib import Path    # Appel systeme des paths
import sys  # Gestion de l interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l interpreteur
sys.path.append(str(DIRECTORY))

# Import des classes necessaires
import Class.Graham as Graham
import Main as main

# Recuperation des valeurs par defaut
SYMBOLE = main.SYMBOLE
WIDTH_CAN_DEFAULT = main.WIDTH_CAN_DEFAULT
HEIGT_CAN_DEFAULT = main.HEIGT_CAN_DEFAULT
COLOR_GRAHAM = main.COLOR_GRAHAM


class GrahamAnimation(tk.Tk, Graham.Graham):
    """
    Fenetre pour afficher l animation de Graham
    """

    def __init__(self) -> None:
        # Heritage des classes
        Graham.Graham.__init__(self)

    def win_creat(self, cloud, width=WIDTH_CAN_DEFAULT,
                  heigh=HEIGT_CAN_DEFAULT) -> None:
        """
        Creation de l interface graphique

        Args:
            cloud (list): Liste des points du nuage
            width (int, optional): Largeur du Canvas. Defaults to 500.
            heigh (int, optional): Hauteur du Canvas. Defaults to 500.
        """
        tk.Tk.__init__(self)
        self.cloud = cloud
        self.can_dim = [width, heigh]
        self.title("Graham")
        self.geometry("-0+55")
        # Canvas principal avec le nuage de points
        self.can = tk.Canvas(
            self, width=self.can_dim[0], heigh=self.can_dim[1], bg="white")
        self.can.pack(side=tk.RIGHT)

        # Frame principale
        frm = tk.Frame(self, heigh=self.can_dim[1])
        frm.pack(side=tk.RIGHT)

        # Label indiquant les etapes realisees
        self.text_label = tk.Label(frm, text="", wraplength=100)
        self.text_label.pack(side=tk.BOTTOM)

        # Bouton pour demarrer l animation
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
        Initialise l animation et permet son demarrage
        """
        global counter
        counter = int()
        self.envelope_anim = list()
        self.start_button['state'] = tk.DISABLED
        self.find_origin()
        # On s assure qu il n y a rien
        self.can.delete("line_convex", "point_convexe", "point_origin")
        # Elements de base
        self.can.create_line(
            0, 0, self.can_dim[0], 0, tag="abscisse", cap="round")
        self.can.create_line(
            0, 0, 0, self.can_dim[1], tag="ordonnee", cap="round")
        # On lance le debut
        self.find_origin_animation()

    def find_origin_animation(self) -> None:
        """
        Animation de la recherche du point avec la plus petite ordonnee et
        abscise
        """
        self.text_label["text"] = "Recherche de l'origine"
        coord_absc = self.can.coords("abscisse")
        coord_ord = self.can.coords("ordonnee")
        # On deplace jusqu a etre a l origine
        if coord_absc[1] < self.origin[1]:
            self.can.move("abscisse", 0, 1)
            self.can.after(10, self.find_origin_animation)    # On recommence
        elif coord_ord[0] < self.origin[0]:
            self.can.move("ordonnee", 1, 0)
            self.can.after(1, self.find_origin_animation)  # On recommence
        else:  # On affiche un rectangle sur l origine
            self.can.create_rectangle(
                self.origin[0] - 5, self.origin[1] - 5, self.origin[0] + 5,
                self.origin[1] + 5, fill=COLOR_GRAHAM,  tag="point_origin")
            self.can.after(1000, self.angle_animation)   # Suite de l animation

    def angle_animation(self) -> None:
        """
        Animation du calcul de l angle entre un point et l origine
        """
        global counter
        self.can.delete("ordonnee")
        if counter < len(self.cloud):
            self.can.delete("Anim_angle")
            self.text_label["text"] = "Mesure de l'angle entre l'origine et\
            l'abscisse relative"
            point = self.cloud[counter]
            self.can.create_line(
                self.origin, point, fil="green", tag="Anim_angle")
            self.can.create_oval(point[0] - 5, point[1] - 5, point[0] + 5,
                                 point[1] + 5, fill="green", tag="Anim_angle")
            counter += 1
            self.can.after(100, self.angle_animation)    # On recommence
        else:
            self.text_label["text"] = "Tri des points en fonction de cet \
                angle"
            self.point_sort = self.sorting_fusion(self.cloud)
            self.can.delete("Anim_angle")
            counter = 2
            for point in self.point_sort:
                self.can.create_text(point[0] - 10, point[1] - 10,
                                     text=self.point_sort.index(point),
                                     tag="point_num")
            self.envelope_anim.extend([self.point_sort[0], self.point_sort[1]])
            # Suite de l animation
            self.can.after(1000, self.convex_hull_animation)

    def convex_hull_animation(self) -> None:
        """
        Animation de la recherche des points de l enveloppe convexe
        """
        global counter
        self.can.delete("abscisse", "point_anim")
        if counter < len(self.point_sort):
            self.text_label["text"] = "Recherche du point le plus à gauche"
            point = self.point_sort[counter]  # Point qui est analyse
            while (self.vectorial_product(self.envelope_anim[-2],
                   self.envelope_anim[-1], point) is True and
                   len(self.envelope_anim) >= 3):
                # Le point teste est plus a l exterieur que le precedent point
                self.envelope_anim.pop()  # On retire le point en trop
            self.envelope_anim.append(point)
            counter += 1
            self.can.after(100, self.convex_hull_animation)   # On recommence
            self.can.delete("line_convex")  # On supprime les enveloppes
            self.can.delete("point_convexe")
            # On dessine la bonne enveloppe
            for point in self.envelope_anim[1:]:
                index_oint = self.envelope_anim.index(point)
                self.can.create_line(self.envelope_anim[index_oint - 1],
                                     self.envelope_anim[index_oint],
                                     fill=COLOR_GRAHAM, tag="line_convex")
                self.can.create_oval(point[0] - 5, point[1] - 5, point[0] + 5,
                                     point[1] + 5, fill=COLOR_GRAHAM,
                                     tag="point_convexe")
        else:
            self.can.create_line(self.envelope_anim[-1], self.origin,
                                 fill=COLOR_GRAHAM, tag="line_convex")
            self.start_button['state'] = tk.NORMAL
            self.text_label["text"] = "Enveloppe convexe complète"
            self.can.delete("point_num")


if __name__ == "__main__":
    import Script.data as data

    data, path, a = data.data()
    Win = GrahamAnimation()
    Win.win_creat(data[0])
    print("FIN")
