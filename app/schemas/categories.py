from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=30)


class CategoryResponse(BaseModel):
    id: int
    name: str


    class Config:
# Указываем Pydantic использовать эти параметры чтобы можно было переносить данные прямо с объекта
        from_attributes = True
