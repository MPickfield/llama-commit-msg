import json
import subprocess
import sys

import requests

url = "http://localhost:11434/api/chat"


def llama3(prompt):
    data = {
        "model": "llama3",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=data)
    return response.json()["message"]["content"]


def git_diff():
    diff_output = subprocess.check_output(["git", "diff"])
    status_output = subprocess.check_output(["git", "status"])
    return (
        "git diff output:"
        + diff_output.decode("utf-8").strip()
        + "\n\n"
        + "git status output:"
        + status_output.decode("utf-8").strip()
    )


def run_llama():
    output = subprocess.check_output(["ollama", "ps"])
    ps_output = output.decode("utf-8").strip()
    if "llama3:latest" in ps_output:
        return
    output = subprocess.check_output(["ollama", "run", "llama3"])


if __name__ == "__main__":
    run_llama()
    changes = git_diff()
    summary = llama3(
        "You are an expert software developer summarizing changes for a commit message. "
        "Here are the changes for you to summarize:\n" + changes
    )
    print(summary)
