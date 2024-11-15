from flask import Blueprint, request, make_response, jsonify
from flask_jwt_extended import current_user, jwt_required
from app import db
from models import Perfume
from schemas import PerfumeSchema, PerfumeMinimalSchema

perfume_bp = Blueprint('perfumes', __name__)

@perfume_bp.route('/perfumes', methods=['GET', 'POST'])
@jwt_required()
def perfumes():
    # Método GET: cualquier usuario autenticado puede ver los perfumes
    if request.method == 'GET':
        perfumes = Perfume.query.all()
        return PerfumeSchema().dump(perfumes, many=True)

    # Método POST: solo los administradores pueden agregar perfumes
   #if not current_user.is_admin:
    #return jsonify({"error": "No tienes permisos para realizar esta acción"}), 403

    data = request.get_json()
    errors = PerfumeSchema().validate(data)
    if errors:
        return make_response(jsonify(errors), 400)

    nuevo_perfume = Perfume(
        nombre=data.get('nombre'),
        marca=data.get('marca'),
        precio=data.get('precio'),
        tipo=data.get('tipo'),
        sexo=data.get('sexo')
    )
    db.session.add(nuevo_perfume)
    db.session.commit()
    return PerfumeSchema().dump(nuevo_perfume), 201

@perfume_bp.route('/perfumes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def perfume_detalle(id):
    perfume = Perfume.query.get_or_404(id)

    # Método GET: cualquier usuario autenticado puede ver el detalle del perfume
    if request.method == 'GET':
        return PerfumeSchema().dump(perfume)

    # Métodos PUT y DELETE: solo los administradores pueden modificar o eliminar perfumes
    if not current_user.is_admin:
        return jsonify({"error": "No tienes permisos para realizar esta acción"}), 403

    if request.method == 'PUT':
        data = request.get_json()
        errors = PerfumeSchema().validate(data)
        if errors:
            return make_response(jsonify(errors), 400)

        perfume.nombre = data.get('nombre', perfume.nombre)
        perfume.marca = data.get('marca', perfume.marca)
        perfume.precio = data.get('precio', perfume.precio)
        perfume.tipo = data.get('tipo', perfume.tipo)
        perfume.sexo = data.get('sexo', perfume.sexo)

        db.session.commit()
        return PerfumeSchema().dump(perfume)

    if request.method == 'DELETE':
        db.session.delete(perfume)
        db.session.commit()
        return jsonify({"message": "Perfume eliminado correctamente"}), 204
