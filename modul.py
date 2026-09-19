from dataclasses import dataclass
from pruefungsleistung import Pruefungsleistung

@dataclass
class Modul:
    name: str
    ects: int
    status: str
    pruefungsleistung: Pruefungsleistung| None = None