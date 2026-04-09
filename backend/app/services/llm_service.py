def generate_resume(resume_text: str, vacancy_text: str) -> dict:
    adapted_resume = (
        "Адаптированное резюме под вакансию:\n\n"
        f"{resume_text}\n\n"
        "Ключевой акцент: соответствие требованиям вакансии."
    )

    cover_letter = (
        "Сопроводительное письмо:\n\n"
        "Здравствуйте!\n\n"
        "Меня заинтересовала данная вакансия.\n\n"
        f"Описание вакансии:\n{vacancy_text}\n\n"
        "Спасибо за внимание."
    )

    return {
        "adapted_resume": adapted_resume,
        "cover_letter": cover_letter
    }