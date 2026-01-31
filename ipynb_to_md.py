"""Convert ipynb to markdown"""

import subprocess
from pathlib import Path
import argparse


def convert_ipynb_to_md(root_dir: str):
    """
    Convert ipynb notebooks to markdown
    """
    root_path = Path(root_dir)

    if not root_path.exists():
        raise FileNotFoundError(f"Path does not exist: {root_dir}")

    for ipynb_file in root_path.rglob("*.ipynb"):
        md_file = ipynb_file.with_suffix(".md")

        print(f"Converting: {ipynb_file}")

        try:
            subprocess.run(
                [
                    "jupyter",
                    "nbconvert",
                    "--to",
                    "markdown",
                    str(ipynb_file),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            if md_file.exists():
                print(f"✅ Saved: {md_file}")
            else:
                print(f"⚠️ Markdown not found for {ipynb_file}")

        except subprocess.CalledProcessError as e:
            print(f"❌ Failed: {ipynb_file}")
            print(e)


def parse_args():
    """
    Parse arguements
    """
    parser = argparse.ArgumentParser(
        description="Convert all .ipynb files to .md recursively"
    )

    parser.add_argument(
        "path",
        type=str,
        help="Root folder path containing Jupyter notebooks",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    convert_ipynb_to_md(args.path)
