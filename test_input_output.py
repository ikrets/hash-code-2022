import os

os.environ["PYTHONPATH"] = ".."

from pathlib import Path
import input_output

def test_read_files():
    for name in Path("files").glob("*.txt"):
        with name.open("r") as fp:
            problem = input_output.read_file(fp)
            