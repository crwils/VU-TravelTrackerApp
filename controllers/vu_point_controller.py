from flask import Flask, render_template, request, redirect, Blueprint
from models.vu_point import Vu_point
import repositories.vu_point_repository as vu_point_repository

vu_points_blueprint = Blueprint("vu_points", __name__)