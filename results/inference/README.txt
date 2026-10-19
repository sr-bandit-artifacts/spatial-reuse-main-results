MAIN INFERENCE RESULTS

All 12 final seed-1 learned checkpoints were remeasured after the matched Neural reruns.
Four controllers x three topologies x batch sizes 1 and 512 x two timing scopes.
48 groups, 1000 calls each; two blocks with 30 warmups + 500 measurements each.
Neural uses NumPy; QNN uses frozen C++ quantum evolution with a NumPy readout.
Measured CPU: AMD Ryzen 9 9950X3D2 16-Core Processor; affinity: [31]; numerical libraries: one thread.
Model loading, retraining, preparation, compilation, posterior sampling, ns-3 and IPC are excluded.
Native baseline-controller operations remain recorded separately with their own timing scope.
protocol.json pins the exact checkpoints; raw_timings.csv contains all 48000 timing samples.

The archived HCM-TS native latency samples use floor_novel_candidates=128.
The current main performance results use 256. These timings have not been rerun for 256.
