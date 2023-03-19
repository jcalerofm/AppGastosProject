from flask import Flask, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/AppGastos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

class Gastos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    concept = db.Column(db.String(100), nullable=False)
    category = db.Column(db.Enum('compras', 'ocio', 'hogar', 'transporte', 'otros'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

# Rutas y controladores aquí
# Todos los gastos de un usuario
@app.route('/api/gastos/<int:user_id>', methods=['GET'])
def get_gastos(user_id):
    gastos = Gastos.query.filter_by(user_id=user_id).all()
    result = []
    for gasto in gastos:
        gasto_data = {
            'id': gasto.id,
            'date': gasto.date,
            'concept': gasto.concept,
            'category': gasto.category,
            'amount': str(gasto.amount),
            'user_id': gasto.user_id
        }
        result.append(gasto_data)
    return jsonify(result)

# add gasto a un usuario
@app.route('/api/gastos/<int:user_id>', methods=['POST'])
def add_gasto(user_id):
    gasto = Gastos(
        date=request.json['date'],
        concept=request.json['concept'],
        category=request.json['category'],
        amount=request.json['amount'],
        user_id=user_id
    )
    db.session.add(gasto)
    db.session.commit()
    return jsonify({'message': 'Gasto agregado correctamente'})

# update gasto de un usuario
@app.route('/api/gastos/<int:user_id>/<int:gasto_id>', methods=['PUT'])
def update_gasto(user_id, gasto_id):
    gasto = Gastos.query.filter_by(id=gasto_id, user_id=user_id).first()
    if gasto:
        gasto.date = request.json['date']
        gasto.concept = request.json['concept']
        gasto.category = request.json['category']
        gasto.amount = request.json['amount']
        db.session.commit()
        return jsonify({'message': 'Gasto actualizado correctamente'})
    return jsonify({'message': 'No se encontró el gasto'})

# delete gasto de un usuario
@app.route('/api/gastos/<int:user_id>/<int:gasto_id>', methods=['DELETE'])
def delete_gasto(user_id, gasto_id):
    gasto = Gastos.query.filter_by(id=gasto_id, user_id=user_id).first()
    if gasto:
        db.session.delete(gasto)
        db.session.commit()
        return jsonify({'message': 'Gasto eliminado correctamente'})
    return jsonify({'message': 'No se encontró el gasto'})

# registrar nuevo usuario
@app.route('/api/users', methods=['POST'])
def add_user():
    user = Users(
        name=request.json['name'],
        email=request.json['email'],
        password=request.json['password']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Usuario agregado correctamente'})

# login de usuario
# login de usuario
@app.route('/api/users/login', methods=['POST'])
def login_user():
    user = Users.query.filter_by(email=request.json['email'], password=request.json['password']).first()
    if user:
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
        return jsonify(user_data)
    return jsonify({'message': 'Login incorrecto'})


# get user by id
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
  user = Users.query.filter_by(id=user_id).first()
  if user:
      user_data = {
          'id': user.id,
          'name': user.name,
          'email': user.email,
          'password': user.password
      }
      return jsonify(user_data)
  return jsonify({'message': 'No se encontró el usuario'})

# delete user by id
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
  user = Users.query.filter_by(id=user_id).first()
  if user:
      db.session.delete(user)
      db.session.commit()
      return jsonify({'message': 'Usuario eliminado correctamente'})
  return jsonify({'message': 'No se encontró el usuario'})

#update user by id
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
  user = Users.query.filter_by(id=user_id).first()
  if user:
      user.name = request.json['name']
      user.email = request.json['email']
      user.password = request.json['password']
      db.session.commit()
      return jsonify({'message': 'Usuario actualizado correctamente'})
  return jsonify({'message': 'No se encontró el usuario'})

# get all users
@app.route('/api/allUsers', methods=['GET'])
def get_all_users():
  users = Users.query.all()
  result = []
  for user in users:
      user_data = {
          'id': user.id,
          'name': user.name,
          'email': user.email,
          'password': user.password
      }
      result.append(user_data)
  return jsonify(result)

if __name__ == '__main__':
  app.run(debug=True, port=5001)


