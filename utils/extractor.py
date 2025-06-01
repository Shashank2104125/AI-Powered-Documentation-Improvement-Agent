from bs4 import BeautifulSoup

def extract_main_content(html):
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    return article.get_text(separator="\n") if article else ""
