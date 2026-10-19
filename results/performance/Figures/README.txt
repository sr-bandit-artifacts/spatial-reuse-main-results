MAIN FIGURES — EXPORT 2026-10-07

HCM-TS: exploration-floor fresh-proposal limit 256, candidate cap 512, epsilon_f=0.1.
The current main panels use the 2026-10-07 native HCM-TS256 measurements.

Neural Bandit (HCM): MLP-Norm, hidden width 64, feature dimension 32,
novel_candidates=256, candidate cap=512, epsilon_f=0.1; 25 physical seeds.
Nine main methods, three topologies, four metrics: 12 PDF and 12 PNG panels.
Measurement cycles 0--2000; frozen empirical references retained.
Reward, fairness and throughput: 21-cycle smoothed cross-seed median and IQR.
Cumulative performance loss: unsmoothed cross-seed median of per-seed cumulative loss.
No figure titles; axes 22 pt, ticks and legends 18 pt.

Neural HCM cumulative loss endpoints:
  C6: 24.57274356
  ENT-Clustered: 24.69732864
  ENT-Dispersed: 321.12708704
summary.csv contains the main metric summaries, including starving-STA counts.
loss_endpoints.csv contains all 27 cumulative loss endpoints.
plotted_median_curves.npz contains the 108 median curves in the current main export.
The filename 02_cumulative_regret is retained for manuscript compatibility;
the plotted metric is cumulative performance loss.

Generate new panels from the repository root:
  python scripts/reproduce_figures.py --output-dir work/Figures
