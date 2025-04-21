import os

project = "OE5XRX - Remote Station"
copyright = "2025, Peter OE5BPA"
author = "Peter OE5BPA"

extensions = [
    "myst_parser",
    "rtds_action",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "de"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

rtds_action_github_repo = "OE5XRX/RemoteStation"
rtds_action_path = "_static"
rtds_action_artifact_prefix = "artifacts-for-"
rtds_action_github_token = os.environ["GITHUB_TOKEN"]
