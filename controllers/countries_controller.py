from flask import Flask, render_template, request, redirect, Blueprint

from models.country import Country
from models.vu_point import Vu_point
from models.location import Location

import repositories.country_repository as country_repository
import repositories.vu_point_repository as vu_point_repository
import repositories.location_repository as location_repository

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/profile")
def profile():
    countries = country_repository.select_all()
    country_percentage = country_repository.country_percentage()
    countries_visited = country_repository.countries_visited()
    return render_template("profile.html", all_countries=countries, country_percentage=country_percentage, countries_visited=countries_visited)


@countries_blueprint.route("/profile", methods=["POST"])
def save_country():
    country_name = request.form['country']
    visited = request.form['visited']
    country = Country(country_name, visited)
    country_repository.save(country)
    return redirect("/profile")


@countries_blueprint.route("/countries-<id>", methods=['GET'])
def view_country(id):
    country = country_repository.select(id)
    all_vu_points = country_repository.vu_points(country)

    # if len(all_vu_points) > 0:  # stops the country visited changing to true when last vu is deleted
        # true_counter = 0
    for vu_point in all_vu_points:  # by doing on this route, it takes account of edits and new vu's
        if vu_point.visited == True:
                country = Country(country.name, True, id)
                country_repository.update(country)
                # true_counter += 1
        # if true_counter > 0:        # every time it iterates over all vu points before displaying, and if any vu_point.visited values are true, 1 is added to true_counter, and if true counter is not 0, it will always assign true to the country visited value. This was to stop the country changing to not visited if one vu_point changed to not visited
        #     country = Country(country.name, True, id)
        #     country_repository.update(country)

    return render_template("countries/view.html", country=country, all_vu_points=all_vu_points)


@countries_blueprint.route("/countries-<id>/new_vu", methods=['GET'])
def new_vu(id):
    country = country_repository.select(id)
    return render_template("countries/new_vu.html", country=country)


# the route here must match the route on the form
@countries_blueprint.route("/countries-<id>/new_vu", methods=['POST'])
def submit_new_vu(id):
    country = country_repository.select(id)
    location = Location(request.form['location_name'], country)
    location_repository.save(location)

    name = request.form['vu_name']
    rating = request.form['rating']
    description = request.form['description']
    visited = request.form['visited']

    vu_point = Vu_point(name, location, country, rating, description, visited)
    vu_point_repository.save(vu_point)

    # can't use angle brackets here, so must use string interpolation
    return redirect("/countries-" + id)


@countries_blueprint.route("/countries-<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/profile")


@countries_blueprint.route("/countries-<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template("countries/edit.html", country=country)


@countries_blueprint.route("/countries-<id>/edit", methods=['POST'])
def submit_country_edit(id):
    country_name = request.form['country']
    visited = request.form['visited']
    country = Country(country_name, visited, id)
    country_repository.update(country)
    return redirect("/countries-" + id)
