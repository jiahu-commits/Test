from studiengang import Studiengang
from studienfortschritt_service import StudienfortschrittService
from json_repository import JsonRepository
from dashboard_controller import DashboardController
from dashboard_view import DashboardView


class DashboardApplication:
    def __init__(self, aktueller_studiengang: Studiengang) -> None:
        self.service = StudienfortschrittService()
        self.repository = JsonRepository()

        try:
            aktueller_studiengang = self.repository.laden(
                "studiendaten.json"
            )
        except FileNotFoundError:
            pass

        self.controller = DashboardController(
            aktueller_studiengang,
            self.service,
            self.repository
        )

        self.view = DashboardView(self.controller)

    def starten(self)->None:
        self.view.starten()
