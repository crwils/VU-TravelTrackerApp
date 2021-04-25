DROP TABLE vu_points;
DROP TABLE locations;
DROP TABLE countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE vu_points (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    rating INT,
    description TEXT, 
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    location_id INT REFERENCES locations(id) ON DELETE CASCADE
);