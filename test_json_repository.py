from datetime import date

from studiengang import Studiengang
from semester import Semester
from modul import Modul
from pruefungsleistung import Pruefungsleistung
from json_repository import JsonRepository
from modul_status import ModulStatus
from pruefungsart import Pruefungsart


pruefung = Pruefungsleistung(Pruefungsart.KLAUSUR, 1.3)


modul = Modul("E-Health", 5, ModulStatus.BESTANDEN, pruefung)
modul_ohne_pruefung = Modul("Programmieren mit Python", 5, ModulStatus.BESTANDEN, pruefung)


semester = Semester(1)
semester.modul_hinzufuegen(modul)
semester.modul_hinzufuegen(modul_ohne_pruefung)

studiengang = Studiengang(
    "Medizinische Informatik",
    date(2026, 7, 30),
    180,
    48,
    2.0
)
studiengang.semester_hinzufuegen(semester)

repository = JsonRepository()
repository.speichern(studiengang, "studiendaten.json")

geladener_studiengang = repository.laden("studiendaten.json")
print(geladener_studiengang.name)
print(geladener_studiengang.semester[0].nummer)
print(geladener_studiengang.semester[0].module[0].name)
print(geladener_studiengang.semester[0].module[0].pruefungsleistung.pruefungsart.value)
print(geladener_studiengang.semester[0].module[0].pruefungsleistung.note)

print(geladener_studiengang.semester[0].module[1].name)
print(geladener_studiengang.semester[0].module[1].pruefungsleistung.pruefungsart.value)


