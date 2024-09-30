from kubiya_sdk.tools import Arg
from .base import JiraCliTool
from kubiya_sdk.tools.registry import tool_registry

jira_cli = JiraCliTool(
    name="jira_cli",
    description="""Interacts with Jira using the CLI. Before passing command arguments, check they
        are correct by using either `--help` or the `help` command.""",
    content="env && jira {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description="""
                The Jira CLI command to run (example: `issue`). Do not add `jira` at the front.
            """,
            required=True),
    ],
)

tool_registry.register("Jira", jira_cli)
