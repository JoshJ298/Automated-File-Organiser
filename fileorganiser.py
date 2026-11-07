
import os
import shutil

path = r"Enter Path:...    "

files = os.listdir(path)

for file in files:
    full_path = os.path.join(path, file)

    if os.path.isfile(full_path):
        filename, extension = os.path.splitext(file)
        extension = extension[1:].lower()

        if not extension:
            continue

        folder = os.path.join(path, extension)

        os.makedirs(folder, exist_ok=True)

        shutil.move(full_path, os.path.join(folder, file))

print("Files organised successfully!")
