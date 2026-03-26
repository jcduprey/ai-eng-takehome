""""Tool for loading all the rules in a given markdown guide."""

from framework.agent import Tool
from tools.choose_markdown import MARKDOWN_DIR


def load_rules(markdown_file: str) -> str:
   """This tool provides the agent with all the contents a given markdown file.

   Args:
        markdown_file: The file identified by the choose_markdown tool.

    Returns:
        A string with the full contents of that file.
   """
   rules = []
   with open(str(MARKDOWN_DIR / markdown_file)) as md:
      rules = md.readlines()
   return ''.join(rules)

LOAD_RULES: Tool = Tool(
    name="load_rules",
    description=(
        "The SQL query needs to follow a specific set of rules."
        "Use this tool to load the rules in the markdown file identified by the"
        " choose_markdown tool. Use these rules and the user's prompt to"
        " filter results provided by the SQL query. Select as many columns "
        " as necessary from the appropriate rows. You must use this tool"
        " before submitting your answer."
    ),
    parameters={
        "type": "object",
        "properties": {
            "markdown_file": {
                "type": "string",
                "description": (
                    "The markdown file identified by the choose_markdown tool."
                    "This must be a valid file name (e.g., 'research.md')"
                ),
            },
        },
        "required": ["markdown_file"],
    },
    function=load_rules,
)