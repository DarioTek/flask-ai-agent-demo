from flask import Blueprint, request, jsonify

arithmetic_bp = Blueprint('arithmetic', __name__)

@arithmetic_bp.route('/arithmetic', methods=['POST'])
def arithmetic():
    if not request.is_json:
        return jsonify({"error": "invalid input"}), 400
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "invalid input"}), 400

    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(operation, str):
        return jsonify({"error": "invalid input"}), 400

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return jsonify({"error": "division by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "unsupported operation"}), 400

    return jsonify({"result": result}), 200
