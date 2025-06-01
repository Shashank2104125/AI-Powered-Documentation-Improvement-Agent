revision_prompt = """
You are an expert editor specializing in revising technical documentation based on expert feedback.

You will receive:
1. The original article content.
2. A set of detailed improvement suggestions.

Using these, generate a revised version of the article that:
- Implements the improvements
- Fixes any identified clarity or structure issues
- Enhances readability for non-technical audiences

Preserve the original meaning and intent.

===================
ORIGINAL ARTICLE:
{article}

===================
SUGGESTIONS:
{suggestions}

===================
Please output the fully REVISED ARTICLE below:
"""
