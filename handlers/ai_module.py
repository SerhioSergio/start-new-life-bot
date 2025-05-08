
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(user_input, zone_name, step_name):
    prompt = f"""
Ты — продвинутый коуч, помогающий пользователю в {zone_name}, шаг: {step_name}.
Пользователь написал: "{user_input}"

Ответь содержательно, направь, предложи техники или новые знания, если нужно.
Говори тепло, уважительно и чётко.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты — коуч и проводник в личной трансформации."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=400
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Произошла ошибка при обращении к AI: {e}"
