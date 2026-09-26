from pruefungsleistung import Pruefungsleistung
from pruefungsart import Pruefungsart
from modul import Modul
from modul_status import ModulStatus

pruefung = Pruefungsleistung(Pruefungsart.KLAUSUR, 1.3)
modul = Modul("E-Health", 5, ModulStatus.BESTANDEN, pruefung)

print(pruefung.pruefungsart.value)
print(pruefung.note)

print(modul.status.value)
print(modul.pruefungsleistung.pruefungsart.value)


