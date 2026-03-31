import requests
import json
from datetime import datetime, timezone

API_KEY = "8cde0b2e-7401-4dc8-a568-1e9bb593a09c"
STOP_ID = "53546"

url = f"http://api.511.org/transit/StopMonitoring?api_key={API_KEY}&agency=AC&stopcode={STOP_ID}&format=json"

response = requests.get(url)
data = json.loads(response.content.decode('utf-8-sig'))

buses = data["ServiceDelivery"]["StopMonitoringDelivery"]["MonitoredStopVisit"]

print(f"Next {len(buses)} buses at your stop:\n")

for bus in buses:
    call = bus["MonitoredVehicleJourney"]["MonitoredCall"]
    arrival_str = call["ExpectedArrivalTime"]
    
    arrival_utc = datetime.fromisoformat(arrival_str.replace("Z", "+00:00"))
    arrival_local = arrival_utc.astimezone()
    minutes_away = (arrival_utc - datetime.now(timezone.utc)).seconds // 60
    
    print(f"Route 6 → arriving in {minutes_away} minutes ({arrival_local.strftime('%I:%M %p')})")