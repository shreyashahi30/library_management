from flask import Blueprint, request, jsonify
from app.services.member_service import MemberService
from app.auth import token_required

members_bp = Blueprint('members', __name__)

@members_bp.route('/members', methods=['POST'])
@token_required
def create_member():
    data = request.json
    if 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid data"}), 400
    member = MemberService.create_member(data['name'], data['email'])
    return jsonify(member), 201

@members_bp.route('/members', methods=['GET'])
@token_required
def list_members():
    members = MemberService.get_all_members()
    return jsonify({"members": members})

