from db.run_sql import run_sql

from models.country import Country
from models.vu_point import Vu_point
import repositories.country_repository as country_repository

def save(vu_point):
    sql = "INSERT INTO vu_points (name, rating, description, visited, country_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [vu_point.name, vu_point.rating, vu_point.description, vu_point.visited, vu_point.country.id]
    results = run_sql(sql, values)
    vu_point.id = results[0]['id']
    return vu_point


def select_all():
    vu_points = []
    sql = "SELECT * FROM vu_points"
    results = run_sql(sql)
    for row in results:
        country = country_repository.select(row['country_id'])
        vu_point = Vu_point(row['name'], country, row['rating'], row['description'], row['visited'], row['id'])
    vu_points.append(vu_point)
    return vu_points


def select(id):
    vu_point = None
    sql = "SELECT * FROM vu_points WHERE id = (%s)"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repository.select(result['country_id'])
        vu_point = Vu_point(result['name'], country, result['rating'], result['description'], result['visited'], result['id'])
    return vu_point


def delete_all():
    sql = "DELETE FROM vu_points"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vu_points WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(vu_point):
    sql = "UPDATE vu_points SET (name, rating, description, visited, country_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [vu_point.name, vu_point.rating, vu_point.description, vu_point.visited, vu_point.country.id, vu_point.id]
    results = run_sql(sql, values)