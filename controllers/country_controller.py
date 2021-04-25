from flask import Flask, render_template, request, redirect, Blueprint
from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/profile")
def profile():
    countries = country_repository.select_all()
    return render_template("profile.html", all_countries = countries)

@countries_blueprint.route("/profile", methods=["POST"])
def save_country():
    country_name = request.form['country']
    visited = request.form['visited']
    country = Country(country_name, visited=visited)
    country_repository.save(country)
    return redirect("/profile")
    # return render_template("profile.html", all_countries = countries)

@countries_blueprint.route("/countries/<id>", methods=['GET'])
def view_country(id):
    country = country_repository.select(id)
    return render_template("countries/view.html", country=country)

@countries_blueprint.route("/countries/<id>/new", methods=['GET'])
def new_vu(id):
    country = country_repository.select(id)
    return render_template("countries/new.html", country=country)