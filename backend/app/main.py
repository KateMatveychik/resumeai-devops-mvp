from fastapi import FastAPI
from app.schemas import GenerateRequest, GenerateResponse
from app.services.llm_service import generate_resume

app = FastAPI()


@app.get("/")
def root():
    return {"message": "ResumeAI backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate", response_model=GenerateResponse)
def generate(data: GenerateRequest):
    result = generate_resume(data.resume_text, data.vacancy_text)

    return GenerateResponse(**result)