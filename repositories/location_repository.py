from db.run_sql import run_sql

from models.country import Country
from models.vu_point import Vu_point
from models.location import Location

import repositories.country_repository as country_repository

def save(location): # working
    sql = "INSERT INTO locations (name, country_id) VALUES (%s, %s) RETURNING *"
    values = [location.name, location.country.id]
    results = run_sql(sql, values)
    location.id = results[0]['id'] # giving the location object an id based on the id given by the database, as the location class has an id of its own (separate from database), but this line makes them the same
    return location


def select_all(): # working
    locations = []
    sql = "SELECT * FROM locations"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        location = Location(row['name'], country, row['id'])
        locations.append(location)
    return locations


def select(id): # working
    locations = None
    sql = "SELECT * FROM locations WHERE id = (%s)"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repository.select(result['country_id'])
        location = Location(result['name'], country, result['id'])
    return location


def delete_all(): # working
    sql = "DELETE FROM locations"
    run_sql(sql)


def delete(id): # working
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(location): # working
    sql = "UPDATE locations SET (name, country_id) = (%s, %s) WHERE id = %s"
    values = [location.name, location.country.id, location.id]
    run_sql(sql, values)