MAIN PERFORMANCE RESULTS

Three topologies, nine methods, 25 physical seeds (1--25), measurement cycles 0--2000.
Each data directory contains reward, fairness, aggregate throughput and direct starving-STA count matrices.
The first TSV row is the measurement-cycle header; the subsequent rows are seeds in order 1--25.
Some original exporters append the unused terminal header label 2001; every measured row contains exactly 2,001 values.
Frozen empirical references and all 108 matrix hashes are recorded in protocol.json.
starvation_provenance.json records the archived AP-observation logs used to recover the count matrices.

Run from the repository root:
  python scripts/analyze_main.py
  python scripts/reproduce_figures.py

Figures/ contains the 2026-10-07 HCM-TS256 publication export (12 PDF + 12 PNG panels).
Neural HCM uses MLP-Norm, hidden width 64, feature dimension 32, novel_candidates=256,
candidate cap=512 and epsilon_f=0.1.
Figures/plotted_median_curves.npz stores the median curves from the supplied export.
reproduce_figures.py writes newly rendered panels to reproduced_Figures/ by default.
Table V uses medians of per-seed tail averages for reward, loss, fairness and throughput,
and the cross-seed mean of per-seed tail averages for the starving-STA count.
Table VI uses individual paired percentile bootstrap intervals.
TableIV.tex and parameter_counts.csv describe the two main feature extractors.

HCM-TS now uses floor_novel_candidates=256, candidate cap=512 and epsilon_f=0.1.
The three 25-seed native runs are recorded in hcm_ts256_run_provenance.json.
The supplied 128--256 comparison is in ../hcm_ts_candidates/.
