import tkinter as tk
from tkinter import ttk

from dashboard_controller import DashboardController

class DashboardView:

    def __init__(self, controller: DashboardController) -> None:
        self.controller = controller

        self.fenster = tk.Tk()
        self.fenster.title("Mein Studien-Dashboard")
        self.fenster.geometry("1200x750")

        self.kopfbereich_erstellen()
        self.inhaltsbereich_erstellen()
        self.studienfortschritt_erstellen()
        self.notenbereich_erstellen()


    def kopfbereich_erstellen(self) -> None:
        self.kopfbereich = tk.Frame(
            self.fenster,
            bg="#24415f",
            height=70
        )
        self.kopfbereich.pack(fill="x")

        self.titel = tk.Label(
            self.kopfbereich,
            text="Mein Studien-Dashboard",
            bg="#24415f",
            fg="white",
            font=("Arial", 18, "bold")
        )
        self.titel.pack(
            side="left",
            padx=40,
            pady=15
        )

        self.studiengang_titel = tk.Label(
            self.kopfbereich,
            text="Medizinische Informatik",
            bg="#24415f",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.studiengang_titel.pack(
            side="right",
            padx=40,
            pady=15
        )


    def inhaltsbereich_erstellen(self) -> None:
        self.inhalt = tk.Frame(self.fenster)
        self.inhalt.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.kennzahlen_zeile = tk.Frame(self.inhalt)
        self.kennzahlen_zeile.pack(fill="x")

        self.kennzahlen_zeile.columnconfigure(
            0,
            weight=1,
            uniform="kennzahlen"
        )
        self.kennzahlen_zeile.columnconfigure(
            1,
            weight=1,
            uniform="kennzahlen"
        )


    def studienfortschritt_erstellen(self) -> None:
        kennzahlen = self.controller.kennzahlen_abrufen()

        self.fortschritt_bereich = tk.Frame(
            self.kennzahlen_zeile,
            bd=1,
            relief="solid",
            height=100
        )
        self.fortschritt_bereich.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        self.fortschritt_titel = tk.Label(
            self.fortschritt_bereich,
            text="Studienfortschritt",
            font=("Arial", 12, "bold")
        )
        self.fortschritt_titel.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.fortschritt_text = tk.Label(
            self.fortschritt_bereich,
            text=f'{kennzahlen["erreichte_ects"]} von {kennzahlen["gesamt_ects"]} ECTS',
            font=("Arial", 16, "bold")
        )
        self.fortschritt_text.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        self.fortschritt_werte = tk.Frame(
            self.fortschritt_bereich
        )
        self.fortschritt_werte.pack(
            fill="x",
            padx=20
        )

        self.fortschritt_ziel = tk.Label(
            self.fortschritt_werte,
            text="Ziel: Abschluss innerhalb von 4 Jahren"
        )
        self.fortschritt_ziel.pack(side="left")

        self.fortschritt_prozent = tk.Label(
            self.fortschritt_werte,
            text=f'{kennzahlen["ects_fortschritt"]:.1f} % erreicht'
        )
        self.fortschritt_prozent.pack(side="right")

        self.fortschritt_balken = ttk.Progressbar(
            self.fortschritt_bereich,
            maximum=100,
            value=kennzahlen["ects_fortschritt"]
        )
        self.fortschritt_balken.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

    def notenbereich_erstellen(self) -> None:
        kennzahlen = self.controller.kennzahlen_abrufen()

        notendurchschnitt = kennzahlen["notendurchschnitt"]
        zielnote = kennzahlen["zielnote"]
        notenabweichung = kennzahlen["notenabweichung"]

        if notendurchschnitt is None:
            aktuell_text = "Aktuell: –"
        else:
            aktuell_text = f"Aktuell: {notendurchschnitt:.1f}"

        ziel_text = f"Ziel: {zielnote:.1f} oder besser"

        if notendurchschnitt is None or notenabweichung is None:
            abweichung_text = "Noch kein Notenvergleich möglich"
        elif notendurchschnitt < zielnote:
            abweichung_text = (
                f"{abs(notenabweichung):.1f} Notenpunkte besser als Ziel"
            )
        elif notendurchschnitt > zielnote:
            abweichung_text = (
                f"{abs(notenabweichung):.1f} Notenpunkte schlechter als Ziel"
            )
        else:
            abweichung_text = "Zielnote genau erreicht"

        self.noten_bereich = tk.Frame(
            self.kennzahlen_zeile,
            bd=1,
            relief="solid",
            height=100
        )
        self.noten_bereich.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        self.noten_titel = tk.Label(
            self.noten_bereich,
            text="Notendurchschnitt",
            font=("Arial", 12, "bold")
        )
        self.noten_titel.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.noten_text = tk.Label(
            self.noten_bereich,
            text=aktuell_text,
            font=("Arial", 16, "bold")
        )
        self.noten_text.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        self.noten_ziel = tk.Label(
            self.noten_bereich,
            text=ziel_text
        )
        self.noten_ziel.pack(
            anchor="w",
            padx=20,
            pady=(0, 8)
        )

        self.noten_abweichung = tk.Label(
            self.noten_bereich,
            text=abweichung_text
        )
        self.noten_abweichung.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    def starten(self) -> None:
        self.fenster.mainloop()

