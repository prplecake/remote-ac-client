from flask import Blueprint, jsonify

from services.dht import get_dht_data

bp = Blueprint("dht", __name__, url_prefix="/dht")


@bp.route('get_current_record', methods=['GET'])
def get_current_record():
    (temp_c, humidity, dht_error) = get_dht_data()
    return jsonify(temp_c=temp_c,
                   humidity=humidity,
                   dht_error=dht_error), 200
