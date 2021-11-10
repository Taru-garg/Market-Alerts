import os
from .alert import Alert


def read_alerts(folderpath: str = "alerts/") -> list[Alert]:
    alert_files = [_.path for _ in os.scandir(r".\alerts")]
    alerts = []
    for alert in alert_files:
        try:
            alerts.append(Alert(alert))
        except:
            continue
    return alerts
