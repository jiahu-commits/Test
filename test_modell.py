from datetime import date

from json_repository import JsonRepository
from studiengang import Studiengang
from semester import Semester
from modul import Modul
from pruefungsleistung import Pruefungsleistung
from pruefungsart import Pruefungsart
from modul_status import ModulStatus
from studienfortschritt_service import StudienfortschrittService
from dashboard_controller import DashboardController
from dashboard_application import DashboardApplication

pruefung = Pruefungsleistung(Pruefungsart.KLAUSUR, 1.3)
modul = Modul("E-Health", 5, ModulStatus.BESTANDEN, pruefung)
semester = Semester(1)
semester.modul_hinzufuegen(modul)
studiengang = Studiengang("Medizinische Informatik", date(2026, 7, 30), 180, 48, 2.0)
studiengang.semester_hinzufuegen(semester)

service = StudienfortschrittService()
repository = JsonRepository()

controller = DashboardController(studiengang, service, repository)

