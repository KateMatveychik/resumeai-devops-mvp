from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class GenerateRequest(BaseModel):
    resume_text: str
    vacancy_text: str


class GenerateResponse(BaseModel):
    adapted_resume: str
    cover_letter: str


@app.get("/")
def root():
    return {"message": "ResumeAI backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate", response_model=GenerateResponse)
def generate(data: GenerateRequest):
    adapted_resume = (
        "Адаптированное резюме под вакансию:\n\n"
        f"{data.resume_text}\n\n"
        "Ключевой акцент: соответствие требованиям вакансии."
    )

    cover_letter = (
        "Сопроводительное письмо:\n\n"
        "Здравствуйте!\n\n"
        "Меня заинтересовала данная вакансия. "
        "Считаю, что мой опыт и навыки соответствуют указанным требованиям.\n\n"
        f"Описание вакансии:\n{data.vacancy_text}\n\n"
        "Спасибо за внимание к моей кандидатуре."
    )

    return GenerateResponse(
        adapted_resume=adapted_resume,
        cover_letter=cover_letter
    )