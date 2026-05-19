import database as db
from datetime import datetime, timezone
import weather_gov_api

def parse_data(loc_id, data):
    for index, period in enumerate(data['properties']['periods']):
        if index > 72:
            break
        date = datetime.strptime(period['startTime'], "%Y-%m-%dT%H:%M:%S%z")
        forecast_date = date.astimezone(timezone.utc).replace(tzinfo=None)
        temperature = period['temperature']
        retrieved_date = datetime.now()

        db.put_forecast(loc_id, forecast_date, temperature, retrieved_date)

    return

def main():
    locations = db.get_all_locations()
    for loc in locations:
        print(f"Getting forecast for: {loc}")
        r = weather_gov_api.get_forecast_for_location(loc['station'], loc['x'], loc['y'])

        parse_data(loc['id'], r)

if __name__=="__main__":
    main()
