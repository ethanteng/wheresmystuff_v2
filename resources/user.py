import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import UserModel
from schemas import UserSchema

blp = Blueprint("users", __name__, description="Operations on users")

@blp.route("/user/<string:user_id>")
class User(MethodView):
    @blp.response(200,UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

@blp.route("/user")
class UserList(MethodView):
    @blp.response(200,UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(201,UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A user with that email already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the user.")
        return user