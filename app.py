from flask import Flask, jsonify, abort, request
import database as db
import weather_gov_api
import datetime

app = Flask(__name__)

# ── Locations ──────────────────────────────────────────────

@app.route("/locations/<int:location_id>", methods=["GET"])
def get_location(location_id):
    """Return a single location by its primary-key id."""
    location = db.get_location_by_id(location_id)
    if location is None:
        abort(404, description=f"Location {location_id} not found.")
    return jsonify(location)


@app.route("/locations", methods=["GET"])
def list_locations():
    """Return all locations."""
    return jsonify(db.get_all_locations())

@app.route("/locations", methods=["POST"])
def post_location():
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']

    (station, x, y, name) = weather_gov_api.get_location_by_lat_long(latitude, longitude)

    if "nickname" in data:
        nickname = data['nickname']
    else:
        nickname = name

    db.add_new_location(latitude, longitude, nickname, station, x, y)
    return {"message": "Added location"}, 201

# ── Forecasts ──────────────────────────────────────────────

@app.route("/forecasts/<int:forecast_id>", methods=["GET"])
def get_forecast(forecast_id):
    """Return a single forecast by its primary-key id."""
    forecast = db.get_forecast_by_id(forecast_id)
    if forecast is None:
        abort(404, description=f"Forecast {forecast_id} not found.")
    return jsonify(forecast)


@app.route("/forecasts", methods=["GET"])
def list_forecasts():
    if not request.args:
        """Return all forecasts."""
        return jsonify(db.get_all_forecasts())

    """Return queried forecasts."""
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)
    date = request.args.get('date')
    hour = request.args.get('hour', type=int)

    if latitude == None or longitude == None or date == None or hour == None:
        return jsonify({"error": "Latitude, Longitude, date, and hour are all required query parameters"}), 400

    # get location
    location = db.get_location_by_lat_long(latitude, longitude)
    if location == None:
        return jsonify({"error": "Latitude, Longitude is not a tracked location"}), 400

    # get forecast for that time
    date_string = f"{date} {hour}"
    forecast_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H")
    return jsonify(db.get_filtered_forecasts_for_location(location['id'], forecast_date))


@app.route("/locations/<int:location_id>/forecasts", methods=["GET"])
def get_forecasts_for_location(location_id):
    """Return all forecasts belonging to a given location."""
    if db.get_location_by_id(location_id) is None:
        abort(404, description=f"Location {location_id} not found.")
    return jsonify(db.get_forecasts_for_location(location_id))


# ── Error handlers ─────────────────────────────────────────

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error.description)}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error.description)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
