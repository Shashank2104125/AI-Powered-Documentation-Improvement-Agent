from agents.doc_analyzer_agent import run_agent1
from agents.doc_revision_agent import run_agent2

def main():
    #The original content of the MoEngage documentation article (fetched from the URL).
    url = "https://help.moengage.com/hc/en-us/articles/360035738832-Explore-the-Number-of-Notifications-Received-by-Users"
    result = run_agent1(url)

    print("\n========= ANALYSIS REPORT =========\n")
    print(result)

    with open("outputs/analysis_report.md", "w", encoding="utf-8") as f:
        f.write(result)

    with open("outputs/original_article.md", "r", encoding="utf-8") as f:
        original_article = f.read()

    with open("outputs/analysis_report.md", "r", encoding="utf-8") as f:
        suggestions = f.read()

    revised = run_agent2(original_article, suggestions)

    with open("outputs/revised_article.md", "w", encoding="utf-8") as f:
        f.write(revised)  

    print("\n========= REVISION DOC =========\n")
    print(revised)

if __name__ == "__main__":
    main()
