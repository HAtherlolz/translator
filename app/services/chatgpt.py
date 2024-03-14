import openai

from config.conf import settings

openai.api_key = settings.OPENAI_TOKEN

llm_model = settings.OPENAI_VERSION


async def translate(prompt: str, lang: str, model=llm_model):
    prompt = f"Can u translate it to {lang}" + prompt
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]






