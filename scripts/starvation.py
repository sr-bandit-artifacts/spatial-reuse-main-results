#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 sr-bandit-artifacts
"""Recover the per-cycle number of starving STAs from AP observation logs.

The ``*_agent_state.tsv`` cell contains one observation vector per AP. Its
seventh observation component (index 6, after the leading reward) is the
fraction of that AP's associated STAs below the starvation threshold. The
simulation logs this fraction directly; ``*_stas.tsv`` instead contains STA
throughput values and must not be interpreted as starvation counts.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
TOPOLOGIES = ROOT / "code" / "nsTest" / "topos"
SEEDS = 25
CYCLES = 2001


def topology_associations(topology: str) -> tuple[list[list[int]], int]:
    document = json.loads((TOPOLOGIES / f"{topology}.json").read_text())
    associations = [[int(sta) for sta in ap["stas"]] for ap in document["aps"]]
    total = len(document["stations"])
    flattened = [sta for associated in associations for sta in associated]
    if sorted(flattened) != list(range(total)) or any(not group for group in associations):
        raise ValueError(f"Invalid station associations for topology {topology}")
    if any("cluster" in ap for ap in document["aps"]):
        raise ValueError(f"Clustered AP observations need a different parser: {topology}")
    return associations, total


def count_starving(cell: str, associations: list[list[int]]) -> int:
    agents = cell.split("|")
    if len(agents) != len(associations):
        raise ValueError(f"Expected {len(associations)} AP observations, got {len(agents)}")
    total = 0
    for ap, (agent, stations) in enumerate(zip(agents, associations)):
        agent_id, separator, vector = agent.partition(":")
        if not separator or agent_id != str(ap):
            raise ValueError(f"AP observation order differs at AP {ap}: {agent_id}")
        fields = vector.split(",", 8)
        if len(fields) < 8:
            raise ValueError(f"AP {ap} observation lacks the starvation fraction")
        ratio = float(fields[7])
        if not math.isfinite(ratio):
            raise ValueError(f"Nonfinite starvation fraction for AP {ap}")
        raw = ratio * len(stations)
        count = round(raw)
        if abs(raw - count) > 5e-5 or not 0 <= count <= len(stations):
            raise ValueError(f"AP {ap} starvation fraction {ratio} cannot encode a valid STA count")
        total += count
    return total


def read_starving_matrix(path: Path, topology: str, *, native: bool) -> tuple[np.ndarray, tuple[int, int]]:
    associations, total_stations = topology_associations(topology)
    matrix = np.empty((SEEDS, CYCLES), dtype=np.int16)
    width = None
    seed_index = -1
    with path.open("r", encoding="utf-8") as stream:
        header = stream.readline().rstrip("\r\n").split("\t")
        if len(header) not in (CYCLES, CYCLES + 1) or header[:CYCLES] != [str(i) for i in range(CYCLES)]:
            raise ValueError(f"Invalid measurement-cycle header: {path}")
        for seed_index, line in enumerate(stream):
            if seed_index >= SEEDS:
                raise ValueError(f"Too many physical-seed rows: {path}")
            cells = line.rstrip("\r\n").split("\t")
            if not native and len(cells) != CYCLES:
                raise ValueError(f"Learned AP log requires exactly {CYCLES} cycles: {path}")
            if native and len(cells) not in (CYCLES, CYCLES + 1):
                raise ValueError(f"Native AP log has invalid width {len(cells)}: {path}")
            if width is None:
                width = len(cells)
            elif len(cells) != width:
                raise ValueError(f"AP log mixes row widths: {path}")
            for cycle, cell in enumerate(cells[:CYCLES]):
                count = count_starving(cell, associations)
                if count > total_stations:
                    raise ValueError(f"Invalid starving count at seed {seed_index + 1}, cycle {cycle}")
                matrix[seed_index, cycle] = count
    if seed_index + 1 != SEEDS:
        raise ValueError(f"Expected {SEEDS} physical-seed rows: {path}")
    return matrix, (SEEDS, width)


def write_starving_matrix(path: Path, matrix: np.ndarray) -> None:
    if matrix.shape != (SEEDS, CYCLES):
        raise ValueError(f"Invalid starving matrix shape: {matrix.shape}")
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(path, matrix, fmt="%d", delimiter="\t",
               header="\t".join(map(str, range(CYCLES))), comments="")
