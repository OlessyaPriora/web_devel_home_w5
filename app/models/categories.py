from app.models import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)

    questions = db.relationship("Question", back_populates="category")


    def __repr__(self):
        return f'Category id: {self.id}, Category name: {self.name}'