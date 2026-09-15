from dataclasses import dataclass

@dataclass
class Pruefungsleistung:
    pruefungsart: str
    note: float | None = None