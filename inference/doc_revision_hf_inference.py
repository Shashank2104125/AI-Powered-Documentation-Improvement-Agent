from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
load_dotenv()

def revise_article(original_article, suggestions,revision_prompt):
    client = InferenceClient(
        provider="together",
        api_key=os.getenv("HUGGINGFACE_API_KEY")
    )

    prompt = revision_prompt.format(
        article=original_article[:4000],
        suggestions=suggestions[:2000]
    )

    stream = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=[
            {"role": "system", "content": revision_prompt},
            {"role": "user", "content": prompt}
        ],
        stream=True,
    )

    output = ""
    for chunk in stream:
        output += chunk.choices[0].delta.content or ""
    return output
