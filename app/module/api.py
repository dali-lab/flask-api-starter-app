"""Sample Routes."""

from flask import Blueprint, jsonify, request

blueprint = Blueprint('/', __name__, url_prefix='/module')


@blueprint.route('/sample', methods=['GET'])
def sentence_grammar():
    return jsonify({
        "id": 1,
    })
