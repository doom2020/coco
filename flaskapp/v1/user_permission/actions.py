from flask import Blueprint

user_permission_bp = Blueprint('user_permission', __name__, url_prefix='/api/v1')


@user_permission_bp.route('users', methods=['GET'])
def users_view():
    pass


@user_permission_bp.route('role', methods=['GET'])
def role_view():
    pass


@user_permission_bp.route('Menu', methods=['GET'])
def menu_view():
    pass

