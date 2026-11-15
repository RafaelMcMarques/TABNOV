"""Run the models selected in configs/benchmark.yaml in isolated environments."""

import argparse
import json
from pathlib import Path
import subprocess

import yaml


ROOT = Path(__file__).resolve().parents[2]


def main():

    #parse args, treats config location at configs/benchmark.yaml as fixed for now
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    benchmark = yaml.safe_load((ROOT / "configs" / "benchmark.yaml").read_text())

    # run each model
    for model in benchmark["models"]:

        #find models configs, including env, reqs and adapter path
        config_path = ROOT / "configs" / "models" / f"{model}.json"
        if not config_path.is_file():
            parser.error(f"Model configuration not found: {config_path}")
        config = json.loads(config_path.read_text())

        #env should be already created and reqs installed
        python = ROOT / config["python_env"] / "bin" / "python"
        if not python.is_file():
            parser.error(
                f"Environment for {model} not found. Run: python scripts/setup_models.py"
            )

        # call the adapter, for now it has no input and output, will have those formatted layer
        result = subprocess.run(
            [str(python), str(ROOT / config["adapter"])], cwd=ROOT
        )
        if result.returncode:
            raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
