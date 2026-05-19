# Forecast App

This project includes a dockerized application that exposes an API to retrieve forecasts for a given latitude/longitude. This project also contains scripts to initialize a local database and retrieve forecasts on a schedule. 

# Architecture

The project uses a sql database with two tables defined in schema.sql. The first table is `Locations` and maps a latitude/longitude pair to metadata from weather.gov. The second table is `Forecasts` and stores hourly forecast data for each location. 

A flask application, app.py, provides the following endpoints:

```
GET /locations/<location_id>
GET /locations
POST /locations
GET /forecasts/<forecast_id>
GET /forecasts
GET /forecasts?latitude=X&longitude=Y&date=YYYY-MM-DD&hour=HH
GET /locations/<location_id>/forecasts
```

There are two standalone support scripts. retrieve_forecasts.py queries weather.gov for each location in the Locations database and saves forecast data. The retrieve forecasts script is intended to be executed via a cron (ie. on the server with the flask application or in a Lambda). init_db.py initializes a local sql database if the Weather.db file is removed.

weather_gov_api.py wraps the weather.gov API. database.py wraps the SQL database queries.

Note: in this example, the flask application, cron, and database are built into the same docker container. However, in an actual deployed environment, the database would be deployed to a standalone cloud database, the flask application would be on a server, and the cron script could be either on the server or running independently on a lambda.

## Building and Running in a Docker container

```
// Build the docker container
docker build -t forecasts .
// Start the docker container
docker run -p 5000:5000 forecasts
```

## Cron setup
`0 * * * * python retrieve_forecasts.py >> /var/log/cron.log 2>&1`

## Running Locally

```
// install dependencies
pip install -r requirements.txt
// initalize database
python init_db.py
// fetch forecasts
retrieve_forecasts.py
// Start flask app
python app.py
```

## Sample Curl Calls

* Add a new location: 
```curl http://127.0.0.1:5000/locations --json '{"latitude": 40.440624, "longitude": -79.995888}'```

* Retrieve forecast min/max based on lat, long, date, and hour:
```curl 'http://127.0.0.1:5000/forecasts?latitude=47.6061&longitude=-122.3328&date=2026-05-19&hour=22'```


## TODO:
* Add logging and error handling
* Run cron job in docker container
