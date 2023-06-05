from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Rol(db.Model):
    __tablename__ = 'rol'
    __table_args__ = {"schema":"credito_web"}
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50), nullable=False)

class Usuarios(db.Model, UserMixin):
    __table_args__ = {"schema":"credito_web"}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name= db.Column(db.String(50), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey(Rol.id), nullable=False)
    rol = db.relationship(Rol, backref=db.backref('usuarios', lazy=True))


class Listasrestrictivas(db.Model):
    __table_args__ = {"schema":"credito_web"}
    Id_Afiliado = db.Column(db.String(10000), primary_key=True)
    Nombre_Completo2 = db.Column(db.String(10000))
    Respuesta_Final_Titular = db.Column(db.String(10000))
    Respuesta_Final_Solidario = db.Column(db.String(10000))
