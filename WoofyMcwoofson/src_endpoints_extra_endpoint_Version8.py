from flask import Blueprint, jsonify

extra = Blueprint('extra', __name__)

@extra.route('/woof-extra', methods=['GET'])
def woof_extra():
    """An extra enterprise endpoint – returns a fun dog fact."""
    return jsonify({"fact": "Dogs have unique nose prints, just like human fingerprints!"})