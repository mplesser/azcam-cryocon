# pull all azcam repos to github

import os
import subprocess

commands = [
    "python setup.py clean --all",
    "python setup.py sdist bdist_wheel",
    "twine upload --repository testpypi dist/*",
]

folder = os.path.abspath(os.curdir)
print("\n==>", folder)

cmd = f"rmdir /s /q {os.path.basename(folder)}.egg-info"
p = subprocess.Popen(cmd, shell=True, cwd=folder)
p.wait()
cmd = f"rmdir /s /q dist"
p = subprocess.Popen(cmd, shell=True, cwd=folder)
p.wait()

for cmd in commands:
    p = subprocess.Popen(cmd, shell=True, cwd=folder)
p.wait()
