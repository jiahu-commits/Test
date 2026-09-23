from dataclasses import dataclass
from pruefungsleistung import Pruefungsleistung
from modul_status import ModulStatus

@dataclass
class Modul:
    name: str
    ects: int
    _status: ModulStatus
    pruefungsleistung: Pruefungsleistung | None = None

    def __post_init__(self) -> None:
        self.status = self._status

    @property
    def status(self) -> ModulStatus:
        return self._status

    @status.setter
    def status(self, neuer_status: ModulStatus) -> None:
        if not isinstance(neuer_status, ModulStatus):
            raise ValueError("Ungültiger Modulstatus")

        self._status = neuer_status





