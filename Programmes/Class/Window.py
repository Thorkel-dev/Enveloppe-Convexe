# -*- coding: utf-8 -*-
import tkinter as tk    # Gestion de l'interface graphique
from pathlib import Path    # Appel système des paths
import sys  # Gestion de l'interpreteur

# Recuperation du chemin du programme
DIRECTORY = Path(__file__).parents[1]
# Ajout du chemin dans la liste des imports de l'interpreteur
sys.path.append(str(DIRECTORY))

# Import des Scripts et Classes necessaires
import Main as main
import Script.data as data
import Script.cloud_of_points as clouds
import Class.Timer as Timer
import Class.Quickhull as Quickhull
import Class.QuickhullAnimation as QuickhullAnim
import Class.Jarvis as Jarvis
import Class.JarvisAnimation as JarvisAnim
import Class.Graham as Graham
import Class.GrahamAnimation as GrahamAnim

# Recuperation des valeurs par default
INFORMATION = main.INFORMATION
SYMBOLE = main.SYMBOLE
WIDTH_FRAME_DEFAULT = main.WIDTH_FRAME_DEFAULT
WIDTH_CAN_DEFAULT = main.WIDTH_CAN_DEFAULT
HEIGT_CAN_DEFAULT = main.HEIGT_CAN_DEFAULT
WIDTH_CAN_MIN = main.WIDTH_CAN_MIN
WIDTH_CAN_MAX = main.WIDTH_CAN_MAX
HEIGT_CAN_MIN = main.HEIGT_CAN_MIN
HEIGT_CAN_MAX = main.HEIGT_CAN_MAX
POINT_MIN = main.POINT_MIN
POINT_MAX = main.POINT_MAX
MARGIN_POINT_X_DEFAULT = main.MARGIN_POINT_X_DEFAULT
MARGIN_POINT_Y_DEFAULT = main.MARGIN_POINT_Y_DEFAULT


