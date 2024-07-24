
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import api

from app.routes.questions import questions_bp
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

app.register_blueprint(questions_bp, url_prefix='/questions')


@app.route('/')
def home():
    return 'Welcome to the Flask'


@app.route('/question/<int:question_id>')
def show_question(question_id):
    return f'Question {question_id}'


@app.route('/add-question', methods=['POST'])
def add_question():
    return 'Question added'


if __name__ == '__main__':
    app.run(debug=True)