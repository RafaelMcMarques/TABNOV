"""Simple adapter, only calls the experiement script for now"""

from pathlib import Path
import runpy


if __name__ == "__main__":
    experiment = Path(__file__).resolve().parents[3] / "models/TabPFNu/density_estimation_outlier_detection.py"
    runpy.run_path(str(experiment), run_name="__main__")
