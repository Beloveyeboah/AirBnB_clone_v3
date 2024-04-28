#!/usr/bin/python3
"""JSON file status """

from models import storage
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/status',  methods=['GET'], strict_slashes=False)
def status():
    """ returns a json"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    Returns the count of all objects by type
    """
     classes = [Amenity, City, Place, Review, State, User]
     values =  names = ["amenities", "cities", "places", "reviews", "states", "users"]

     new_list = {}
     total_list = len(classes)

     for objs in range(total_list):
         new_list[values[objs]] = storage.count(classes[objs])

         return jsonify(new_list)

