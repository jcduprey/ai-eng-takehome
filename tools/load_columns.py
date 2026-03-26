""""Tool for loading the columns in tables associated with a given schema."""

from framework.agent import Tool
from framework.database import describe_table, list_tables


def load_columns(schema: str) -> str:
    """List all the columns in all the tables that us a given schema.

    This tool gives the agent a list of all the columns available so it can
    choose the relevant ones to use for the final SQL query.

    Args:
        schema: A valid schema from the SQL database.

    Returns:
        A string with all the columns in each table.
    """
    descriptions: list[str] = []
    descriptions.append(f"Schema \"{schema}\" is used for the following tables:")
    for table in list_tables(schema):
        columns = ",".join(describe_table(schema, table))
        descriptions.append(f"\t- Table \"{table}\" with columns {columns}")
    description = "\n".join(descriptions)
    return description

LOAD_COLUMNS: Tool = Tool(
    name="load_columns",
    description=(
        "The SQL query needs to reference specific columns in tables that use "
        "the schema identified by the choose_schema tool. Use this tool to "
        "decide which columns to use for the SQL query. You must use this tool "
        "before submitting your answer."
    ),
    parameters={
        "type": "object",
        "properties": {
            "schema": {
                "type": "string",
                "description": (
                    "The schema identified by the choose_schema tool."
                    "This must be a valid SQL schema (e.g., 'ErgastF1', 'Accidents')"
                ),
            },
        },
        "required": ["schema"],
    },
    function=load_columns,
)