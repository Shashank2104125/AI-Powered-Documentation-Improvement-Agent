from prompts.revision_prompt import revision_prompt
from inference.doc_revision_hf_inference import revise_article

#agent2 that address the improvement suggestion given by agent 1 and provide revised content
def run_agent2(original_article, suggestions):
    return revise_article(original_article,suggestions,revision_prompt)