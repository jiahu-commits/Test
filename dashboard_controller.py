from studiengang import Studiengang
from semester import Semester
from modul import Modul
from modul_status import ModulStatus
from pruefungsleistung import Pruefungsleistung
from pruefungsart import Pruefungsart
from studienfortschritt_service import StudienfortschrittService
from json_repository import JsonRepository

class DashboardController:
    def __init__(
            self,
            aktueller_studiengang: Studiengang,
            service: StudienfortschrittService,
            repository: JsonRepository,
            dateipfad: str = "studiendaten.json"
    ) -> None:
        self.aktueller_studiengang = aktueller_studiengang
        self.service = service
        self.repository = repository
        self.dateipfad = dateipfad

    def _finde_semester(self, semester_nummer: int) -> Semester | None:
        for aktuelles_semester in self.aktueller_studiengang.semester:
            if aktuelles_semester.nummer == semester_nummer:
                return aktuelles_semester

        return None

    def _finde_modul(self, semester_nummer: int, modul_name: str) -> Modul | None:
        gefundenes_semester = self._finde_semester(semester_nummer)

        if gefundenes_semester is None:
            return None

        for aktuelles_modul in gefundenes_semester.module:
            if aktuelles_modul.name == modul_name:
                return aktuelles_modul

        return None

    def semester_hinzufuegen(self, nummer: int) -> None:
        neues_semester = Semester(nummer)
        self.aktueller_studiengang.semester_hinzufuegen(neues_semester)
        self.repository.speichern(self.aktueller_studiengang, self.dateipfad)

    def semester_entfernen(self, semester_nummer: int) -> None:
        gefundenes_semester = self._finde_semester(semester_nummer)

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
            ects: str,
            status: str,
            pruefungsart: str,
            note: str
    ) -> None:

        gefundenes_semester = self._finde_semester(semester_nummer)

        if gefundenes_semester is None:
            return

        bereits_vorhandenes_modul = self._finde_modul(
            semester_nummer,
            name
        )

        if bereits_vorhandenes_modul is not None:
            raise ValueError ("Dieses Modul existiert in diesem Semester bereits.")

        ects_wert = int(ects)
        neuer_status = ModulStatus(status)

        if note:
            try:
                neue_note = float(note)
            except ValueError:
                raise ValueError("Bitte gib eine gültige Note ein.")
        else:
            neue_note = None

        if pruefungsart:
            neue_pruefungsart = Pruefungsart(pruefungsart)

            neue_pruefungsleistung = Pruefungsleistung(
                neue_pruefungsart,
                neue_note
            )
        else:
            neue_pruefungsleistung = None

        neues_modul = Modul(
            name,
            ects_wert,
            neuer_status,
            neue_pruefungsleistung
        )

        gefundenes_semester.modul_hinzufuegen(neues_modul)
        self.repository.speichern(self.aktueller_studiengang,self.dateipfad)

    def modul_entfernen(self, semester_nummer: int, modul_name: str) -> None:
        gefundenes_semester = self._finde_semester(semester_nummer)

        if gefundenes_semester is None:
            return

        gefundenes_modul = self._finde_modul(semester_nummer, modul_name)

        if gefundenes_modul is None:
            return

        gefundenes_semester.modul_entfernen(gefundenes_modul)
        self.repository.speichern(self.aktueller_studiengang, self.dateipfad)

    def modul_bearbeiten(
            self,
            semester_nummer: int,
            modul_name: str,
            neuer_status: str,
            neue_note: str
    ) -> None:

        gefundenes_modul = self._finde_modul(
            semester_nummer,
            modul_name
        )

        if gefundenes_modul is None:
            return

        status_wert = ModulStatus(neuer_status)

        if neue_note:
            try:
                note_wert = float(neue_note)
            except ValueError:
                raise ValueError(
                    "Bitte gib eine gültige Note ein."
                )
        else:
            note_wert = None

        gefundenes_modul.status = status_wert

        if gefundenes_modul.pruefungsleistung is not None:

            if status_wert == ModulStatus.BESTANDEN:
                gefundenes_modul.pruefungsleistung.note = note_wert
            else:
                gefundenes_modul.pruefungsleistung.note = None

        self.repository.speichern(self.aktueller_studiengang,self.dateipfad)

    def semester_abrufen(self) -> list[Semester]:
        return self.aktueller_studiengang.semester

    def module_abrufen(self, semester_nummer: int) -> list[Modul]:
        gefundenes_semester = self._finde_semester(semester_nummer)

        if gefundenes_semester is None:
            return []

        return gefundenes_semester.module

    def kennzahlen_abrufen(self) -> dict:
        erreichte_ects = self.service.berechne_erreichte_ects(self.aktueller_studiengang)
        ects_fortschritt = self.service.berechne_ects_fortschritt(self.aktueller_studiengang)
        notendurchschnitt = self.service.berechne_notendurchschnitt(self.aktueller_studiengang)
        vergangene_monate = self.service.berechne_vergangene_monate(self.aktueller_studiengang)
        zeitfortschritt = self.service.berechne_zeitfortschritt(self.aktueller_studiengang)
        soll_ects = self.service.berechne_soll_ects(self.aktueller_studiengang)
        ects_soll_ist_abweichung = self.service.berechne_soll_ist_abweichung(self.aktueller_studiengang)
        notenabweichung = self.service.berechne_notenabweichung(self.aktueller_studiengang)

        return {
            "erreichte_ects": erreichte_ects,
            "ects_fortschritt": ects_fortschritt,
            "notendurchschnitt": notendurchschnitt,
            "vergangene_monate": vergangene_monate,
            "zeitfortschritt": zeitfortschritt,
            "soll_ects": soll_ects,
            "ects_soll_ist_abweichung": ects_soll_ist_abweichung,
            "notenabweichung": notenabweichung,
            "gesamt_ects": self.aktueller_studiengang.gesamt_ects,
            "studiendauer_monate": self.aktueller_studiengang.studiendauer_monate,
            "zielnote": self.aktueller_studiengang.zielnote
        }