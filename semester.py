from dataclasses import dataclass, field
from modul import Modul

@dataclass
class Semester:
    nummer: int
    module: list[Modul] = field(default_factory=list)

    def modul_hizufuegen(self, modul: Modul) -> None:
        self.module.append(modul)
