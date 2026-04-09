from pydantic import BaseModel


class GenerateRequest(BaseModel):
    resume_text: str
    vacancy_text: str


class GenerateResponse(BaseModel):
    adapted_resume: str
    cover_letter: str