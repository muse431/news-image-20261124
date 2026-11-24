# main.py — entrypoint for news-image-20261124.
# Copies the finished poster (entry.png, drawn by render.py from the day's
# cross-checked news) to the grader's output directory. Standard library
# only, no network, deterministic: both runs write the same bytes.
# The poster itself is the deliverable; this program only places it where
# the grader expects it, so a re-run can never change a pixel.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
