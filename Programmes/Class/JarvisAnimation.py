# -*- coding: utf-8 -*-
import tkinter as tk
from pathlib import Path    # Appel systeme des paths
import sys  # Gestion de l interpreteur
import math as mt   # Methode mathematique

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l interpreteur
sys.path.append(str(DIRECTORY))

# Import des classes necessaires
import Class.Jarvis as Jarvis
import Main as main

# Recuperation des valeurs par defaut
SYMBOLE = main.SYMBOLE
WIDTH_CAN_DEFAULT = main.WIDTH_CAN_DEFAULT
HEIGT_CAN_DEFAULT = main.HEIGT_CAN_DEFAULT
COLOR_JARVIS = main.COLOR_JARVIS


class JarvisAnimation(tk.Tk, Jarvis.Jarvis):
    """
    Fenetre pour afficher l animation de Jarvis

    Args:
        cloud (list): Liste des points du nuage
        width (int, optional): Largeur du Canvas. Defaults to 500.
        heigh (int, optional): Hauteur du Canvas. Defaults to 500.
    """

    def __init__(self) -> None:
        # Heritage des classes
        Jarvis.Jarvis.__init__(self)

    def win_creat(self, cloud: list, width: int = 500, heigh: int = 500) \
            -> None:
        """
        Creation de l interface graphique

        Args:
            cloud (list): Liste des points du nuage
            width (int, optional): Largeur du Canvas. Defaults to 500.
            heigh (int, optional): Hauteur du Canvas. Defaults to 500.
        """
        tk.Tk.__init__(self)
        self.can_dim = [width, heigh]
        self.cloud = cloud
        self.title("Jarvis")
        self.geometry("-0+70")
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
        self.envelope_anim = list()
        self.list_points = self.cloud.copy()
        self.start_button['state'] = tk.DISABLED
        self.find_origin()
        # On s assure qu il n y a rien
        self.can.delete("line_convex", "point_convexe",
                        "point_origin", "previous_line")
        # Element de base
        self.can.create_line(
            0, 0, self.can_dim[0], 0, tag="abscisse", cap="round")
        self.can.create_line(
            0, 0, 0, self.can_dim[1], tag="ordonnee", cap="round")
        # On lance le debut
        self.find_origin_animation()

    def find_origin_animation(self) -> None:
        """
        Animation de la recherche du point avec la plus petite ordonnee et
        abscisse
        """
        global previous_point_1, previous_point_2
        self.text_label["text"] = "Recherche de l'origine"
        coord_absc = self.can.coords("abscisse")
        coord_ord = self.can.coords("ordonnee")
        # On deplace jusqu a etre sur l origine
        if coord_absc[1] < self.origin[1]:
            self.can.move("abscisse", 0, 1)
            self.can.after(10, self.find_origin_animation)    # On recommence
        elif coord_ord[0] < self.origin[0]:
            self.can.move("ordonnee", 1, 0)
            self.can.after(1, self.find_origin_animation)  # On recommence
        else:  # On affiche un rectangle sur l origine
            self.can.create_rectangle(self.origin[0] - 5, self.origin[1] - 5,
                                      self.origin[0] + 5, self.origin[1] + 5,
                                      fill=COLOR_JARVIS,  tag="point_origin")
            previous_point_1 = self.origin
            previous_point_2 = [self.origin[0] + 1000, self.origin[1]]
            # Suite de l animation
            self.envelope_anim.append(self.origin)
            self.can.after(1000, self.find_next_point_anim)

    def find_next_point_anim(self) -> None:
        """
        Animation de la recherche des points de l enveloppe convexe
        """
        global min_angle, previous_angle, counter
        counter = int()
        if previous_point_1 == self.origin and len(self.envelope_anim) >= 3:
            # Si le dernier point est l origine alors on a fait le tour de
            # l enveloppe
            self.text_label["text"] = "Enveloppe convexe complète"
            self.start_button['state'] = tk.NORMAL
            return
        min_angle = mt.inf
        previous_delta_x = previous_point_1[0] - previous_point_2[0]
        previous_delta_y = previous_point_1[1] - previous_point_2[1]
        previous_angle = mt.atan2(previous_delta_y, previous_delta_x)
        self.can.create_line(previous_point_1, previous_point_2,
                             fill="red", tag="previous_line")
        self.angle_anim()    # Suite de l animation

    def angle_anim(self) -> None:
        """
        Animation de la recherche du point le plus a droite du segment
        precedent
        """
        global counter, min_angle, previous_point_1, previous_point_2
        global next_point
        if counter < len(self.list_points):
            self.text_label["text"] = "Recherche du point le plus à droite"
            point = self.list_points[counter]
            next_delta_x = point[0] - previous_point_1[0]
            next_delta_y = point[1] - previous_point_1[1]
            next_angle = mt.atan2(next_delta_y, next_delta_x)
            self.can.delete("line_anim", "point_anim", "abscisse", "ordonnee")
            # Le point analyse est affiche en vert
            self.can.create_line(point, previous_point_1,
                                 fill="green", tag="line_anim")
            self.can.create_oval(point[0] - 5, point[1] - 5,
                                 point[0] + 5, point[1] + 5,
                                 fill="green", tag="point_anim")
            if abs(next_angle - previous_angle) <= min_angle:
                if previous_angle != next_angle:  # Si les points ne sont pas
                    # alignes
                    min_angle = abs(next_angle - previous_angle)
                    next_point = point
                else:
                    next_point = self.distance(
                        point, previous_point_1, previous_point_2)
                    self.envelope_anim[-1] = next_point
            counter += 1
            self.can.after(50, self.angle_anim)  # On recommence
        # Si le point est aligne en ordonne par rapport a l origine
        elif next_point[1] == self.origin[1]:
            self.envelope_anim.append(next_point)
            self.can.delete("line_anim", "point_anim", "previous_line")
            # Le point de l enveloppe est affiche en bleu
            self.can.create_line(next_point, previous_point_1,
                                 fill=COLOR_JARVIS, tag="line_convex")
            self.can.create_line(next_point, self.origin,
                                 fill=COLOR_JARVIS, tag="line_convex")
            self.can.create_oval(next_point[0] - 5, next_point[1] - 5,
                                 next_point[0] +
                                 5, next_point[1] + 5, fill=COLOR_JARVIS,
                                 tag="point_convexe")
            self.text_label["text"] = "Enveloppe convexe complète"
            self.start_button['state'] = tk.NORMAL
            return  # On a fait le tour
        else:
            self.list_points.remove(next_point)
            self.envelope_anim.append(next_point)
            self.can.delete("line_anim", "point_anim", "previous_line")
            # Le point de l enveloppe est affiche en bleu
            self.can.create_line(next_point, previous_point_1,
                                 fill=COLOR_JARVIS, tag="line_convex")
            self.can.create_oval(next_point[0] - 5, next_point[1] - 5,
                                 next_point[0] + 5, next_point[1] + 5,
                                 fill=COLOR_JARVIS, tag="point_convexe")
            # Prochain segment
            previous_point_1 = self.envelope_anim[-1]
            previous_point_2 = self.envelope_anim[-2]
            # On recommence pour le prochain point
            self.can.after(250, self.find_next_point_anim)


if __name__ == "__main__":
    import Script.data as data

    data, path, a = data.data()
    Win = JarvisAnimation()
    Win.win_creat(data[0])
    print("FIN")
