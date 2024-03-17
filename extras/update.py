#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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
from src.logger.log import logger
from extras.logo import logo

def updateFromGit():
    try:
        print(logo)
        repository_url = "https://github.com/HeisenbergCipherCracker/sqlgo.git"
        local_path = os.getcwd()
        logger.info("Updating to latest version from git...")

        try:
            repo = git.Repo(local_path)
        except git.NoSuchPathError:
            repo = git.Repo.clone_from(repository_url, local_path)

        repo.remotes.origin.fetch()

        repo.head.reset(index=True, working_tree=True)

        repo.remotes.origin.pull()
    except:
        os.system("git pull")

