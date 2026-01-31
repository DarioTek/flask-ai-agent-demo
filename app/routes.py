from flask import Blueprint, jsonify

bp = Blueprint('routes', __name__)

@bp.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})
