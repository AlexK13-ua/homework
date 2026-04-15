import os

folder = "\\MyProjects\\School\\venv\\test1"

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    if os.path.isfile(file_path):
        os.unlink(file_path)