from dataclasses import dataclass, field
from modul import Modul

@dataclass
class Semester:
    nummer: int
    module: list[Modul] = field(default_factory=list)

    def modul_hinzufuegen(self, neues_modul: Modul) -> None:
        self.module.append(neues_modul)

    def modul_entfernen(self, zu_entfernendes_modul: Modul) -> None:
        self.module.remove(zu_entfernendes_modul)


