import json
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
