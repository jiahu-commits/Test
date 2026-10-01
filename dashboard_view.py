import tkinter as tk
from tkinter import ttk

from dashboard_controller import DashboardController

class DashboardView:
    def __init__(self, controller: DashboardController):
        self.controller = controller
        self.fenster = tk.Tk()
        self.fenster.title("Mein Studien-Dashboard")
        self.fenster.geometry("1200x750")

        self.kopfbereich = tk.Frame(self.fenster, bg="#24415f",height = 70)
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

        self.inhalt = tk.Frame(self.fenster)
        self.inhalt.pack(fill="both", expand=True, padx=20, pady=20)
        self.kennzahlen_zeile = tk.Frame(self.inhalt)
        self.kennzahlen_zeile.pack(fill="x")
        self.kennzahlen_zeile.columnconfigure(0, weight=1, uniform="kennzahlen")
        self.kennzahlen_zeile.columnconfigure(1, weight=1, uniform="kennzahlen")

        self.fortschritt_bereich = tk.Frame(
            self.kennzahlen_zeile,
            bd=1,
            relief="solid",
            height= 100
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

        self.fortschritt_balken = ttk.Progressbar(
            self.fortschritt_bereich,
            maximum=100
        )

        kennzahlen = self.controller.kennzahlen_abrufen()
        self.fortschritt_balken["value"] = kennzahlen["ects_fortschritt"]

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

        self.fortschritt_werte = tk.Frame(self.fortschritt_bereich)
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

        self.fortschritt_balken.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

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

        self.noten_titel.pack(pady=(10, 5))
        if kennzahlen["notendurchschnitt"] is None:
            noten_text = "Noch keine Note"
        else:
            noten_text = f'{kennzahlen["notendurchschnitt"]:.2f}'

        self.noten_wert = tk.Label(
            self.noten_bereich,
            text=noten_text,
            font=("Arial", 16, "bold")
        )

        self.noten_wert.pack(pady=(5, 10))

        self.zeit_bereich = tk.Frame(
            self.inhalt,
            bd=1,
            relief="solid"
        )

        self.zeit_bereich.pack(
            fill="x",
            pady=(20, 0)
        )

        self.zeit_titel = tk.Label(
            self.zeit_bereich,
            text="Zeitlicher Stand",
            font=("Arial", 12, "bold")
        )

        self.zeit_titel.pack(pady=(10, 5))



    def starten(self)->None:
        self.fenster.mainloop()


