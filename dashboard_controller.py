from studiengang import Studiengang
from semester import Semester
from modul import Modul
from modul_status import ModulStatus
from pruefungsleistung import Pruefungsleistung
from studienfortschritt_service import StudienfortschrittService
from json_repository import JsonRepository

class DashboardController:
    def __init__(self, aktueller_studiengang: Studiengang, dateipfad: str = "studiendaten.json") -> None:
        self.aktueller_studiengang = aktueller_studiengang
        self.dateipfad = dateipfad
        self.service = StudienfortschrittService()
        self.repository = JsonRepository()

    def semester_hinzufuegen(self, nummer: int) -> None:
        neues_semester = Semester(nummer)
        self.aktueller_studiengang.semester_hinzufuegen(neues_semester)
        self.repository.speichern(self.aktueller_studiengang, self.dateipfad)

    def semester_entfernen(self, semester_nummer: int) -> None:
        gefundenes_semester = None

        for aktuelles_semester in self.aktueller_studiengang.semester:
            if aktuelles_semester.nummer == semester_nummer:
                gefundenes_semester = aktuelles_semester
                break

        if gefundenes_semester is None:
            return

        if gefundenes_semester.module:
            return

        self.aktueller_studiengang.semester_entfernen(gefundenes_semester)
        self.repository.speichern(self.aktueller_studiengang, self.dateipfad)


    def modul_hinzufuegen(
            self,
            semester_nummer: int,
            name: str,
            ects: int,
            status: ModulStatus,
            pruefungsleistung: Pruefungsleistung | None = None
    ) -> None:

        gefundenes_semester = None
        for aktuelles_semester in self.aktueller_studiengang.semester:
            if aktuelles_semester.nummer == semester_nummer:
                gefundenes_semester = aktuelles_semester
                break

        if gefundenes_semester is None:
            return

        neues_modul = Modul(name, ects, status, pruefungsleistung)
        gefundenes_semester.modul_hinzufuegen(neues_modul)
        self.repository.speichern(self.aktueller_studiengang, self.dateipfad)

    def modul_loeschen(self, semester_nummer: int, modul_name: str) -> None:
        gefundenes_semester = None

        for aktuelles_semester in self.aktueller_studiengang.semester:
            if aktuelles_semester.nummer == semester_nummer:
                gefundenes_semester = aktuelles_semester
                break

        if gefundenes_semester is None:
            return

        gefundenes_modul = None

        for aktuelles_modul in gefundenes_semester.module:
            if aktuelles_modul.name == modul_name:
                gefundenes_modul = aktuelles_modul
                break

        if gefundenes_modul is None:
            return

        gefundenes_semester.modul_entfernen(gefundenes_modul)
        self.repository.speichern(self.aktueller_studiengang, self.dateipfad)

    def _finde_modul(self, semester_nummer: int, modul_name: str) -> Modul | None:
        for aktuelles_semester in self.aktueller_studiengang.semester:
            if aktuelles_semester.nummer == semester_nummer:
                for aktuelles_modul in aktuelles_semester.module:
                    if aktuelles_modul.name == modul_name:
                        return aktuelles_modul

        return None

    def status_aendern(self, semester_nummer: int, modul_name: str, neuer_status: ModulStatus) -> None:
        gefundenes_modul = self._finde_modul(semester_nummer, modul_name)

        if gefundenes_modul is None:
            return

        gefundenes_modul.status = neuer_status
        self.repository.speichern(self.aktueller_studiengang, self.dateipfad)

    def note_eintragen(self, semester_nummer: int, modul_name: str, neue_note: float) -> None:
        gefundenes_modul = self._finde_modul(semester_nummer, modul_name)
        if gefundenes_modul is None:
            return
        if gefundenes_modul.pruefungsleistung is None:
            return

        gefundenes_modul.pruefungsleistung.note = neue_note
        self.repository.speichern(self.aktueller_studiengang, self.dateipfad)
