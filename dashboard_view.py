import tkinter as tk
from tkinter import ttk, messagebox
from modul_status import ModulStatus
from pruefungsart import Pruefungsart

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
        self.zeitbereich_erstellen()
        self.modulbereich_erstellen()

        self.dashboard_aktualisieren()


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
            text="",
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
            text=""
        )

        self.fortschritt_prozent.pack(side="right")

        self.fortschritt_balken = ttk.Progressbar(
            self.fortschritt_bereich,
            maximum=100,
            value=0
        )

        self.fortschritt_balken.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

    def notenbereich_erstellen(self) -> None:
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
            text="",
            font=("Arial", 16, "bold")
        )

        self.noten_text.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        self.noten_ziel = tk.Label(
            self.noten_bereich,
            text=""
        )

        self.noten_ziel.pack(
            anchor="w",
            padx=20,
            pady=(0, 8)
        )

        self.noten_abweichung = tk.Label(
            self.noten_bereich,
            text=""
        )

        self.noten_abweichung.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    def zeitbereich_erstellen(self) -> None:
        self.zeit_bereich = tk.Frame(
            self.inhalt,
            bd=1,
            relief="solid",
            height=100
        )

        self.zeit_bereich.pack(
            fill="x",
            pady=(20, 0)
        )

        self.zeit_bereich.columnconfigure(
            0,
            weight=1,
            uniform="zeit"
        )

        self.zeit_bereich.columnconfigure(
            1,
            weight=1,
            uniform="zeit"
        )

        self.zeit_links = tk.Frame(
            self.zeit_bereich
        )

        self.zeit_links.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.zeit_titel = tk.Label(
            self.zeit_links,
            text="Zeitlicher Stand",
            font=("Arial", 12, "bold")
        )

        self.zeit_titel.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        self.zeit_text = tk.Label(
            self.zeit_links,
            text="",
            font=("Arial", 14)
        )

        self.zeit_text.pack(
            anchor="w",
            padx=20,
            pady=(0, 5)
        )

        self.zeit_prozent = tk.Label(
            self.zeit_links,
            text=""
        )

        self.zeit_prozent.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        self.zeit_rechts = tk.Frame(
            self.zeit_bereich
        )

        self.zeit_rechts.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.zeit_soll = tk.Label(
            self.zeit_rechts,
            text=""
        )

        self.zeit_soll.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        self.zeit_abweichung = tk.Label(
            self.zeit_rechts,
            text=""
        )

        self.zeit_abweichung.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    def dashboard_aktualisieren(self) -> None:
        kennzahlen = self.controller.kennzahlen_abrufen()

        self.fortschritt_text.config(
            text=f'{kennzahlen["erreichte_ects"]} von {kennzahlen["gesamt_ects"]} ECTS'
        )

        self.fortschritt_prozent.config(
            text=f'{kennzahlen["ects_fortschritt"]:.1f} % erreicht'
        )

        self.fortschritt_balken.config(
            value=kennzahlen["ects_fortschritt"]
        )

        notendurchschnitt = kennzahlen["notendurchschnitt"]
        zielnote = kennzahlen["zielnote"]
        notenabweichung = kennzahlen["notenabweichung"]

        if notendurchschnitt is None:
            aktuell_text = "Aktuell: –"
        else:
            aktuell_text = f"Aktuell: {notendurchschnitt:.1f}"

        ziel_text = f"Ziel: {zielnote:.1f} oder besser"

        if notendurchschnitt is None:
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

        self.noten_text.config(
            text=aktuell_text
        )

        self.noten_ziel.config(
            text=ziel_text
        )

        self.noten_abweichung.config(
            text=abweichung_text
        )

        self.zeit_text.config(
            text=(
                f'{kennzahlen["vergangene_monate"]} von '
                f'{kennzahlen["studiendauer_monate"]} '
                f'Studienmonaten vergangen'
            )
        )

        self.zeit_prozent.config(
            text=(
                f'{kennzahlen["zeitfortschritt"]:.1f} % '
                f'der geplanten Studienzeit'
            )
        )

        self.zeit_soll.config(
            text=f'Soll-Stand: {kennzahlen["soll_ects"]:.2f} ECTS'
        )

        self.zeit_abweichung.config(
            text=(
                f'Abweichung '
                f'{kennzahlen["ects_soll_ist_abweichung"]:+.2f} ECTS'
            )
        )


    def ausgewaehltes_semester_finden(self):
        for semester in self.controller.semester_abrufen():
            if self.semester_auswahl.get() == f"Semester {semester.nummer}":
                return semester

        return None

    def semester_werte_erstellen(self) -> list[str]:
        semester_werte = []

        for semester in self.controller.semester_abrufen():
            semester_werte.append(f"Semester {semester.nummer}")

        return semester_werte

    def modulbereich_erstellen(self) -> None:
        self.modul_bereich = tk.Frame(
            self.inhalt,
            bd=1,
            relief="solid"
        )
        self.modul_bereich.pack(
            fill="both",
            expand=True,
            pady=(20, 0)
        )

        self.modul_kopfzeile = tk.Frame(
            self.modul_bereich
        )
        self.modul_kopfzeile.pack(
            fill="x",
            padx=20,
            pady=15
        )

        self.modul_kopfzeile.columnconfigure(
            1,
            weight=1
        )

        self.semester_bereich = tk.Frame(
            self.modul_kopfzeile
        )
        self.semester_bereich.grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 20)
        )

        semester_werte = self.semester_werte_erstellen()

        self.semester_auswahl = ttk.Combobox(
            self.semester_bereich,
            values=semester_werte,
            state="readonly",
            width=14
        )
        self.semester_auswahl.pack(
            anchor="w"
        )

        if semester_werte:
            self.semester_auswahl.current(0)

        self.verwaltungs_aktionen = tk.Frame(
            self.modul_kopfzeile
        )
        self.verwaltungs_aktionen.grid(
            row=0,
            column=1,
            sticky="e"
        )

        self.semester_hinzufuegen_button = tk.Button(
            self.verwaltungs_aktionen,
            text="+ Semester hinzufügen",
            command=self.semester_hinzufuegen
        )
        self.semester_hinzufuegen_button.pack(
            side="left",
            padx=(0, 10)
        )

        self.semester_entfernen_button = tk.Button(
            self.verwaltungs_aktionen,
            text="- Semester entfernen",
            command=self.semester_entfernen
        )
        self.semester_entfernen_button.pack(
            side="left",
            padx=(0, 10)
        )

        self.modul_hinzufuegen_button = tk.Button(
            self.verwaltungs_aktionen,
            text="+ Modul hinzufügen",
            state="normal",
            command=self.modul_hinzufuegen
        )
        self.modul_hinzufuegen_button.pack(
            side="left",
            padx=(0, 10)
        )

        self.modul_entfernen_button = tk.Button(
            self.verwaltungs_aktionen,
            text="- Modul entfernen",
            state="normal",
            command=self.ausgewaehltes_modul_entfernen
        )
        self.modul_entfernen_button.pack(
            side="left",
        )

        self.tabellen_bereich = tk.Frame(
            self.modul_bereich
        )
        self.tabellen_bereich.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.modul_tabelle = ttk.Treeview(
            self.tabellen_bereich,
            columns=("modul","pruefungsart", "ects", "status", "note"),
            show="headings",
            selectmode="browse",
            height=6
        )

        self.modul_tabelle.heading(
            "modul",
            text="Modul",
            anchor="w"
        )
        self.modul_tabelle.column(
            "modul",
            width=550,
            anchor="w"
        )

        self.modul_tabelle.heading(
            "pruefungsart",
            text="Prüfungsart",
        )

        self.modul_tabelle.column(
            "pruefungsart",
            width=180,
            anchor="center",
            stretch=False
        )

        self.modul_tabelle.heading(
            "ects",
            text="ECTS"
        )
        self.modul_tabelle.column(
            "ects",
            width=80,
            anchor="center",
            stretch=False
        )

        self.modul_tabelle.heading(
            "status",
            text="Status"
        )
        self.modul_tabelle.column(
            "status",
            width=160,
            anchor="center",
            stretch=False
        )

        self.modul_tabelle.heading(
            "note",
            text="Note"
        )
        self.modul_tabelle.column(
            "note",
            width=80,
            anchor="center",
            stretch=False
        )

        self.modul_tabelle.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.modul_scrollbar = ttk.Scrollbar(
            self.tabellen_bereich,
            orient="vertical",
            command=self.modul_tabelle.yview
        )
        self.modul_scrollbar.pack(
            side="right",
            fill="y"
        )

        self.modul_tabelle.config(
            yscrollcommand=self.modul_scrollbar.set
        )

        self.modul_tabelle.bind(
            "<Double-1>",
            self.modul_bearbeiten
        )

        self.semester_auswahl.bind(
            "<<ComboboxSelected>>",
            self.modultabelle_aktualisieren
        )

        self.modultabelle_aktualisieren()

    def modultabelle_aktualisieren(self, ereignis=None) -> None:
        for zeile in self.modul_tabelle.get_children():
            self.modul_tabelle.delete(zeile)

        ausgewaehltes_semester = self.ausgewaehltes_semester_finden()

        if ausgewaehltes_semester is None:
            return

        module = self.controller.module_abrufen(
            ausgewaehltes_semester.nummer
        )

        for modul in module:
            pruefungsart =  ""
            note = ""

            if modul.pruefungsleistung is not None:
                pruefungsart = modul.pruefungsleistung.pruefungsart.value

                if modul.pruefungsleistung.note is not None:
                    note = f"{modul.pruefungsleistung.note:.1f}"

            self.modul_tabelle.insert(
                "",
                "end",
                values=(
                    modul.name,
                    pruefungsart,
                    modul.ects,
                    modul.status.value,
                    note
                )
            )

    def semester_hinzufuegen(self) -> None:
        neue_nummer = 1

        for semester in self.controller.semester_abrufen():
            if semester.nummer >= neue_nummer:
                neue_nummer = semester.nummer + 1

        self.controller.semester_hinzufuegen(neue_nummer)

        semester_werte = self.semester_werte_erstellen()

        self.semester_auswahl.config(
            values=semester_werte
        )
        self.semester_auswahl.set(
            f"Semester {neue_nummer}"
        )

        self.modultabelle_aktualisieren()

    def semester_entfernen(self) -> None:
        ausgewaehltes_semester = self.ausgewaehltes_semester_finden()

        if ausgewaehltes_semester is None:
            messagebox.showinfo(
                "Kein Semester ausgewählt",
                "Bitte zuerst ein Semester auswählen.",
                parent=self.fenster
            )
            return

        hoechste_nummer = max(
            semester.nummer
            for semester in self.controller.semester_abrufen()
        )

        if ausgewaehltes_semester.nummer != hoechste_nummer:
            messagebox.showinfo(
                "Semester kann nicht entfernt werden",
                "Es kann nur das letzte Semester entfernt werden.",
                parent=self.fenster
            )
            return

        module = self.controller.module_abrufen(
            ausgewaehltes_semester.nummer
        )

        if module:
            messagebox.showinfo(
                "Semester nicht leer",
                "Dieses Semester enthält noch Module und kann "
                "deshalb nicht entfernt werden.",
                parent=self.fenster
            )
            return

        self.controller.semester_entfernen(
            ausgewaehltes_semester.nummer
        )

        semester_werte = self.semester_werte_erstellen()

        self.semester_auswahl.config(
            values=semester_werte
        )

        if semester_werte:
            self.semester_auswahl.current(len(semester_werte) - 1)
        else:
            self.semester_auswahl.set("")

        self.modultabelle_aktualisieren()

    def modul_hinzufuegen(self) -> None:
        ausgewaehltes_semester = self.ausgewaehltes_semester_finden()

        if ausgewaehltes_semester is None:
            messagebox.showinfo(
                "Kein Semester ausgewählt",
                "Bitte zuerst ein Semester auswählen.",
                parent=self.fenster
            )
            return

        modul_fenster = tk.Toplevel(self.fenster)
        modul_fenster.title("Modul hinzufügen")

        modul_fenster.transient(self.fenster)
        modul_fenster.grab_set()

        tk.Label(
            modul_fenster,
            text="Modulname:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        modulname_eingabe = tk.Entry(modul_fenster)

        modulname_eingabe.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            modul_fenster,
            text="ECTS:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        ects_auswahl = ttk.Combobox(
            modul_fenster,
            values=[5, 10],
            state="readonly"
        )

        ects_auswahl.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            modul_fenster,
            text="Status:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        status_auswahl = ttk.Combobox(
            modul_fenster,
            values=[status.value for status in ModulStatus],
            state="readonly"
        )

        status_auswahl.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            modul_fenster,
            text="Prüfungsart:"
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        pruefungsart_auswahl = ttk.Combobox(
            modul_fenster,
            values=[art.value for art in Pruefungsart],
            state="readonly"
        )

        pruefungsart_auswahl.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            modul_fenster,
            text="Note:"
        ).grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        note_eingabe = tk.Entry(modul_fenster)

        note_eingabe.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )

        def modul_speichern() -> None:
            modulname = modulname_eingabe.get()
            ects = ects_auswahl.get()
            status = status_auswahl.get()
            pruefungsart = pruefungsart_auswahl.get()
            note = note_eingabe.get()

            try:
                self.controller.modul_hinzufuegen(
                    ausgewaehltes_semester.nummer,
                    modulname,
                    ects,
                    status,
                    pruefungsart,
                    note
                )

            except ValueError as fehler:
                    messagebox.showerror("Ungültige Eingabe",str(fehler))
                    return

            self.modultabelle_aktualisieren()
            self.dashboard_aktualisieren()
            modul_fenster.destroy()

        speichern_button = tk.Button(
            modul_fenster,
            text="Speichern",
            command=modul_speichern
        )

        speichern_button.grid(
            row=5,
            column=0,
            columnspan=2,
            padx=10,
            pady=15
        )

    def modul_bearbeiten(self, ereignis=None) -> None:
        ausgewaehlte_zeile = self.modul_tabelle.selection()

        if not ausgewaehlte_zeile:
            return

        zeilen_id = ausgewaehlte_zeile[0]

        zeilen_werte = self.modul_tabelle.item(
            zeilen_id,
            "values"
        )

        modulname = zeilen_werte[0]
        pruefungsart = zeilen_werte[1]
        status = zeilen_werte[3]
        note = zeilen_werte[4]

        ausgewaehltes_semester = self.ausgewaehltes_semester_finden()

        if ausgewaehltes_semester is None:
            return

        bearbeiten_fenster = tk.Toplevel(self.fenster)
        bearbeiten_fenster.title("Modul bearbeiten")

        bearbeiten_fenster.transient(self.fenster)
        bearbeiten_fenster.grab_set()

        tk.Label(
            bearbeiten_fenster,
            text="Prüfungsart:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        pruefungsart_auswahl = ttk.Combobox(
            bearbeiten_fenster,
            values=[
                pruefungsart_option.value
                for pruefungsart_option in Pruefungsart
            ],
            state="readonly"
        )

        pruefungsart_auswahl.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        pruefungsart_auswahl.set(pruefungsart)

        tk.Label(
            bearbeiten_fenster,
            text="Status:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        status_auswahl = ttk.Combobox(
            bearbeiten_fenster,
            values=[
                status_option.value
                for status_option in ModulStatus
            ],
            state="readonly"
        )

        status_auswahl.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        status_auswahl.set(status)

        tk.Label(
            bearbeiten_fenster,
            text="Note:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        note_eingabe = tk.Entry(
            bearbeiten_fenster
        )

        note_eingabe.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        note_eingabe.insert(
            0,
            note
        )

        def aenderungen_speichern() -> None:
            neue_pruefungsart = pruefungsart_auswahl.get()
            neuer_status = status_auswahl.get()
            neue_note = note_eingabe.get()

            try:
                self.controller.modul_bearbeiten(
                    ausgewaehltes_semester.nummer,
                    modulname,
                    neue_pruefungsart,
                    neuer_status,
                    neue_note
                    )


            except ValueError as fehler:
                    messagebox.showerror("Ungültige Eingabe",str(fehler))
                    return

            self.modultabelle_aktualisieren()
            self.dashboard_aktualisieren()
            bearbeiten_fenster.destroy()

        speichern_button = tk.Button(
            bearbeiten_fenster,
            text="Speichern",
            command=aenderungen_speichern
        )

        speichern_button.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=15
        )

    def ausgewaehltes_modul_entfernen(self) -> None:
        ausgewaehlte_zeile = self.modul_tabelle.selection()

        if not ausgewaehlte_zeile:
            return

        zeilen_id = ausgewaehlte_zeile[0]

        zeilen_werte = self.modul_tabelle.item(
            zeilen_id,
            "values"
        )

        modulname = zeilen_werte[0]

        ausgewaehltes_semester = self.ausgewaehltes_semester_finden()

        if ausgewaehltes_semester is None:
            return

        bestaetigung = messagebox.askyesno(
            "Modul löschen",
            f'Möchtest du das Modul "{modulname}" wirklich löschen?'
        )

        if not bestaetigung:
            return

        self.controller.modul_entfernen(
            ausgewaehltes_semester.nummer,
            modulname
        )

        self.modultabelle_aktualisieren()
        self.dashboard_aktualisieren()

    def starten(self) -> None:
        self.fenster.mainloop()

