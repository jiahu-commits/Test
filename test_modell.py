from datetime import date
from studiengang import Studiengang
from semester import Semester
from modul import Modul
from pruefungsleistung import Pruefungsleistung


prüfung = Pruefungsleistung("Klausur", 1.3)
modul = Modul("E-Health", 5, "Bestanden", prüfung)
semester = Semester(1)
semester.modul_hinzufuegen(modul)
studiengang = Studiengang("Medizinische Informatik", date(2026, 7, 30), 180, 48, 2.0)
studiengang.semester_hinzufuegen(semester)

print(studiengang.semester[0].module[0].pruefungsleistung.note)
print(studiengang.semester[0].module[0].name)