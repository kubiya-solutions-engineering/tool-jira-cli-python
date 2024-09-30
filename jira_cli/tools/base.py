from kubiya_sdk.tools.models import Tool
from .common import COMMON_ENVIRONMENT_VARIABLES, COMMON_SECRET_VARIABLES

JIRA_ICON_URL = "https://static-00.iconduck.com/assets.00/apps-jira-icon-512x512-sdy7ek52.png"

class JiraCliTool(Tool):
    def __init__(self, name, description, content, args, long_running=False, mermaid_diagram=None):
                super().__init__(
            name=name,
            description=description,
            icon_url=JIRA_ICON_URL,
            type="docker",
            image="ghcr.io/kubiyabot/jira-cli:latest",
            content=content,
            args=args,
            env=COMMON_ENVIRONMENT_VARIABLES,
            secrets=COMMON_SECRET_VARIABLES,
            long_running=long_running,
            mermaid_diagram=mermaid_diagram
        )

