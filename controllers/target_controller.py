from dataclasses import asdict
from flask import Blueprint, jsonify, request
from dto.ResponseDto import ResponseDto
from models import Target
from repository.target_repository import insert_target, get_target_by_id, delete_target, update_target, get_all_targets

targets_blueprint = Blueprint("targets", __name__)

@targets_blueprint.route("/", methods=['GET'])
def all_targets():
    return jsonify(asdict(ResponseDto(body=get_all_targets()))), 200

@targets_blueprint.route('/', methods=['POST'])
def add_target():
    target = insert_target(**request.json)
    return jsonify(asdict(ResponseDto(body=target))), 201

@targets_blueprint.route("/<int:target_id>", methods=['GET'])
def target_by_id(target_id):
    target = get_target_by_id(target_id)
    return ((jsonify(asdict(ResponseDto(body=target))), 200) if target else
            (jsonify(asdict(ResponseDto(error=f'not found target by the id {target_id}'))), 404))

@targets_blueprint.route("/<int:target_id>", methods=['DELETE'])
def delete(target_id):
    is_deleted = delete_target(target_id)
    return (jsonify(asdict(ResponseDto(message=is_deleted))), 200) if is_deleted else(
        (jsonify(asdict(ResponseDto(message=f'not found target by the id {target_id}'))), 404))

@targets_blueprint.route("/<int:target_id>", methods=['PUT'])
def update(target_id):
    is_updated = update_target(target_id, Target(**request.json))
    return ((jsonify(asdict(ResponseDto(body=is_updated))), 201) if is_updated else
            (jsonify(asdict(ResponseDto(error='not found'))), 404))
