import requests
import json
from datetime import datetime, timezone
from flask import Flask

app = Flask(__name__)

API_KEY = "8cde0b2e-7401-4dc8-a568-1e9bb593a09c"
STOP_ID = "53546"

@app.route("/bus")
def get_bus():
    url = f"http://api.511.org/transit/StopMonitoring?api_key={API_KEY}&agency=AC&stopcode={STOP_ID}&format=json"
    response = requests.get(url)
    data = json.loads(response.content.decode('utf-8-sig'))
    
    buses = data["ServiceDelivery"]["StopMonitoringDelivery"]["MonitoredStopVisit"]
    first_bus = buses[0]["MonitoredVehicleJourney"]["MonitoredCall"]
    arrival_str = first_bus["ExpectedArrivalTime"]
    
    arrival_utc = datetime.fromisoformat(arrival_str.replace("Z", "+00:00"))
    minutes_away = (arrival_utc - datetime.now(timezone.utc)).seconds // 60
    
    return f"Your Route 6 bus arrives in {minutes_away} minutes."

if __name__ == "__main__":
    app.run()