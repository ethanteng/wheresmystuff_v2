from db import db

class PackageModel(db.Model):
    __tablename__ = "packages"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), db.ForeignKey("users.email"), unique=False, nullable=False)
    tracking_code = db.Column(db.String(80), unique=False, nullable=False)
    carrier = db.Column(db.String(80), unique=False, nullable=True)
    description = db.Column(db.String(256), unique=False, nullable=True)
    custom_url = db.Column(db.String(80), unique=False, nullable=True)
    user = db.relationship("UserModel", back_populates="packages")