# AI Documentation Improvement Agent

## Model Used

This project leverages the **`mistralai/Mistral-7B-Instruct-v0.3`** model from Hugging Face, accessed via the **Together AI** inference provider.  
It is used for:

- Analyzing documentation quality (clarity, tone, structure, accuracy).
- Generating revised content based on suggestions and prompts.

API access is securely managed using the Hugging Face `InferenceClient` with the Together provider.

---

## Tasks Overview

This repository contains the complete solution to an AI-powered agent designed to **analyze** and **revise** technical documentation using LLMs. The project is divided into two tasks:

- ✅ **Task 1**: Analyze an article and provide suggestions for improvement.
- ✅ **Task 2**: Apply those suggestions to revise the article using a revision prompt.

---

## Project Overview

This tool fetches MoEngage documentation pages, extracts the article content, analyzes it using a system prompt, and then rewrites it using structured suggestions.

---

## Tasks

### Task 1: Analyze the Article

- Extract the article from the provided URL using Selenium and BeautifulSoup.
- Use a system prompt to evaluate:
  - Clarity
  - Structure
  - Tone
  - Technical accuracy
- Output suggestions into `outputs/analysis_report.md`.

### Task 2: Revise the Article

- Use the original article and suggestions from Task 1.
- Apply a revision prompt using HuggingFace's `InferenceClient`.
- Save the improved version in `outputs/revised_article.md`.

---

## ⚙️ Setup & Usage

### 1. Clone the Repository

git clone
cd ai_doc_improvement_agent

### 2. Install Required Dependencies

pip install -r requirements.txt

### 3. Set Up Environment Variables

Create a .env file in the root directory and add your Hugging Face API key:
HUGGINGFACE_API_KEY=your_hf_api_key_here

### 4. Run the Project

python main.py
