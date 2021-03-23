from pathlib import Path
from time import ctime
import shutil
from zipfile import ZipFile

# path = Path("module/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_suffix(".txt")
# print(path)

# path = Path("module")

# paths = [p for p in path.iterdir() if p.is_dir()]
# pyfiles = [p for p in path.rglob("*.py")]  # glob for non recursive
# print(paths)
# print(pyfiles)

path = Path(r"module\__init__.py")
source = path
target = Path(r"__init__.py")
shutil.copy(source, target)
# path.exists()
# print(ctime(path.stat().st_ctime))
# with open("__init__.py", "r") as file:

# path.read_bytes()
# print(path.read_text())
with ZipFile("files.zip", "w") as zip:
    for path in Path("module").rglob("*.*"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
