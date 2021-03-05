#!/usr/bin/python3

import tempfile
import os
import sys

REPO_ENV_NAME = sys.argv[1]
SHADOW_ENV_NAME = sys.argv[2]

REPO = os.getenv(REPO_ENV_NAME)
SHADOW = os.getenv(SHADOW_ENV_NAME)

CLONE =  "git clone --mirror %s %s/.git"
RENAME = "git remote rename origin origin-old"
ADD =    "git remote add origin %s"
PUSH_ALL = "git push -u origin --all"
PUSH_TAGS = "git push -u origin --tags"

with tempfile.TemporaryDirectory() as tdname:
    print(tdname)
    print("Cloning", REPO)
    os.system(CLONE % (REPO, tdname))
    os.chdir(tdname)
    os.system(RENAME)

    print("Adding new upstream", SHADOW)
    os.system(ADD % SHADOW)

    print("pushing")
    os.system(PUSH_ALL)
    os.system(PUSH_TAGS)
