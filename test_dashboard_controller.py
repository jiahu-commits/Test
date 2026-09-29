from datetime import date

from studiengang import Studiengang
from pruefungsleistung import Pruefungsleistung
from pruefungsart import Pruefungsart
from modul_status import ModulStatus
from dashboard_controller import DashboardController
from studienfortschritt_service import StudienfortschrittService
from json_repository import JsonRepository

studiengang = Studiengang(
    "Medizinische Informatik",
    date(2026, 7, 30),
    180,
    48,
    2.0
)

service = StudienfortschrittService()
repository = JsonRepository()

controller = DashboardController(studiengang,service,repository)

controller.semester_hinzufuegen(1)
print(controller.semester_abrufen())

pruefung = Pruefungsleistung(
    Pruefungsart.KLAUSUR,
    1.3
)

controller.modul_hinzufuegen(
    1,
    "E-Health",
    5,
    ModulStatus.BESTANDEN,
    pruefung
)

print(controller.semester_abrufen())


print(controller.module_abrufen(1))

controller.note_eintragen(
    1,
    "E-Health", 1)
print(controller.module_abrufen(1)[0].pruefungsleistung.note)

print(controller.kennzahlen_abrufen())



