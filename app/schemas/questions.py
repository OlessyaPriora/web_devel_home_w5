from pydantic import BaseModel, Field


class QuestionCreate(BaseModel):
    text: str = Field(..., max_length=255)
    category_id: int = Field(..., gt=0)


class QuestionResponse(BaseModel):
    id: int
    text: str
    category_id: int

    class Config:
# Указываем Pydantic использовать эти параметры чтобы можно было переносить данные прямо с объекта
        from_attributes = True


