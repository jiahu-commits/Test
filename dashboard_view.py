import tkinter as tk

from dashboard_controller import DashboardController

class DashboardView:
    def __init__(self, controller: DashboardController):
        self.controller = controller
        self.fenster = tk.Tk()
        self.fenster.title("Mein Studien-Dashboard")
        self.fenster.geometry("900x600")

        self.kopfbereich = tk.Frame(self.fenster, bg="#24415f",height = 70)
        self.kopfbereich.pack(fill="x")
        self.titel = tk.Label(
            self.kopfbereich,
            text="Mein Studien-Dashboard",
            bg="#24415f",
            fg="white",
            font=("Arial", 18, "bold")
        )

        self.titel.pack(pady=15)

        self.inhalt = tk.Frame(self.fenster)
        self.inhalt.pack(fill="both", expand=True, padx=20, pady=20)
        self.kennzahlen_zeile = tk.Frame(self.inhalt)
        self.kennzahlen_zeile.pack(fill="x")
        self.fortschritt_bereich = tk.Frame(
            self.kennzahlen_zeile,
            bd=1,
            relief="solid",
            height= 100
        )

        self.fortschritt_bereich.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        self.fortschritt_titel = tk.Label(
            self.fortschritt_bereich,
            text="Studienfortschritt",
            font=("Arial", 12, "bold")
        )

        self.fortschritt_titel.pack(pady=(10, 5))


    def starten(self)->None:
        self.fenster.mainloop()


