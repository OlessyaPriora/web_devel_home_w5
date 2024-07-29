from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(..., nullable=False, max_length=30)

    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: int


class QuestionResponse(BaseModel):
    text : str
    category: CategoryBase

    class Config:
# Указываем Pydantic использовать эти параметры чтобы можно было переносить данные прямо с объекта
        from_attributes = True


class MessageResponse(BaseModel):
    message: str

    class Config:
        from_attributes  = True
