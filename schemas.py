from app import ma

from marshmallow import validates, ValidationError

from models import User, Perfume

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password_hash = ma.auto_field()
    is_admin = ma.auto_field()

class UserMinimalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = ma.auto_field()



class PerfumeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Perfume

    id = ma.auto_field()
    nombre = ma.auto_field()
    marca = ma.auto_field()
    precio = ma.auto_field()
    tipo = ma.auto_field()
    sexo = ma.auto_field()

class PerfumeMinimalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Perfume

    nombre = ma.auto_field()
    marca = ma.auto_field()
    precio = ma.auto_field()



