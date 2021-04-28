from db.run_sql import run_sql

from models.country import Country
from models.vu_point import Vu_point
from models.location import Location

import repositories.vu_point_repository as vu_point_repository
import repositories.location_repository as location_repository


def save(country):  # working
    sql = "INSERT INTO countries (name, visited) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.visited]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country


def select_all():  # working
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        # taking entries from database and attaching to a new country instance (arguments based on class parameters)
        country = Country(row['name'], row['visited'], row['id'])
        countries.append(country)
    return countries


def select(id):  # working
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = Country(result['name'], result['visited'], result['id'])
    return country


def delete_all():  # working
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):  # working
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):  # working
    sql = "UPDATE countries SET (name, visited) = (%s, %s) WHERE id = %s"
    values = [country.name, country.visited, country.id]
    run_sql(sql, values)


def vu_points(country):  # working but need to pass a country object in as an argument
    vu_points = []

    sql = "SELECT * FROM vu_points WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        # was passing row['location_id'] into the vu_point instance below but this meant when using this function, the location was an id rather than an object. By selecting the object using the location id like this, I could then pass in the variable 'location' to the object
        location = location_repository.select(row['location_id'])
        vu_point = Vu_point(row['name'], location, country, row['rating'],
                            row['description'], row['visited'], row['id'])
        vu_points.append(vu_point)
    return vu_points


def country_percentage():
    countries = select_all()
    visited = []
    for country in countries:
        if country.visited == True:
            visited.append(country)
    return round(100*(len(visited) / 195), 2)


def countries_visited():
    countries = select_all()
    visited = []
    for country in countries:
        if country.visited == True:
            visited.append(country)
    return len(visited)
