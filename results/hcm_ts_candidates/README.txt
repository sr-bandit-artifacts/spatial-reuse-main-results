HCM-TS FRESH-PROPOSAL LIMIT: 128 AND 256

Recorded 2026-10-07: three topologies, physical seeds 1--25, 150 simulated seconds.
The main performance dataset now uses HCM-TS with floor_novel_candidates=256.
The retained 128 reference matrices are in reference/data/.
The 256 matrices are in ../performance/data/, under hcm_ts_* filenames.
The Neural HCM and QNN HCM comparison data are also in ../performance/data/.
summary.csv, per_seed.csv, paired_contrasts.csv and comparison_table.tex are the
supplied comparison outputs. Figures/ contains six PDF and six PNG panels.

Only the HCM-TS exploration-floor fresh-proposal limit changes from 128 to 256.
The candidate cap is 512, epsilon_f is 0.1, native TS epsilon is 0.1,
HCM global epsilon is 0.0, and cold-start is 20.
Equal fresh-proposal limits do not make controller acquisition procedures identical.
Paired intervals use 10,000 percentile bootstrap samples, seed 20261007,
and are individual, exploratory, unadjusted comparisons.

Replay HCM-TS256 from the repository root after building ns-3:
  python scripts/run_main.py --methods hcm_ts --jobs 8 --run-id hcm_ts256
Generate the main tables and figures:
  python scripts/analyze_main.py --output-dir work/tables
  python scripts/reproduce_figures.py --output-dir work/Figures
