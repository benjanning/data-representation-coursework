"""Local configuration for coursework examples.

Set GITHUB_TOKEN in your environment before running exercises that use the GitHub API.
Never commit real tokens or personal credentials.
"""
import os

config = {
    "githubkey": os.getenv("GITHUB_TOKEN", ""),
}
