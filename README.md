# Jira Command Line Interface (`jira`) tool

This tool definition wraps a Docker Hub container containing the Jira CLI into a tool. Can
be used by Kubiya Teammates to access Jira using CLI commands.

# Installation

## Pre-requisites

To use this tool set up a Jira Integration in the Kubiya Web App.

1. Navigate to the Kubiya Web App, [app.kubiya.ai](https://app.kubiya.ai). Login if needed.
2. Select *Resources*, *Integrations*, and then *+ New Integration*.
3. In the Jira integration card, select *+ Add*.
4. Follow the instructions to authorize with Jira.
5. Select *Create Integration*.

## Uploading the tool as a new Source

1. Navigate to the Kubiya Web App, [app.kubiya.ai](https://app.kubiya.ai). Login if needed.
2. Select *Resources*, *Sources*, and then *+ New Source*.
3. Copy and paste this respository's URL into the text box *Source URL* and select *Load tools &
workflows*.
4. Under *Tools & workflows discovered* you should see a list of tools associated with this
repository.
5. Select *+ Create*.

The tool is now available for use by a Teammate.

# Usage

Depending on the roles and access assigned to the associated user, this tool can execute any
command using the Jira CLI, as indicated below:

    jira {{.command}}

This gives the tool significant ability to affect change on your Jira account. Therefore it is
highly recommended to ensure that appropriate roles and access is assigned.

In addition, this tool has been modified to only execute one type of command. For example:

    jira {{.command}}

# Contact

Please contact the author of this tool using the email address:
[support@kubiya.ai](mailto:support@kubiya.ai).
