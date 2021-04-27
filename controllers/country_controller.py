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

    if len(all_vu_points) > 0: # stops the country visited changing to true when last vu is deleted
        true_counter = 0
        for vu_point in all_vu_points:
            if vu_point.visited == True:
                true_counter +=1
        if true_counter > 0:        # every time it iterates over all vu points before displaying, and if any vu_point.visited values are true, 1 is added to true_counter, and if true counter is not 0, it will always assign true to the country visited value
            country = Country(country.name, True, id)
            country_repository.update(country)
        else:
            country = Country(country.name, False, id)
            country_repository.update(country)

    return render_template("country/view.html", country=country, all_vu_points=all_vu_points)


@countries_blueprint.route("/country-<id>/new_vu", methods=['GET'])
def new_vu(id):
    country = country_repository.select(id)
    return render_template("country/new_vu.html", country=country)


@countries_blueprint.route("/country-<id>/new_vu", methods=['POST']) # the route here must match the route on the form
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


@countries_blueprint.route("/country-<id>/vu-point-<id2>/view", methods=['GET'])
def view_vu(id, id2):
    # id2 is being passed the vu_point.id 
    # so we can pass that in to the select(id) to get the vu_point we're looking at
    country = country_repository.select(id)
    vu_point = vu_point_repository.select(id2)
    all_vu_points = country_repository.vu_points(country)

    return render_template("vu_points/view.html", country=country, vu_point=vu_point, all_vu_points=all_vu_points)


@countries_blueprint.route("/country-<id>/vu-point-<id2>/edit", methods=['GET'])
def edit_vu(id, id2):
    # id2 is being passed the vu_point.id 
    # so we can pass that in to the select(id) to get the vu_point we're looking at
    country = country_repository.select(id)
    vu_point = vu_point_repository.select(id2)
    # all_locations = location_repository.select_all()
    # all_vu_points = country_repository.vu_points(country)
    return render_template("vu_points/edit.html", country=country, vu_point=vu_point)


@countries_blueprint.route("/country-<id>/vu-point-<id2>/edit", methods=['POST'])
def edit_vu_submit(id, id2):
    country = country_repository.select(id)
    update_vu_point = vu_point_repository.select(id2)
    location = location_repository.select(update_vu_point.location.id) 

    name = request.form['vu_name']
    rating = request.form['rating']
    description = request.form['description']
    visited = request.form['visited']   
    location_name = request.form['location_name']
    if location.name != location_name: # if the location name is not equal to the location already attached, udpate it with the new location from the form
        location.name = location_name
        location_repository.update(location)
    
    # if visited == True:
        # print("hello")

    update_vu_point = Vu_point(name, location, country, rating, description, visited, id2)
    vu_point_repository.update(update_vu_point)

    if visited == "True":
        updated_country = Country(country.name, True, id)
        country_repository.update(updated_country)

    return redirect("/country-" + id)

@countries_blueprint.route("/country-<id>/vu-point-<id2>/delete", methods=['POST'])
def delete_vu(id, id2):
    # get vu_point_object
    vu_point_repository.delete(id2)
    return redirect("/country-" + id)

@countries_blueprint.route("/country-<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/profile")