import git
import os

def update_from_git():
    repository_url = "https://github.com/HeisenbergCipherCracker/sqlgo.git"
    local_path = os.getcwd()

    try:
        # Open the repository if it already exists, otherwise clone it
        repo = git.Repo(local_path)
    except git.NoSuchPathError:
        repo = git.Repo.clone_from(repository_url, local_path)

    # Fetch the latest changes from the remote repository
    repo.remotes.origin.fetch()

    # Reset the local branch to the latest commit from the remote repository
    repo.head.reset(index=True, working_tree=True)

    # Pull the changes into the working directory
    repo.remotes.origin.pull()

