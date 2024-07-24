from flask import Blueprint

questions_bp = Blueprint('questions', __name__)


@questions_bp.route('/questions')
def list_questions():
    return 'Return all questions'


@questions_bp.route('/questions/add',
methods=['POST'])
def add_question():
    return 'Question added'
