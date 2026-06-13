import os

home_dir = os.environ["HOME"]

with open(f"{home_dir}/.ssh/codeberg.pub", "r") as f:
    print(f.read())
