DROP TABLE vu_points;
DROP TABLE countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255), 
    capital VARCHAR(255),
    continent VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE vu_points (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    rating INT,
    description TEXT, 
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);