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

    def semester_hinzufuegen(self, semester: Semester) -> None:
        self.semester.append(semester)