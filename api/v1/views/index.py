#!/usr/bin/python3
"""JSON file status """

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """
    Returns the count of all objects by type
    """
     my_dict = {"amenities": storage.count(Amenity),
               "cities": storage.count(City),
               "places": storage.count(Place),
               "reviews": storage.count(Review),
               "states": storage.count(State),
               "users": storage.count(User)}
    return jsonify(my_dict)
