from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)


class Usuario(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    favoritos_usuario = db.relationship('Favoritos', backref='usuario', lazy=True)


    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Personajes(db.Model):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    apellido = db.Column(db.String(250), nullable=False)
    genero = db.Column(db.String(250), nullable=False)
    altura = db.Column(db.String(250), nullable=False)
    favoritos_personajes = db.relationship('Favoritos', backref='personajes', lazy=True)


    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre":self.nombre,
            "apellido": self.apellido,
            "genero": self.genero,
            "altura": self.altura,
        }

class Vehiculos(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(250), nullable=False)
    capacidad = db.Column(db.String(250), nullable=False)
    creacion = db.Column(db.String(250), nullable=False)
    favoritos_vehiculos = db.relationship('Favoritos', backref='vehiculos', lazy=True)


    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "modelo":self.modelo,
            "capacidad": self.capacidad,
            "creacion": self.creacion,
        }

class Planetas(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    poblacion = db.Column(db.String(250), nullable=False)
    bioma = db.Column(db.String(250), nullable=False)
    favoritos_planetas = db.relationship('Favoritos', backref='planetas', lazy=True)

    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre":self.nombre,
            "poblacion": self.poblacion,
            "bioma": self.bioma,
        }





class Favoritos(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    personajes_id = db.Column(db.Integer, db.ForeignKey('personajes.id'))
    vehiculos_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'))
    planetas_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))


    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personajes_id":self.personajes_id,
            "vehiculos_id":self.vehiculos_id,
            "planetas_id ":self.planetas_id

        }