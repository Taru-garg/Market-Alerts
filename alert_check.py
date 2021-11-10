from market import pricepull
from src.alert import Alert
from src.alert_utils import read_alerts

def process_alerts():
    alerts = read_alerts()
    for alert in alerts:
        check_alert(alert)

# implementation must be changed fetching price again and again is not good
# since a get request takes a lot of time. A function that will first see which
# alerts are to be executed should be implemented.

def check_alert(alert : Alert) -> None:
    price_acutal = pricepull.pull(alert.marketName)
    if alert.triggerReason == 'above' and price_acutal > float(alert.price):
        alert.send_alert()
    elif alert.triggerReason == 'below' and price_acutal < float(alert.price):
        alert.send_alert()

process_alerts()