import sqlite3

# ── Connection helper ──────────────────────────────────────

def get_connection():
    """Return a sqlite3 connection with row_factory set for dict-like rows."""
    conn = sqlite3.connect('Weather.db')
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ── Location helpers ───────────────────────────────────────

def get_location_by_id(location_id):
    """Return a location row as a dict, or None if not found."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, latitude, longitude, nickname FROM locations WHERE id = ?",
            (location_id,),
        ).fetchone()
    return dict(row) if row else None


def get_location_by_lat_long(latitude, longitude):
    """Return a location row as a dict, or None if not found."""
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, latitude, longitude, nickname FROM locations WHERE latitude = ? AND longitude = ?",
            (latitude,longitude,),
        ).fetchone()
    return dict(row) if row else None

def get_all_locations():
    """Return all location rows as a list of dicts."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, latitude, longitude, nickname, station, x, y FROM locations"
        ).fetchall()
    return [dict(r) for r in rows]

def add_new_location(latitude, longitude, nickname, station, x, y):
    """Insert new location into table"""
    with get_connection() as conn:
        conn.execute(
            f"INSERT INTO locations (latitude, longitude, nickname, station, x, y) VALUES ({latitude}, {longitude}, '{nickname}', '{station}', {x}, {y})"
        )
    return

# ── Forecast helpers ───────────────────────────────────────

def get_forecast_by_id(forecast_id):
    """Return a forecast row as a dict, or None if not found."""
    with get_connection() as conn:
        row = conn.execute(
            """SELECT id, location_id, forecast_date, temperature, retrieved_date
               FROM forecasts WHERE id = ?""",
            (forecast_id,),
        ).fetchone()
    return dict(row) if row else None


def get_all_forecasts():
    """Return all forecast rows as a list of dicts."""
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT id, location_id, forecast_date, temperature, retrieved_date
               FROM forecasts"""
        ).fetchall()
    return [dict(r) for r in rows]


def get_forecasts_for_location(location_id):
    """Return all forecasts belonging to a given location."""
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT id, location_id, forecast_date, temperature, retrieved_date
               FROM forecasts WHERE location_id = ?""",
            (location_id,),
        ).fetchall()
    return [dict(r) for r in rows]

def get_filtered_forecasts_for_location(location_id, forecast_date):
    """Return filtered forecasts belonging to a given location."""
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT MAX(temperature), MIN(temperature)
               FROM forecasts WHERE location_id = ? AND forecast_date = ?""",
            (location_id, forecast_date,),
        ).fetchall()
    return [dict(r) for r in rows]

def put_forecast(location_id, date, temperature, forecast_date):
    """Insert new forecast into table"""
    with get_connection() as conn:
        conn.execute(
            f"INSERT INTO forecasts (location_id, forecast_date, temperature, retrieved_date) VALUES ({location_id}, '{date}', {temperature}, '{forecast_date}')"
        )
    return
