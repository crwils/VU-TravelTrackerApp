from flask import Flask, render_template, request, redirect, Blueprint

from models.country import Country
from models.vu_point import Vu_point
from models.location import Location

import repositories.country_repository as country_repository
import repositories.vu_point_repository as vu_point_repository
import repositories.location_repository as location_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/profile") # working
def profile():
    countries = country_repository.select_all()
    return render_template("profile.html", all_countries = countries)


@countries_blueprint.route("/profile", methods=["POST"]) # working
def save_country():
    country_name = request.form['country']
    visited = request.form['visited']
    country = Country(country_name, visited)
    country_repository.save(country)
    return redirect("/profile")


@countries_blueprint.route("/country-<id>", methods=['GET'])
def view_country(id):
    country = country_repository.select(id)
    
    all_vu_points = country_repository.vu_points(country)

    return render_template("country/view.html", country=country, all_vu_points=all_vu_points)


@countries_blueprint.route("/country-<id>/new", methods=['GET'])
def new_vu(id):
    country = country_repository.select(id)
    return render_template("country/new.html", country=country)


@countries_blueprint.route("/country-<id>", methods=['POST']) # the route here must match the route on the form
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
    return redirect("/country-" + id) # can't use angle brackets here, so must use string interpolation


@countries_blueprint.route("/country-<id>/vu-point-<id2>/edit", methods=['GET'])
def edit_vu(id, id2):
    # id2 is being passed the vu_point.id 
    # so we can pass that in to the select(id) to get the vu_point we're looking at
    country = country_repository.select(id)
    vu_point = vu_point_repository.select(id2)
    # all_vu_points = country_repository.vu_points(country)
    return render_template("country/edit.html", country=country, vu_point=vu_point)


@countries_blueprint.route("/country-<id>", methods=['POST'])
def edit_vu_submit(id):
    # get the vu_point we are dealing with
    # use the form to change the values like vu_point.name = request.form...
    # update(vu_point) to finish
    country = country_repository.select(id)
    # vu_point_repository.select(id)
    location = Location(request.form['location_name'], country)
    location_repository.update(location)

    name = request.form['vu_name']
    rating = request.form['rating']
    description = request.form['description']
    visited = request.form['visited']   

    vu_point = Vu_point(name, location, country, rating, description, visited, location.id)
    vu_point_repository.update(vu_point)

    return redirect("/country-" + id)