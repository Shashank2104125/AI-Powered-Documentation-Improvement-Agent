from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
load_dotenv()

def analyze_article(system_prompt, content, url):
    client = InferenceClient(
        provider="together",
        api_key=os.getenv("HUGGINGFACE_API_KEY")
    )

    prompt = f"""
    Analyze the following MoEngage documentation content using the criteria in the system prompt.

    ARTICLE URL: {url}
    ARTICLE CONTENT:
    {content[:4000]}
    """

    stream = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        stream=True,
    )

    output = ""
    for chunk in stream:
        output += chunk.choices[0].delta.content or ""
    return output
