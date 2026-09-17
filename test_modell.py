from datetime import date
from studiengang import Studiengang
from semester import Semester
from modul import Modul
from pruefungsleistung import Pruefungsleistung
from studienfortschritt_service import StudienfortschrittService

pruefung = Pruefungsleistung("Klausur", 1.3)
modul = Modul("E-Health", 5, "Bestanden", pruefung)
semester = Semester(1)
semester.modul_hinzufuegen(modul)
studiengang = Studiengang("Medizinische Informatik", date(2026, 7, 30), 180, 48, 2.0)
studiengang.semester_hinzufuegen(semester)

service = StudienfortschrittService()

print(service.berechne_erreichte_ects(studiengang))
print(service.berechne_notendurchschnitt(studiengang))

print(studiengang.semester[0].module[0].pruefungsleistung.note)
print(studiengang.semester[0].module[0].name)
print(service.berechne_ects_fortschritt(studiengang))
print(service.berechne_vergangene_monate(studiengang))