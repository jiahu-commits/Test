import json
from enum import nonmember

from studiengang import Studiengang
from semester import Semester
from modul import Modul
from pruefungsleistung import Pruefungsleistung

class JsonRepository:
    def speichern(self, aktueller_studiengang: Studiengang, dateipfad: str) -> None:
        datei = open(dateipfad, "w", encoding="utf-8")
        daten = {
            "name": aktueller_studiengang.name,
            "startdatum": aktueller_studiengang.startdatum.isoformat(),
            "gesamt_ects": aktueller_studiengang.gesamt_ects,
            "studiendauer_monate": aktueller_studiengang.studiendauer_monate,
            "zielnote": aktueller_studiengang.zielnote,
            "semester": []
         }

        for aktuelles_semester in aktueller_studiengang.semester:
            semester_daten = {
                "nummer": aktuelles_semester.nummer,
                "module" : []
            }
            for aktuelles_modul in aktuelles_semester.module:
                modul_daten = {
                    "name": aktuelles_modul.name,
                    "ects": aktuelles_modul.ects,
                    "status": aktuelles_modul.status,

                }

                aktuelle_pruefungsleistung = aktuelles_modul.pruefungsleistung

                if aktuelle_pruefungsleistung is not None:
                    modul_daten["pruefungsleistung"] = {
                        "pruefungsart": aktuelle_pruefungsleistung.pruefungsart,
                        "note": aktuelle_pruefungsleistung.note
                    }

                else:
                    modul_daten["pruefungsleistung"] = None

                semester_daten["module"].append(modul_daten)

            daten["semester"].append(semester_daten)

        json.dump(daten, datei, ensure_ascii=False, indent=4)
        datei.close()


def laden(self, dateipfad: str) -> Studiengang:
    datei = open(dateipfad, "r", encoding="utf-8")
    daten = json.load(datei)
    datei.close()
    geladener_studiengang = Studiengang(

