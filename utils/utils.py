from flask import jsonify

def generate_id(counter):
    return counter + 1

def format_response(data, message="Success"):
    return jsonify({"message": message, "data": data})

def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code
