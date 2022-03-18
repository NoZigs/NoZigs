"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

import os

api = Blueprint('api', __name__)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/token", methods=["POST"])
def create_token():
    user = request.json.get('user')
    password = request.json.get('password')
    if user != "test" or password != "test":
         return jsonify({"msg": "Bad login or password"}), 401

    # To-do: 1. verify that the user exists in the database
    # 2. compare the hash from the password of the password input (line20) with the hash in the database (password field in the database)
    # 3. if above true, return token (line 28), if not, return error (line 22)

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/hello", methods=["GET"])
def get_hello():
     dictionary = {
          "message" : "hello world"
     }
     return jsonify(dictionary)


@api.route("/home", methods=["GET"])
def get_home():
     dictionary = {
          "message" : "hello world"
     }
     return jsonify(dictionary)