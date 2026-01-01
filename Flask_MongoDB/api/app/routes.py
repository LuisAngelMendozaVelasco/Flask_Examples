from flask import request, Response, Blueprint, jsonify
from bson import json_util
from pymongo.errors import PyMongoError
from werkzeug.security import generate_password_hash
import datetime
from .models import User

bp = Blueprint('main', __name__)

@bp.route("/users", methods=["GET"])
def get_users():
    try:
        users = User.find_all()
        response = json_util.dumps([user.to_dict() for user in users])
        return Response(response, mimetype="application/json")
    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/users/<id>", methods=["GET"])
def get_user(id):
    try:
        user = User.find_by_id(id)
        if user:
            response = json_util.dumps(user.to_dict())
            return Response(response, mimetype="application/json")
        else:
            return jsonify({"error": "User not found!"}), 404
    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/users", methods=["POST"])
def create_user():
    try:
        user_data = request.get_json()
        user = User(
            fullname=user_data['fullname'],
            email=user_data['email'],
            password=user_data['password'],
            registration=datetime.datetime.now(datetime.UTC)
        )
        try:
            user.validate()
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        user.password = generate_password_hash(user.password)
        user.save()
        return jsonify({"message": "User created successfully!"})
    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/users/<id>", methods=["PUT"])
def update_user(id):
    try:
        user_data = request.get_json()
        user = User.find_by_id(id)
        if user:
            user.fullname = user_data['fullname']
            user.email = user_data['email']
            user.password = user_data['password']
            user.modification = datetime.datetime.now(datetime.UTC)
            try:
                user.validate()
            except ValueError as e:
                return jsonify({"error": str(e)}), 400
            user.password = generate_password_hash(user.password)
            user.save()
            return jsonify({"message": "User updated successfully!"})
        else:
            return jsonify({"error": "User not found!"}), 404
    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = User.find_by_id(id)
        if user:
            user.delete()
            return jsonify({"message": "User deleted successfully!"})
        else:
            return jsonify({"error": "User not found!"}), 404
    except PyMongoError as e:
        return jsonify({"error": str(e)}), 500
