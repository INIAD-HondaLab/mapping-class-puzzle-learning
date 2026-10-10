#!/usr/bin/env python3
"""
Reproduce the word-length-penalty sensitivity analysis in the revised paper.

The reported experiments use lambda = 0.  This script does not retrain any
model; it uses the already obtained baseline candidate-wise validation losses.
"""
from pathlib import Path
import itertools
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INFILE = ROOT / "results" / "baseline" / "candidate_validation_losses.csv"
OUTFILE = ROOT / "results" / "paper_tables" / "table5_lambda_sensitivity.csv"

df = pd.read_csv(INFILE)

def score(row, lam):
    return row.validation_loss + lam * row.word_length

def lower_envelope(group):
    # All nonnegative pairwise line intersections.
    points = {0.0}
    rows = list(group.itertuples(index=False))
    for a, b in itertools.combinations(rows, 2):
        dl = a.word_length - b.word_length
        if dl == 0:
            continue
        x = (b.validation_loss - a.validation_loss) / dl
        if x >= 0 and np.isfinite(x):
            points.add(float(x))
    pts = sorted(points)

    # Identify the minimizer on each open interval and at lambda=0.
    probes = [0.0]
    for x, y in zip(pts[:-1], pts[1:]):
        probes.append((x + y) / 2.0)
    if pts:
        probes.append(pts[-1] + max(1.0, pts[-1]))

    path = []
    for lam in probes:
        scores = [(score(r, lam), r.candidate) for r in rows]
        cand = min(scores)[1]
        if not path or path[-1] != cand:
            path.append(cand)
    return path

records = []
for (learner, sampling), g in df.groupby(["learner", "sampling"], sort=False):
    by = g.set_index("candidate")
    ab_to_b = float(by.loc["B", "validation_loss"] - by.loc["AB", "validation_loss"])
    b_to_id = float(by.loc["id", "validation_loss"] - by.loc["B", "validation_loss"])
    path = lower_envelope(g)

    assert ab_to_b < b_to_id, (learner, sampling, ab_to_b, b_to_id)
    assert path[:3] == ["AB", "B", "id"], (learner, sampling, path)

    records.append({
        "learner": learner,
        "sampling": sampling,
        "lambda_AB_to_B": ab_to_b,
        "lambda_B_to_id": b_to_id,
        "lower_envelope_path": "AB -> B -> id",
    })

out = pd.DataFrame(records)
out.to_csv(OUTFILE, index=False)
print(out.to_string(index=False))
print(f"\nWrote {OUTFILE}")
