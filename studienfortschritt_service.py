from studiengang import Studiengang

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


