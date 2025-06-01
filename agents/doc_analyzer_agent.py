from prompts.analyzer_prompt import analyzer_prompt
from inference.doc_analyze_hf_inference import analyze_article
from utils.fetcher import fetch_dynamic_content
from utils.extractor import extract_main_content

#agent1 that give doc-improvement suggestion
def run_agent1(url):
    html = fetch_dynamic_content(url)
    article_content = extract_main_content(html)

    with open("outputs/original_article.md", "w", encoding="utf-8") as f:
        f.write(article_content)

    if not article_content:
        return "❌ Failed to extract article content."

    return analyze_article(analyzer_prompt, article_content, url)
