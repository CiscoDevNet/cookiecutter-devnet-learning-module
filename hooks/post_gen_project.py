import os
import shutil


# cookiecutter doesn't easily support nested templated directories,
# so we patch it here.  this script executes with the generated cookiecutter
# as the working directory
root_files = ['Makefile', 'README.md', 'contributing.md']
files = os.listdir('.')
lab_name = '{{ cookiecutter.lab_name }}'
dest = 'labs/{}'.format(lab_name)
if not os.path.exists(dest):
    os.makedirs(dest)
for f in files:
    if f not in root_files:
        shutil.move(f, dest)
