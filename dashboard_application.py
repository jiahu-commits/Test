from studiengang import Studiengang
from studienfortschritt_service import StudienfortschrittService
from json_repository import JsonRepository
from dashboard_controller import DashboardController


class DashboardApplication:
    def __init__(self, aktueller_studiengang: Studiengang) -> None:
        self.service = StudienfortschrittService()
        self.repository = JsonRepository()

        self.controller = DashboardController(
            aktueller_studiengang,
            self.service,
            self.repository
        )
