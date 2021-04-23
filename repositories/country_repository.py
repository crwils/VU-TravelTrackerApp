from db.run_sql import run_sql

from models.country import Country
from models.vu_point import Vu_point

def save(country):
    sql = "INSERT INTO countries (name, capital, continent, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country.name, country.capital, country.continent, country.visited]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country