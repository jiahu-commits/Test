from dataclasses import dataclass, field
from datetime import date
from semester import Semester

@dataclass
class Studiengang:
    name: str
    startdatum: date
    gesamt_ects: int
    studiendauer_monate: int
    zielnote: float
    semester: list[Semester] = field(default_factory=list)

    def semester_hinzufuegen(self, neues_semester: Semester) -> None:
        self.semester.append(neues_semester)

    def semester_entfernen(self, zu_entfernendes_semester: Semester) -> None:
        self.semester.remove(zu_entfernendes_semester)