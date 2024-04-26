#!/usr/bin/python3
""" module contains endpoint(route) status
"""

from flask import jsonify
from api.v1.views import app_views
from flask import Flask

@app_views.route('/status', strict_slashes=False)
def status():

    """ returns json ok - status 
    """

    return jsonify({"status": "OK"})
