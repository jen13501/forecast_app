DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS forecasts;

CREATE TABLE IF NOT EXISTS locations (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude  REAL    NOT NULL,
    longitude REAL    NOT NULL,
    nickname  TEXT,
    station   TEXT,
    x         INTEGER NOT NULL,
    y         INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS forecasts (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id   INTEGER NOT NULL
                        REFERENCES locations(id)
                        ON DELETE CASCADE,
    forecast_date TIMESTAMP NOT NULL,
    temperature   REAL    NOT NULL,
    retrieved_date TIMESTAMP NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_forecasts_location_id
                ON forecasts(location_id);

-- Initialize with two locations
INSERT INTO locations (latitude, longitude, nickname, station, x, y) VALUES (39.7456, -97.0892, "Kansas", "TOP", 32, 81);
INSERT INTO locations (latitude, longitude, nickname, station, x, y) VALUES (47.6061, -122.3328, "Seattle", "SEW", 125, 68);
