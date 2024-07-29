from flask import Blueprint, request, jsonify, make_response
from pydantic import ValidationError
from app.models import Question, db, Category
from app.schemas.questions import QuestionCreate, QuestionResponse


questions_bp = Blueprint('questions', __name__, url_prefix='/questions')


# @questions_bp.route('/', methods=['GET'])
# def get_questions():
#     questions = Question.query.all()
#     questions_data = [{'id': q.id, 'text': q.text} for q in questions]
#     return jsonify(questions_data)
@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Получение списка всех вопросов."""
    questions = Question.query.all()
    # Сериализуем объекты SQLAlchemy в Pydantic модели
    results = [QuestionResponse.from_orm(question).dict() for question in questions]
    return jsonify(results)


@questions_bp.route('/', methods=['POST'])
def create_question():
    data = request.get_json()

    try:
        question_data = QuestionCreate(**data)
    except ValidationError as e:
        return jsonify(e.error()), 400
    category = Category.query.get(question_data.category_id)
    if not category:
        return jsonify({"message": "Категория с таким ID не найдена"}), 404

    # if not data or 'text' not in data:
    #     return jsonify({'error': 'Missing data'}), 400

    question = Question(text=question_data['text'], category_id=category['id'])
    db.session.add(question)
    db.session.commit()

    return jsonify(QuestionResponse.from_orm(question).dict()), 201


@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = Question.query.get(question_id)

    if question is None:
        return jsonify({'message': 'Question with this ID not found'}), 404

    return jsonify(QuestionResponse.from_orm(question).dict()), 200


@questions_bp.route('/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    question = Question.query.get(question_id)

    if question is None:
        return jsonify({'message': 'Question with this ID not found'}), 404

    data = request.get_json()
    if 'text' in data:
        question.text = data['text']
    if 'category_id' in data:
        question.category_id = data['category_id']
    db.session.commit()
    return jsonify({'message': 'Question updated'}), 200


@questions_bp.route('/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    question = Question.query.get(question_id)

    if question is None:
        return jsonify({'message': 'Question with this ID not found'}), 404

    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': f'Question {question.id} deleted'}), 200