import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def get_api_key() -> str | None:
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        return api_key

    try:
        import streamlit as st
    except ImportError:
        return None

    return st.secrets.get("GROQ_API_KEY")


def get_client() -> Groq:
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "Missing GROQ_API_KEY. Set it in your environment, .env file, or Streamlit secrets before generating questions."
        )
    return Groq(api_key=api_key)

def call_llm(
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        model: str = "llama-3.3-70b-versatile"
):
    client = get_client()
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content


