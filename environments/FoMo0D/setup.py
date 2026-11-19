"""Set up pretrained CPU inference as described in docs/fomo-setup.md."""

from pathlib import Path
import subprocess
import sys


DIRECTORY = Path(__file__).resolve().parent
ROOT = DIRECTORY.parents[1]


def main():
    environment = DIRECTORY / ".venv"
    python = environment / "bin" / "python"

    #install dependencies
    subprocess.run([sys.executable, "-m", "venv", str(environment)], check=True)
    subprocess.run(
        [str(python), "-m", "pip", "install", "-r", str(DIRECTORY / "requirements.txt")],
        cwd=ROOT,
        check=True,
    )

    subprocess.run([str(python), "-m", "pip", "check"], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
