import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def analyze_and_reply(user_message: str) -> str:
    try:
        prompt = (
            "Ты — мудрый и заботливый коуч. Пользователь делится личным размышлением или голосом. "
            "Проанализируй это коротко и с поддержкой. Дай обратную связь, как будто ты хочешь помочь, не судя.\n\n"
            f"Сообщение пользователя:\n{user_message}\n\n"
            "Ответ:"
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты — доброжелательный психолог и коуч."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        reply = response.choices[0].message["content"].strip()
        return reply

    except Exception as e:
        return f"Произошла ошибка при анализе ответа: {e}"# Обработка ответов, голосов и ИИ-анализ
