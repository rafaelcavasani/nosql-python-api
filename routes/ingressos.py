from flask import Blueprint, jsonify, request
from services.ingressos import IngressoService
from db import db

ingressos_blueprint = Blueprint('ingressos', __name__)

@ingressos_blueprint.route('/ingressos', methods=['GET'])
def getIngressos():
    return IngressoService.getAll(db.dbObject), 200

@ingressos_blueprint.route('/ingressos/<int:id>', methods=['GET'])
def getOneIngresso(id):
    return IngressoService.getOne(db.dbObject, id), 200

@ingressos_blueprint.route('/ingressos', methods=['POST'])
def insertIngresso():
    return IngressoService.insert(db.dbObject, request), 200

@ingressos_blueprint.route('/ingressos/<int:id>', methods=['PUT'])
def updateIngresso(id):
    return IngressoService.update(db.dbObject, request, id), 200

@ingressos_blueprint.route('/ingressos/<int:id>', methods=['DELETE'])
def deleteIngresso(id):
    return IngressoService.delete(db.dbObject, id), 200
