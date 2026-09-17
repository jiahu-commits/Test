from studiengang import Studiengang
from datetime import date

class StudienfortschrittService:
    def berechne_erreichte_ects(self, aktueller_studiengang: Studiengang) -> int:
        erreichte_ects = 0

        for aktuelles_semester in aktueller_studiengang.semester:
            for aktuelles_modul in aktuelles_semester.module:
                if aktuelles_modul.status == "Bestanden":
                    erreichte_ects += aktuelles_modul.ects

        return erreichte_ects

    def berechne_notendurchschnitt(self, aktueller_studiengang: Studiengang) -> float | None:
        noten: list[float] = []

        for aktuelles_semester in aktueller_studiengang.semester:
            for aktuelles_modul in aktuelles_semester.module:
                if aktuelles_modul.pruefungsleistung is not None:
                    if aktuelles_modul.pruefungsleistung.note is not None:
                        noten.append(aktuelles_modul.pruefungsleistung.note)

        if not noten:
            return None

        return sum(noten) / len(noten)

    def berechne_ects_fortschritt(self, aktueller_studiengang: Studiengang) -> float:
        erreichte_ects = self.berechne_erreichte_ects(aktueller_studiengang)

        if aktueller_studiengang.gesamt_ects == 0:
            return 0.0

        return erreichte_ects / aktueller_studiengang.gesamt_ects * 100

    def berechne_vergangene_monate(self, aktueller_studiengang: Studiengang) -> int:
        heutiges_datum = date.today()
        vergangene_monate = (heutiges_datum.year - aktueller_studiengang.startdatum.year) * 12
        vergangene_monate += heutiges_datum.month - aktueller_studiengang.startdatum.month

        if heutiges_datum.day < aktueller_studiengang.startdatum.day:
            vergangene_monate -= 1

        return vergangene_monate

    def berechne_zeitfortschritt(self, aktueller_studiengang: Studiengang) -> float:
        vergangene_monate = self.berechne_vergangene_monate(aktueller_studiengang)

        if aktueller_studiengang.studiendauer_monate == 0:
            return 0.0

        return vergangene_monate / aktueller_studiengang.studiendauer_monate * 100

