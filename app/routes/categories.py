from flask import Blueprint, request, jsonify, make_response
from pydantic import ValidationError

from app.models import Category, db
from app.schemas.categories import CategoryResponse, CategoryCreate

categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


@categories_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    results = [CategoryResponse.from_orm(category).dict() for category in categories]
    return jsonify(results)


@categories_bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()

    try:
        category_data = CategoryCreate(**data)
    except ValidationError as e:
        return jsonify(e.error()), 400


    category = Category(name=category_data['name'])
    db.session.add(category)
    db.session.commit()

    return jsonify(CategoryResponse(id=category.id, name=category.name).dict()), 201


@categories_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get(id)

    if category is None:
        return jsonify({'message': 'Category with this ID not found'}), 404

    data = request.get_json()
    if 'name' in data:
        category.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Category updated'}), 200
    else:
        return jsonify({'message': 'Missing name'}), 400


@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)

    if category is None:
        return jsonify({'message': 'Category with this ID not found'}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': f'Category {category.id} deleted'}), 200

