from flask import Flask, render_template, request, redirect, Blueprint

from models.vu_point import Vu_point

import repositories.vu_point_repository as vu_point_repository
import repositories.country_repository as country_repository
import repositories.location_repository as location_repository

vu_points_blueprint = Blueprint("vu_points", __name__)


@vu_points_blueprint.route("/countries-<id>/vu-points-<id2>/view", methods=['GET'])
def view_vu(id, id2):
    # id2 is being passed the vu_point.id
    # so we can pass that in to the select(id) to get the vu_point we're looking at
    country = country_repository.select(id)
    vu_point = vu_point_repository.select(id2)
    all_vu_points = country_repository.vu_points(country)

    return render_template("vu_points/view.html", country=country, vu_point=vu_point, all_vu_points=all_vu_points)


@vu_points_blueprint.route("/countries-<id>/vu-points-<id2>/edit", methods=['GET'])
def edit_vu(id, id2):
    # id2 is being passed the vu_point.id
    # so we can pass that in to the select(id) to get the vu_point we're looking at
    country = country_repository.select(id)
    vu_point = vu_point_repository.select(id2)
    # all_locations = location_repository.select_all()
    # all_vu_points = country_repository.vu_points(country)
    return render_template("vu_points/edit.html", country=country, vu_point=vu_point)


@vu_points_blueprint.route("/countries-<id>/vu-points-<id2>/edit", methods=['POST'])
def edit_vu_submit(id, id2):
    country = country_repository.select(id)
    update_vu_point = vu_point_repository.select(id2)
    location = location_repository.select(update_vu_point.location.id)

    name = request.form['vu_name']
    rating = request.form['rating']
    description = request.form['description']
    visited = request.form['visited']
    location_name = request.form['location_name']
    if location.name != location_name:  # if the location name is not equal to the location already attached, udpate it with the new location from the form
        location.name = location_name
        location_repository.update(location)

    update_vu_point = Vu_point(name, location, country, rating, description, visited, id2)
    vu_point_repository.update(update_vu_point)

    return redirect("/countries-" + id)


@vu_points_blueprint.route("/countries-<id>/vu-points-<id2>/delete", methods=['POST'])
def delete_vu(id, id2):
    # get vu_point_object
    vu_point_repository.delete(id2)
    return redirect("/countries-" + id)
