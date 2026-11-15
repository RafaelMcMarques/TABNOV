# Tabular Foundation Models for Novelty Detection (TABNOV)

A repository for exploring, reviewing, and benchmarking **Tabular Foundation Models (TABFMs)** applied to **novelty detection**. **Under development:** the benchmark interfaces and workflow are still evolving.

The benchmark runs each model through an adapter in a separate Python environment.
This keeps model dependencies isolated and separates benchmark integration from model implementations.

## Running

From the repository root, create and activate the project environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Select the models to run in `configs/benchmark.yaml`. Each model has a configuration
in `configs/models/` defining its environment, requirements, and adapter.

Set up the selected models, then run them:

```sh
python scripts/setup_models.py
python src/benchmark/runner.py
```

The project environment runs the setup and benchmark scripts. Setup creates a separate
environment for each selected model and installs its dependencies. The runner launches
each adapter with that model's Python interpreter, so model environments do not need
to be activated manually. Rerun setup when adding models or changing their requirements.

## Project Structure

- **`configs/`**: Benchmark model selection and individual model configurations.
- **`src/benchmark/`**: Benchmark runner and model adapters.
- **`models/`**: Model source code and run scripts.
- **`environments/`**: Model dependency specifications and isolated environments.
- **`scripts/`**: Model environment setup.
- **`docs/`**: Literature review, notes, and references.
- **`requirements.txt`**: Project environment dependencies.
