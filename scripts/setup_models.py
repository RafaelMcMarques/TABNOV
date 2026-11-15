"""Create environments for the models selected in configs/benchmark.yaml.
    Only venv + pip supported for now, might include uv/conda later
"""

import argparse
import json
from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]


def main():
    #parse args, treats config location at configs/benchmark.yaml as fixed for now
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    benchmark = yaml.safe_load((ROOT / "configs" / "benchmark.yaml").read_text())

    for model in benchmark["models"]:
        config_path = ROOT / "configs" / "models" / f"{model}.json"
        if not config_path.is_file():
            parser.error(f"Model configuration not found: {config_path}")
        config = json.loads(config_path.read_text())
        environment = ROOT / config["python_env"]
        python = environment / "bin" / "python"

        #create env
        subprocess.run([sys.executable, "-m", "venv", str(environment)], check=True)

        #install dependencies
        subprocess.run(
            [str(python), "-m", "pip", "install", "-r", str(ROOT / config["requirements"])],
            cwd=ROOT,
            check=True,
        )


if __name__ == "__main__":
    main()
