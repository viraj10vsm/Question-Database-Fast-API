from pydantic import BaseModel

class Question(BaseModel):
    question: str
    answer: str
    category: str
    difficulty: str
    role: str