class Window(tk.Tk):
    """
    Creation de l'interface grahique, classe fille de tkinter

    Args:
        width (int, optional): Largeur du Canvas. Defaults to 500.
        heigh (int, optional): Hauteur du Canvas. Defaults to 500.
    """

    def __init__(self, width: int = WIDTH_CAN_DEFAULT,
                 heigh: int = HEIGT_CAN_DEFAULT) -> None:
        global Chrono, G, J, Q, Ganim, Janim, QuickhullAnim
        # Heritage des classes
        tk.Tk.__init__(self)
        G = Graham.Graham()
        J = Jarvis.Jarvis()
        Q = Quickhull.Quickhull()
        Ganim = GrahamAnim.GrahamAnimation()
        Janim = JarvisAnim.JarvisAnimation()
        QuickhullAnim = QuickhullAnim.QuickhullAnimation()
        Chrono = Timer.Timer()
        self.can_dim = [width, heigh]
        self.num_cloud = int()
        self.win_creat()
        self.new_cloud()
        self.title("Envelopes Convexes")
        self.geometry("-550+50")
        self.resizable(width=False, height=False)
        self.mainloop()

    def win_creat(self) -> None:
        """
        Creation de l'interface graphique
        """
        global var_G, var_J, var_Q, var_S, var_radio
        global spinbox_width, spinbox_heigh, spinbox_cloud
        global width_text, heigh_text, point_text
        # Variable de controle
        var_G = tk.BooleanVar()
        var_J = tk.BooleanVar()
        var_Q = tk.BooleanVar()
        var_S = tk.BooleanVar()
        var_radio = tk.StringVar()
        width_text = tk.IntVar()
        heigh_text = tk.IntVar()
        point_text = tk.IntVar()

        # Canvas principal avec le nuage de points
        self.can = tk.Canvas(
            self, width=self.can_dim[0], heigh=self.can_dim[1], bg="white")
        self.can.grid(column=2, row=0, rowspan=4)

        # Frame principal
        frm = tk.Frame(self, heigh=self.can_dim[1], width=WIDTH_FRAME_DEFAULT)
        frm.grid_propagate(False)
        frm.grid(column=0, row=2, sticky="n", columnspan=2, rowspan=2)

        # LabelFrame secondaire se trouvant dans le Label principal,
        # affiche les animation
        label_anim = tk.LabelFrame(
            frm, text="Animation", height=100, width=WIDTH_FRAME_DEFAULT)
        label_anim.grid_propagate(False)
        label_anim.grid(column=0, row=1, sticky="n")

        # LabelFrame secondaire se trouvant dans le Label principal,
        # affiche des informations auteurs
        info_label = tk.LabelFrame(
            frm, text="Enveloppes Convexes", width=WIDTH_FRAME_DEFAULT,
            heigh=100, relief="ridge")
        info_label.grid_propagate(False)
        info_label.grid(column=0, row=0, columnspan=2)
        tk.Label(info_label, text=INFORMATION,
                 justify="left", wraplength=WIDTH_FRAME_DEFAULT).grid()

        # LabelFrame principal se trouvant dans le Label princpal,
        # affiche Temps des programme
        self.label_frame = tk.LabelFrame(
            frm, text="Temps et nombres d'ittérations",
            width=WIDTH_FRAME_DEFAULT, heigh=120)
        self.label_frame.grid_propagate(False)
        self.label_frame.grid(column=0, row=2, rowspan=3)
        self.label_frame.columnconfigure(1, minsize=65)
        self.label_frame.columnconfigure(2, minsize=50)

        # Label secondaire se trouvant dans le Label principal,
        # affichant  Nom du fchier
        self.file_label = tk.Label(frm, text="fichier:")
        self.file_label.grid(row=5, column=0, pady=5)

        # Label secondaire se trouvant dans le Label principal,
        # permet de créer un nuage de point
        label_cloud = tk.LabelFrame(
            frm, text="Créer un nuage", width=WIDTH_FRAME_DEFAULT, heigh=75)
        label_cloud.grid_propagate(False)
        label_cloud.grid(row=7, column=0)
        spinbox_width = tk.Spinbox(
            label_cloud, from_=WIDTH_CAN_MIN, to=WIDTH_CAN_MAX,
            width=8, textvariable=width_text)
        spinbox_heigh = tk.Spinbox(
            label_cloud, from_=HEIGT_CAN_MIN, to=HEIGT_CAN_MAX,
            width=8, textvariable=heigh_text)
        spinbox_cloud = tk.Spinbox(
            label_cloud, from_=POINT_MIN, to=POINT_MAX, width=8,
            textvariable=point_text)
        tk.Label(label_cloud, text="Hauteur").grid(row=0, column=0)
        tk.Label(label_cloud, text="Largeur").grid(row=1, column=0)
        tk.Label(label_cloud, text="Points").grid(row=0, column=2)
        spinbox_width.grid(row=0, column=1, padx=5)
        spinbox_heigh.grid(row=1, column=1, padx=5)
        spinbox_cloud.grid(row=0, column=3, padx=5)
        tk.Button(label_cloud, text="Créer",
                  command=self.cloud_creation).grid(
            row=1, column=2, pady=5, padx=5, columnspan=2)

        # Creation des boutons se trouvant dans le Label principal
        self.previous_bouton = tk.Button(frm, text='Nuage précedent',
                                         state=tk.DISABLED,
                                         command=self.previous_cloud, width=15,
                                         repeatdelay=1000, repeatinterval=500)
        self.previous_bouton.grid(row=6, column=0, sticky="w", pady=5)
        tk.Button(frm, text='Nuage suivant', command=self.next_cloud,
                  width=15, repeatdelay=1000,
                  repeatinterval=500).grid(row=6, column=0, sticky="e", pady=5)
        tk.Button(frm, text='Quitter', command=self.destroy, width=10,
                  activebackground="red2").grid(row=8, column=0,
                                                sticky="sw", pady=5)

        # Creation des Checkbutton se trouvant dans le label_frame principal
        self.check_select = tk.Checkbutton(
            self.label_frame, text="Sectionnener tout",
            command=self.select_all, variable=var_S)
        self.check_select.grid(row=0, column=0, sticky="w")
        self.check_Graham = tk.Checkbutton(
            self.label_frame, text="Graham",
            command=self.envelope_Graham, variable=var_G)
        self.check_Graham.grid(row=1, column=0, sticky="w")
        self.check_Jarvis = tk.Checkbutton(
            self.label_frame, text="Jarvis",
            command=self.envelope_Jarvis, variable=var_J)
        self.check_Jarvis.grid(row=2, column=0, sticky="w")
        self.check_Quickhull = tk.Checkbutton(
            self.label_frame, text="Quickhull",
            command=self.envelope_Quickhull, variable=var_Q)
        self.check_Quickhull.grid(row=3, column=0, sticky="w")

        # Creation des Label se trouvant dans le label_frame principal
        self.time_Graham = tk.Label(self.label_frame, text="00s")
        self.time_Graham.grid(row=1, column=1, sticky="w")
        self.time_Jarvis = tk.Label(self.label_frame, text="00s")
        self.time_Jarvis.grid(row=2, column=1, sticky="w")
        self.time_Quickhull = tk.Label(self.label_frame, text="00s")
        self.time_Quickhull.grid(row=3, column=1, sticky="w")

        self.iteration_Graham = tk.Label(self.label_frame, text="0")
        self.iteration_Graham.grid(row=1, column=2, sticky="e")
        self.iteration_Jarvis = tk.Label(self.label_frame, text="0")
        self.iteration_Jarvis.grid(row=2, column=2, sticky="e")
        self.iteration_Quickhull = tk.Label(self.label_frame, text="0")
        self.iteration_Quickhull.grid(row=3, column=2, sticky="e")

        # Creation des Radiobutton se trouvant dans label_anim,
        # permet de lancer les animations
        tk.Radiobutton(label_anim, text="Graham",
                       command=self.animation_envelope,
                       variable=var_radio, value="Graham").grid(row=0,
                                                                column=0,
                                                                sticky="w")
        tk.Radiobutton(label_anim, text="Jarvis",
                       command=self.animation_envelope,
                       variable=var_radio, value="Jarvis").grid(row=1,
                                                                column=0,
                                                                sticky="w")
        tk.Radiobutton(label_anim, text="Quickhull",
                       command=self.animation_envelope,
                       variable=var_radio, value="Quickhull").grid(row=2,
                                                                   column=0,
                                                                   sticky="w")

        # Initialisation des actions souris
        self.can.bind('<Button-1>', self.add_point)
        self.can.bind('<Button-3>', self.dell_point)

    def add_point(self, event) -> None:
        """
        Ajout d'un nouveau point dans le nuage de points

        Args:
            event (object): variable de controle
        """
        new_point = [event.x, event.y]
        self.can.create_text(new_point, text=SYMBOLE)
        self.cloud.append(new_point)
        clouds.writing(path=self.path, list_points=[
                       self.cloud], can_dim=self.can_dim)
        self.update_win()

    def dell_point(self, event) -> None:
        """
        Retire un point du nuage de point

        Args:
            event (object): variable de controle
        """
        element = self.can.find_overlapping(
            event.x-5, event.y-5, event.x+5, event.y+5)
        for point in element:
            print(self.can.itemcget(point, "tag"))
            if self.can.itemcget(point, "tag") == "Point":
                self.cloud.remove(self.can.coords(point))
                clouds.writing(path=self.path, list_points=[
                               self.cloud], can_dim=self.can_dim)
                self.update_win()

    def next_cloud(self) -> None:
        """
        Charge le nuage suivant
        """
        self.num_cloud += 1
        self.previous_bouton['state'] = tk.NORMAL
        self.new_cloud()

    def previous_cloud(self) -> None:
        """
        Charge le nuage precedant
        """
        self.num_cloud -= 1
        if self.num_cloud <= 0:
            self.previous_bouton['state'] = tk.DISABLED
        self.new_cloud()

    def new_cloud(self, path=None) -> None:
        """
        Charge le nouveau nuage

        Args:
            path (pathlib, optional): Chemin vers le fichier nuage.
            Defaults to None.
        """
        global width_text, heigh_text, point_text
        if path is not None:
            liste_data, self.path, filename = data.data(
                path=path)  # Recuperation des informations
            self.num_cloud += 1
        else:
            liste_data, self.path, filename = data.data(
                self.num_cloud)  # Recuperation des informations
        self.file_label["text"] = "fichier: " + filename
        self.cloud = liste_data[0]
        self.can_dim = liste_data[1]
        # Nouvels dimensions du Canvas
        self.can.config(width=self.can_dim[0], heigh=self.can_dim[1])
        width_text.set(int(self.can_dim[0]))
        heigh_text.set(int(self.can_dim[1]))
        point_text.set(len(liste_data[0]))
        self.update_win()

    def update_win(self) -> None:
        """
        Actualise l'affichage du nuage de points
        """
        self.can.delete("all")
        for point in self.cloud:
            self.can.create_text(point, text=SYMBOLE,
                                 tag="Point", fill='black')
        self.envelope_Graham()
        self.envelope_Jarvis()
        self.envelope_Quickhull()

    def select_all(self) -> None:
        """
        Selectionne toute les Checkbutton
        """
        if var_S.get() is True:  # Si Checkbutton est coche
            self.check_Graham.select()
            self.check_Jarvis.select()
            self.check_Quickhull.select()
        else:  # Sinon on l'efface
            self.check_Graham.deselect()
            self.check_Jarvis.deselect()
            self.check_Quickhull.deselect()
        self.update_win()

    def envelope_Graham(self) -> None:
        """
        Lance le calcul de l'enveloppe convex Avec la methode de Graham
        """
        if var_G.get() is True:  # Si Checkbutton est coche
            Chrono.start()  # On lance le chronometre
            G.convex_hull(self.cloud)
            Chrono.stop()  # Arret du chronometre
            self.time_Graham["text"] = Chrono.chrono
            self.iteration_Graham["text"] = G.itteration
            # On affiche lenveloppe
            self.can.create_polygon(
                G.envelope, outline="red", fill="", tag=("Envelope", "Graham"))
            for point in G.envelope:
                self.can.create_oval(point[0] - 5, point[1] - 5, point[0] + 5,
                                     point[1] + 5, fill="red",
                                     tag=("Envelope", "Graham"))
        else:  # Sinon on l'efface
            self.can.delete("Graham")
            self.check_select.deselect()

    def envelope_Jarvis(self) -> None:
        """
        Lance le calcul de l'enveloppe convex Avec la methode de Jarvis
        """
        if var_J.get() is True:  # Si Checkbutton est coche
            Chrono.start()  # On lance le chronometre
            J.convex_hull(self.cloud)
            Chrono.stop()  # Arret du chronometre
            self.time_Jarvis["text"] = Chrono.chrono
            self.iteration_Jarvis["text"] = J.itteration
            # On affiche lenveloppe
            self.can.create_polygon(J.envelope, outline="blue", fill="",
                                    tag=("Envelope", "Jarvis"))
            for point in J.envelope:
                self.can.create_oval(point[0] - 5, point[1] - 5, point[0] + 5,
                                     point[1] + 5, fill="blue",
                                     tag=("Envelope", "Jarvis"))
        else:  # Sinon on l'efface
            self.can.delete("Jarvis")
            self.check_select.deselect()

    def envelope_Quickhull(self) -> None:
        """
        Lance le calcul de l'enveloppe convex Avec la methode de Quickhull
        """
        if var_Q.get() is True:  # Si Checkbutton est coche
            Chrono.start()  # On lance le chronometre
            Q.convex_hull(self.cloud)
            Chrono.stop()  # Arret du chronometre
            self.time_Quickhull["text"] = Chrono.chrono
            self.iteration_Quickhull["text"] = Q.itteration
            # On affiche lenveloppe
            self.can.create_polygon(Q.envelope, outline="green",
                                    fill="", tag=("Envelope", "Quickhull"))
            for point in Q.envelope:
                self.can.create_oval(point[0] - 5, point[1] - 5, point[0] + 5,
                                     point[1] + 5, fill="green",
                                     tag=("Envelope", "Quickhull"))
        else:  # Sinon on l'efface
            self.can.delete("Quickhull")
            self.check_select.deselect()

    def animation_envelope(self) -> None:
        """
        Lance les animations en fonction du Radiobutton selectionne
        """
        if var_radio.get() == "Graham":
            Ganim.win_creat(self.cloud, self.can_dim[0], self.can_dim[1])
        elif var_radio.get() == "Jarvis":
            Janim.win_creat(self.cloud, self.can_dim[0], self.can_dim[1])
        elif var_radio.get() == "Quickhull":
            QuickhullAnim.win_creat(
                self.cloud, self.can_dim[0], self.can_dim[1])

    def cloud_creation(self) -> None:
        """
        Creation d un nuage celon les criteres voulu
        """
        global width_text, heigh_text, point_text
        # Recuperation des valeur
        width = int(spinbox_width.get())
        heigh = int(spinbox_heigh.get())
        point = int(spinbox_cloud.get())
        # On verifie si elles respectent les regles
        if width > WIDTH_CAN_MAX or width < WIDTH_CAN_MIN:
            width = min(width, WIDTH_CAN_MAX)
            width = max(width, WIDTH_CAN_MIN)
            width_text.set(width)
        if heigh > HEIGT_CAN_MAX or heigh < HEIGT_CAN_MIN:
            heigh = min(heigh, HEIGT_CAN_MAX)
            heigh = max(heigh, HEIGT_CAN_MIN)
            heigh_text.set(heigh)
        while (point * MARGIN_POINT_X_DEFAULT * MARGIN_POINT_Y_DEFAULT * 5
               > heigh * width):
            point -= 1
            point_text.set(int(point))
        # On ecrit le fichier
        path = clouds.writing(target_point_num=point, can_dim=(width, heigh))
        self.new_cloud(path=path)  # On charge le nouveau nuage


if __name__ == "__main__":
    Win = Window()
    print("FIN")
