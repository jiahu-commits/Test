from dataclasses import dataclass
from pruefungsart import Pruefungsart

@dataclass
class Pruefungsleistung:
    _pruefungsart: Pruefungsart
    _note: float | None = None

    def __post_init__(self) -> None:
        self.pruefungsart = self._pruefungsart
        self.note = self._note


    @property
    def pruefungsart(self) -> Pruefungsart:
        return self._pruefungsart

    @pruefungsart.setter
    def pruefungsart(self, neue_pruefungsart: Pruefungsart) -> None:
        if not isinstance(neue_pruefungsart, Pruefungsart):
            raise ValueError ("Ungültige Prüfungsart")

        self._pruefungsart = neue_pruefungsart

    @property
    def note(self) -> float | None:
        return self._note

    @note.setter
    def note(self, neue_note: float | None) -> None:
        if neue_note is not None:
            if not isinstance(neue_note, (int, float)):
                raise ValueError("Die Note muss eine Zahl sein.")

            if not 1.0 <= neue_note <= 5.0:
                raise ValueError(
                    "Die Note muss zwischen 1.0 und 5.0 liegen."
                )

        self._note = neue_note

