from db.run_sql import run_sql

from models.country import Country
from models.vu_point import Vu_point
from models.location import Location

import repositories.country_repository as country_repository
import repositories.location_repository as location_repository


def save(vu_point):  # working
    sql = "INSERT INTO vu_points (name, rating, description, visited, country_id, location_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [vu_point.name, vu_point.rating, vu_point.description,
              vu_point.visited, vu_point.country.id, vu_point.location.id]
    results = run_sql(sql, values)
    vu_point.id = results[0]['id']
    return vu_point


def select_all():  # working
    vu_points = []
    sql = "SELECT * FROM vu_points"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        location = location_repository.select(row['location_id'])
        vu_point = Vu_point(row['name'], location, country, row['rating'],
                            row['description'], row['visited'], row['id'])
        vu_points.append(vu_point)
    return vu_points


def select(id):  # working
    vu_point = None
    sql = "SELECT * FROM vu_points WHERE id = (%s)"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repository.select(result['country_id'])
        location = location_repository.select(result['location_id'])
        vu_point = Vu_point(result['name'], location, country, result['rating'],
                            result['description'], result['visited'], result['id'])
    return vu_point


def delete_all():  # working
    sql = "DELETE FROM vu_points"
    run_sql(sql)


def delete(id):  # working
    sql = "DELETE FROM vu_points WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(vu_point):  # working
    sql = "UPDATE vu_points SET (name, rating, description, visited, country_id, location_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [vu_point.name, vu_point.rating, vu_point.description,
              vu_point.visited, vu_point.country.id, vu_point.location.id, vu_point.id]
    run_sql(sql, values)
