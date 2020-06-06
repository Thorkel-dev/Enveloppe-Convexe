# -*- coding: utf-8 -*-
import datetime as dt  # Mise en oeuvre rapide du type date heure


class Timer():
    """
    Chronometre
    """

    def __inti__(self) -> None:
        self.start()  # On lance chronometre

    def start(self) -> None:
        """
        Lancement du chronometre
        """
        self.start_time = dt.datetime.now()  # Capture l heure de l ordinateur

    def stop(self) -> None:
        """
        Arret du chronometre
        """
        self.chrono = str()
        stop_time = dt.datetime.now()  # Capture l heure de l ordinateur
        time_execut = stop_time - self.start_time
        # Difference entre debut et fin
        self.time_s = time_execut.total_seconds()
        time_execut = str(time_execut)[5:]
        # Mise en forme du temps
        if time_execut != "00":
            if time_execut[:3] != "00.":
                self.chrono += time_execut[:3].lstrip("0") + "s "
            if time_execut[3:6] != "000":
                self.chrono += time_execut[3:6].lstrip("0") + "ms "
            if time_execut[6:] != "000":
                self.chrono += time_execut[6:].lstrip("0") + "µs"
        else:
            self.chrono = "< 1µs"
