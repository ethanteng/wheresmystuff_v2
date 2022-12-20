import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import PackageModel
from schemas import PackageSchema

blp = Blueprint("packages", __name__, description="Operations on packages")

@blp.route("/package/<string:package_id>")
class Package(MethodView):
    @blp.response(200,PackageSchema)
    def get(self, package_id):
        package = PackageModel.query.get_or_404(package_id)
        return package

@blp.route("/package")
class PackageList(MethodView):
    @blp.response(200,PackageSchema(many=True))
    def get(self):
        return PackageModel.query.all()

    @blp.arguments(PackageSchema)
    @blp.response(201,PackageSchema)
    def post(self, package_data):
        package = PackageModel(**package_data)
        try:
            db.session.add(package)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the package.")
        return package