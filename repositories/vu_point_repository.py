from db.run_sql import run_sql

from models.country import Country
from models.vu_point import Vu_point

def save(vu_point):
    sql = "INSERT INTO vu_points (name, rating, description, visited, country_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [vu_point.name, vu_point.rating, vu_point.description, vu_point.visited, vu_point.country.id]
    results = run_sql(sql, values)
    vu_point.id = results[0]['id']
    return vu_point