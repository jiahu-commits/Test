from dataclasses import dataclass
from pruefungsleistung import Pruefungsleistung

@dataclass
class Modul:
    name: str
    ects: int
    status: str
    pruefungsleistung: Pruefungsleistung| None = None

    def status_aendern(self, neuer_status: str) -> None:
        self.status = neuer_status