""""Tool for identifying the markdown guide most relevant to the prompt."""

import os
from pathlib import Path

from framework.agent import Tool

# Path to the folder with all the markdown guides.
MARKDOWN_DIR = Path(__file__).parent.parent / "evaluation" /"data" / "guides"

def markdown_summary(md_path: str) -> tuple[str, str]:
    """Reads the file from md_path and returns the title and first line."""
    title = summary = ""
    with open(md_path) as md:
        for line in md:
            if line.startswith('# '):
                title = line[2:].strip()
            elif line.isspace():
                continue
            else:
                summary = line.strip()
                break
    return (title, summary)

def choose_markdown() -> str:
    """Lists the title and first line summary in each markdown guide.

    This tool provides the agent with a summary of the rules in the markdown
    guides by using the title and first line in that section.

    Returns:
        A list of summaries for each markdown guide.
    """
    descriptions: list[str] = []
    for md in os.listdir(MARKDOWN_DIR):
        md_path = str(MARKDOWN_DIR / md)
        title, summary = markdown_summary(md_path)
        descriptions.append(
            f"Markdown file \"{md}\" contains rules about {title}. "
            f"The file states that \"{summary}\"."
        )
    return "\n".join(descriptions)

CHOOSE_MARKDOWN: Tool = Tool(
    name="choose_markdown",
    description=(
        "The SQL query needs to follow a specific set of rules. "
        "Use this tool to identify the document with rules most relevant to the"
        " prompt. You must use this tool before submitting your answer."
    ),
    parameters={},
    function=choose_markdown,
)
