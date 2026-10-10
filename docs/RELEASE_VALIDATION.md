# Release validation

Validation performed on 2026-09-25 before public release.

## Static checks

All eight public notebooks were parsed as valid notebook JSON. Their Python code
cells passed a syntax parse, and no active `/content/...` or Google Drive mount
paths were present. No obvious GitHub-token-like or Google-API-key-like strings
were found in the notebook sources.

The active mapping-class selector in every public notebook is unpenalized
validation loss, i.e. `lambda = 0.0`. Mentions of `1e-7` are explanatory only
and identify the legacy exploratory value.

## Lambda-sensitivity analysis

The following command was run without modifying the script:

```bash
python analysis/lambda_sensitivity.py
```

It completed successfully and reproduced
`results/paper_tables/table5_lambda_sensitivity.csv` exactly. The verified
lower-envelope path was

```text
AB -> B -> id
```

for all four baseline settings.

## Notebook smoke tests

The four robustness notebooks were executed on temporary copies with
`QUICK_TEST=True` and all completed successfully:

- `robustness/multiple_hidden_words.ipynb`
- `robustness/residual_amplitude.ipynb`
- `robustness/exact_flow.ipynb`
- `robustness/observation_noise.ipynb`

The four baseline notebooks were also executed successfully on temporary copies
after reducing sample sizes and training/integration budgets strictly for smoke
testing:

- `baseline/pnn_uniform.ipynb`
- `baseline/pnn_gaussian_mixture.ipynb`
- `baseline/pal_uniform.ipynb`
- `baseline/pal_gaussian_mixture.ipynb`

These smoke tests establish that the public notebooks execute end-to-end; they
are **not** replacements for the canonical full runs reported in the manuscript.

The smoke-test environment was Python 3.13.5, PyTorch 2.10.0+cpu, NumPy 2.3.5,
pandas 2.2.3, and Matplotlib 3.10.8. The versions recorded by the original
canonical runs are documented separately in the repository requirements and
provenance notes.

## Scope

The expensive canonical full experiments were not rerun as part of this release
validation. Their compact numerical outputs are included under `results/`, and
the public notebooks preserve the architectures, target definitions, candidate
sets, seed design, and numerical methods used for those runs.


## Additional validation on 2026-10-10

The PAL observation-noise notebook added during revision was stripped of
execution/user metadata and checked as valid notebook JSON. A reduced smoke-mode
execution completed end-to-end with seed 0, observation-noise levels 0 and 0.05,
40/20/20 train/validation/test samples, 2 training epochs, and 2 RK4 steps.
This smoke test checks code execution only and is not a scientific run.

All nine public notebooks have execution outputs and Colab user/execution
metadata removed in the public-release branch.
