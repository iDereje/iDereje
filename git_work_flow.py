import subprocess
import datetime
import os


def generate_commit_message(custom_message=None):
    # Generate the commit message dynamically based on the current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if custom_message:
        commit_message = f"{custom_message} - {current_datetime}"
    else:
        commit_message = f"Auto commit - {current_datetime}"

    return commit_message


def git_workflow(commit_message=None):
    # Specify the repository path
    repo_path = "/Users/idereje/Desktop/github/iDereje"

    # Change directory to the specified repository path
    try:
        os.chdir(repo_path)
    except FileNotFoundError:
        print(f"Repo path '{repo_path}' does not exist.")
        return

    # Generate the commit message
    commit_message = generate_commit_message(commit_message)

    # Git commands
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", commit_message],
        ["git", "push", "origin", "main"],
    ]

    # Execute git commands
    for command in commands:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)


# Call the function to execute the Git workflow
git_workflow("feat: Add support for custom commit messages with date and time")
