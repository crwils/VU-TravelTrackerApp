from db.run_sql import run_sql

from models.country import Country
from models.vu_point import Vu_point

def save(country):
    sql = "INSERT INTO countries (name, capital, continent, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country.name, country.capital, country.continent, country.visited]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country


def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['capital'], row['continent'], row['visited'], row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = (%s)"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = Country(result['name'], result['capital'], result['continent'], result['visited'], result['id'])
    return country


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

