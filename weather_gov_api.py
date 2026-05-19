import requests

WEATHER_URL = "https://api.weather.gov"

def get_forecast_for_location(station, x, y):
    response = requests.get(f"{WEATHER_URL}/gridpoints/{station}/{x},{y}/forecast/hourly?units=us",
                    headers={'accept': 'application/geo+json'})
    
    # TODO: add error handling
    
    return response.json()

def get_location_by_lat_long(lat, long):
    response = requests.get(f"{WEATHER_URL}/points/{lat},{long}",
                    headers={'accept': 'application/geo+json'})
    
    # TODO: add error handling
    
    json = response.json()

    props = json["properties"]
    name = props['relativeLocation']['properties']['city']
    
    return (props['gridId'], props['gridX'], props['gridY'], name)


{
  "@context": [
    "https://geojson.org/geojson-ld/geojson-context.jsonld",
    {
      "@version": "1.1",
      "wx": "https://api.weather.gov/ontology#",
      "s": "https://schema.org/",
      "geo": "http://www.opengis.net/ont/geosparql#",
      "unit": "http://codes.wmo.int/common/unit/",
      "@vocab": "https://api.weather.gov/ontology#",
      "geometry": {
        "@id": "s:GeoCoordinates",
        "@type": "geo:wktLiteral"
      },
      "city": "s:addressLocality",
      "state": "s:addressRegion",
      "distance": {
        "@id": "s:Distance",
        "@type": "s:QuantitativeValue"
      },
      "bearing": {
        "@type": "s:QuantitativeValue"
      },
      "value": {
        "@id": "s:value"
      },
      "unitCode": {
        "@id": "s:unitCode",
        "@type": "@id"
      },
      "forecastOffice": {
        "@type": "@id"
      },
      "forecastGridData": {
        "@type": "@id"
      },
      "publicZone": {
        "@type": "@id"
      },
      "county": {
        "@type": "@id"
      }
    }
  ],
  "id": "https://api.weather.gov/points/47.6061,-122.3328",
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      -122.3328,
      47.6061
    ]
  },
  "properties": {
    "@id": "https://api.weather.gov/points/47.6061,-122.3328",
    "@type": "wx:Point",
    "cwa": "SEW",
    "type": "land",
    "forecastOffice": "https://api.weather.gov/offices/SEW",
    "gridId": "SEW",
    "gridX": 125,
    "gridY": 68,
    "forecast": "https://api.weather.gov/gridpoints/SEW/125,68/forecast",
    "forecastHourly": "https://api.weather.gov/gridpoints/SEW/125,68/forecast/hourly",
    "forecastGridData": "https://api.weather.gov/gridpoints/SEW/125,68",
    "observationStations": "https://api.weather.gov/gridpoints/SEW/125,68/stations",
    "relativeLocation": {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -122.350876,
          47.620499
        ]
      },
      "properties": {
        "city": "Seattle",
        "state": "WA",
        "distance": {
          "unitCode": "wmoUnit:m",
          "value": 2097.493676173
        },
        "bearing": {
          "unitCode": "wmoUnit:degree_(angle)",
          "value": 139
        }
      }
    },
    "forecastZone": "https://api.weather.gov/zones/forecast/WAZ315",
    "county": "https://api.weather.gov/zones/county/WAC033",
    "fireWeatherZone": "https://api.weather.gov/zones/fire/WAZ654",
    "timeZone": "America/Los_Angeles",
    "radarStation": "KATX",
    "astronomicalData": {
      "sunrise": "2026-05-18T05:25:54-07:00",
      "sunset": "2026-05-18T20:45:40-07:00",
      "transit": "2026-05-18T13:05:47-07:00",
      "civilTwilightBegin": "2026-05-18T04:50:29-07:00",
      "civilTwilightEnd": "2026-05-18T21:21:05-07:00",
      "nauticalTwilightBegin": "2026-05-18T04:01:44-07:00",
      "nauticalTwilightEnd": "2026-05-18T22:09:51-07:00",
      "astronomicalTwilightBegin": "2026-05-18T02:59:48-07:00",
      "astronomicalTwilightEnd": "2026-05-18T23:11:46-07:00"
    },
    "nwr": {
      "transmitter": "KHB60",
      "sameCode": "053033",
      "areaBroadcast": "https://api.weather.gov/radio/KHB60/broadcast",
      "pointBroadcast": "https://api.weather.gov/points/47.6061,-122.3328/radio"
    }
  }
}