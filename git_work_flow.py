import subprocess
import datetime
import os


def generate_commit_message(custom_message=None):
    # Generate the commit message dynamically based on the current date
    if custom_message:
        commit_message = custom_message
    else:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        commit_message = f"Auto commit - {current_date}"
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
    final_commit_message = generate_commit_message(commit_message)

    # Git commands
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", final_commit_message],
        ["git", "push", "origin", "main"],
    ]

    # Execute git commands
    for command in commands:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)


# Call the function to execute the Git workflow
git_workflow("added Python Script to auto COMMIT")
