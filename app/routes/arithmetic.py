from flask import Blueprint, request, jsonify

arithmetic_bp = Blueprint('arithmetic', __name__)

@arithmetic_bp.route('/arithmetic', methods=['POST'])
def arithmetic():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    if a is None or b is None or operation is None:
        return jsonify({"error": "Missing required fields"}), 400
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Fields 'a' and 'b' must be numbers"}), 400

    if not isinstance(operation, str):
        return jsonify({"error": "Field 'operation' must be a string"}), 400


    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Fields 'a' and 'b' must be numbers"}), 400

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return jsonify({"error": "division by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Unsupported operation"}), 400

    return jsonify({"result": result}), 200
