from dataclasses import dataclass

@dataclass
class Pruefungsleistung:
    pruefungsart: str
    note: float | None = None

    def note_eintragen(self, neue_note: float) -> None:
        self.note = neue_note