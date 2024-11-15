from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Boolean)


    def to_dict(self):
        return dict(
            username=self.username,
            password=self.password_hash
        )


class Perfume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return dict(
            id=self.id,
            nombre=self.nombre,
            marca=self.marca,
            precio=self.precio,
            tipo=self.tipo,
            sexo=self.sexo
        )