""""Tool for identifying the SQL schema most relevant to the prompt."""

from framework.agent import Tool
from framework.database import list_schemas, list_tables


def choose_schema() -> str:
    """List all the schema and tables available in the database.

    This tool queries the database for a list of schema and their associated
    tables. The agent uses the schema and table names to decide which ones
    should be used when building the final SQL query.

    Returns:
        A description of all the schemas and tables available.
    """

    descriptions: list[str] = []
    for schema in list_schemas():
        tables = ','.join(list_tables(schema))
        descriptions.append(
            f"Schema \"{schema}\" is used for the following tables: {tables}"
        )
    description = "\n".join(descriptions)
    return description

CHOOSE_SCHEMA: Tool = Tool(
    name="choose_schema",
    description=(
        "Use this tool to select the most relevant schema and tables. You must "
        "use this tool after you've used the load_rules tool and before"
        " constructing the final SQL query."
    ),
    parameters={},
    function=choose_schema,
)
