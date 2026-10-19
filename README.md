# Run the spatial reuse experiments

## 1. Install the environment

Use Linux with Conda. Clone the repository and run the commands from its root:

```bash
git clone https://github.com/sr-bandit-artifacts/spatial-reuse-main-results.git
cd spatial-reuse-main-results
conda env create -f environment.yml
conda activate spatial-reuse-main
```

For an existing Python 3.10 environment with a C/C++ toolchain:

```bash
python -m pip install --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt
```

## 2. Build ns-3

```bash
python scripts/build_ns3.py --jobs 4
```

## 3. Run the experiments

Short run:

```bash
python scripts/run_main.py --mode smoke --topologies C6o --jobs 1 --run-id smoke_run
```

Full run:

```bash
python scripts/run_main.py --mode full --jobs 4 --run-id main_replay
```

Selected methods, topology and seeds:

```bash
python scripts/run_main.py --mode full --methods neural_hcm qnn_hcm --topologies C6o --seed-start 1 --seed-end 5 --jobs 2 --run-id selected_replay
```

Use `--jobs` to set the number of parallel seeds and `--run-id` to name the run.
Edit `configs/main_experiment.json` to change experiment settings.

## 4. Collect and analyze a full run

Run these commands after the full run completes. Choose a new output directory
if `work/replay_results` already exists.

```bash
python scripts/collect_replay.py --run-id main_replay --output-dir work/replay_results
python scripts/analyze_main.py --results-dir work/replay_results
python scripts/reproduce_figures.py --results-dir work/replay_results --output-dir work/replay_results/Figures
```

## 5. Generate tables and figures from the included data

```bash
python scripts/analyze_main.py --output-dir work/tables
python scripts/reproduce_figures.py --output-dir work/Figures
```

## 6. Run the inference benchmark

```bash
python scripts/benchmark_inference.py --warmup 30 --repetitions 1000 --output-dir work/inference
```
