#!/usr/bin/python3
"""api for State module"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.state import State
from flasgger.utils import swag_from


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get.yml', methods=['GET'])
def print_all_states():
    """
        getting all states from storage
    """
    all_states = storage.all(State).values()
    list_states = []
    for state in all_states:
        list_states.append(state.to_dict())
    return jsonify(list_states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/state/get_id.yml', methods=['GET'])
def print_state_by_id(state_id):
    """ Retrieves a specific State """
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/state/delete.yml', methods=['DELETE'])
def delete_state(state_id):
    """ delete state by id"""
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    storage.delete(state)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/state/post.yml', methods=['POST'])
def create_state():
    """ create new instance """
    request_json = request.get_json()
    if request_json is None:
        abort(400, 'Not a JSON')
    try:
        name_state = request_json['name']
    except Exception:
        abort(400, "Missing name")
    state = State(name=name_state)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/state/put_state.yml', methods=['PUT'])
def update_state(state_id):
    tate = check(state_id)
    request_json = request.get_json()
    if request_json is None:
        abort(400, 'Not a JSON')
    for x, y in request_json.items():
        if (x not in ('id', 'created_at', 'updated_at')):
            setattr(state, x, y)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
