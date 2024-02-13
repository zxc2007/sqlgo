"""
# SQLGO License - Version 1.1

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
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

