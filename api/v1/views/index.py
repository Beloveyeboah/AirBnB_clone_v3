#!/usr/bin/python3
"""JSON file status """

from api.v1.views import app_views
from flask import jsonify
from flask import Flask
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats',  strict_slashes=False)
def stats():
    """
    Returns the count of all objects by type
    """
    classes = {
        'amenities': 'Amenity',
        'cities': 'City',
        'places': 'Place',
        'reviews': 'Review',
        'states': 'State',
        'users': 'User'
    }
    counts = {}
    for key, value in classes.items():
        counts[key] = storage.count(value)
    return jsonify(counts)
