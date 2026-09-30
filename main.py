from datetime import date

from studiengang import Studiengang
from dashboard_application import DashboardApplication

studiengang = Studiengang(
    "Medizinische Informatik",
    date(2026, 7, 30),
    180,
    48,
    2.0
)
app = DashboardApplication(studiengang)
app.starten()