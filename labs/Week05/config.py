"""Local configuration for API-based coursework exercises.

Set GITHUB_TOKEN and HTML_TO_PDF_API_KEY in your environment as needed.
Never commit tokens or secrets to a public repository.
"""
import os

config = {
    "githubkey": os.getenv("GITHUB_TOKEN", ""),
    "htmltopdfkey": os.getenv("HTML_TO_PDF_API_KEY", ""),
}
