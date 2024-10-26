from flask import request, jsonify
from models.models import User, Category, Record

def init_routes(app):
    @app.route('/user/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.get_user(user_id)
        if user:
            return jsonify({"id": user.id, "name": user.name}), 200
        return jsonify({"error": "User not found"}), 404

    @app.route('/user', methods=['POST'])
    def create_user():
        data = request.get_json()
        if 'name' not in data:
            return jsonify({"error": "Name is required"}), 400
        user = User(data['name'])
        return jsonify({"id": user.id, "name": user.name}), 201

    @app.route('/user/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.users.pop(user_id, None)
        if user:
            return jsonify({"message": "User deleted"}), 200
        return jsonify({"error": "User not found"}), 404

    @app.route('/users', methods=['GET'])
    def get_all_users():
        users = [{"id": user.id, "name": user.name} for user in User.get_all_users()]
        return jsonify(users), 200

    @app.route('/category', methods=['GET'])
    def get_all_categories():
        categories = [{"id": category.id, "name": category.name} for category in Category.get_all_categories()]
        return jsonify(categories), 200

    @app.route('/category', methods=['POST'])
    def create_category():
        data = request.get_json()
        if 'name' not in data:
            return jsonify({"error": "Category name is required"}), 400
        category = Category(data['name'])
        return jsonify({"id": category.id, "name": category.name}), 201

    @app.route('/category/<int:category_id>', methods=['DELETE'])
    def delete_category(category_id):
        category = Category.categories.pop(category_id, None)
        if category:
            return jsonify({"message": "Category deleted"}), 200
        return jsonify({"error": "Category not found"}), 404

    @app.route('/record/<int:record_id>', methods=['GET'])
    def get_record(record_id):
        record = Record.get_record(record_id)
        if record:
            return jsonify({
                "id": record.id,
                "user_id": record.user_id,
                "category_id": record.category_id,
                "date": record.date.isoformat(),
                "amount": record.amount
            }), 200
        return jsonify({"error": "Record not found"}), 404

    @app.route('/record', methods=['POST'])
    def create_record():
        data = request.get_json()
        if 'user_id' not in data or 'category_id' not in data or 'amount' not in data:
            return jsonify({"error": "user_id, category_id, and amount are required"}), 400
        record = Record(data['user_id'], data['category_id'], data['amount'])
        return jsonify({
            "id": record.id,
            "user_id": record.user_id,
            "category_id": record.category_id,
            "date": record.date.isoformat(),
            "amount": record.amount
        }), 201

    @app.route('/record/<int:record_id>', methods=['DELETE'])
    def delete_record(record_id):
        record = Record.records.pop(record_id, None)
        if record:
            return jsonify({"message": "Record deleted"}), 200
        return jsonify({"error": "Record not found"}), 404

    @app.route('/record', methods=['GET'])
    def get_filtered_records():
        user_id = request.args.get('user_id', type=int)
        category_id = request.args.get('category_id', type=int)
        if user_id is None and category_id is None:
            return jsonify({"error": "user_id or category_id parameter is required"}), 400

        records = Record.get_all_records()
        if user_id:
            records = [record for record in records if record.user_id == user_id]
        if category_id:
            records = [record for record in records if record.category_id == category_id]

        response = [{
            "id": record.id,
            "user_id": record.user_id,
            "category_id": record.category_id,
            "date": record.date.isoformat(),
            "amount": record.amount
        } for record in records]

        return jsonify(response), 200
