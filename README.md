# Mapping-Class-Group Learning for Diffeomorphisms — reproducibility code

This repository contains the numerical code and compact result files accompanying
the manuscript **“Mapping-Class-Group Learning for Diffeomorphisms.”**

All datasets used in the experiments are generated synthetically by the code in
this repository; no external dataset is required.

## Selection rule

The manuscript reports mapping-class selection by **unpenalized
validation loss**, i.e. `lambda = 0`.

Some archived result CSVs originated from exploratory runs that also logged a
reference word-length score with `lambda = 1e-7`. Across the repeated-seed experiments, including the PAL observation-noise
runs, that legacy selector and the unpenalized selector agreed in all 145
individual runs. The public notebooks therefore use `lambda = 0` by default.

## Repository layout

```text
baseline/
  pnn_uniform.ipynb
  pnn_gaussian_mixture.ipynb
  pal_uniform.ipynb
  pal_gaussian_mixture.ipynb

robustness/
  multiple_hidden_words.ipynb
  residual_amplitude.ipynb
  exact_flow.ipynb
  observation_noise.ipynb
  pal_observation_noise.ipynb

analysis/
  lambda_sensitivity.py

results/
  baseline/
  exact_flow/
  observation_noise/
  paper_tables/

docs/
  PROVENANCE.md
  RELEASE_VALIDATION.md
  RESULT_MAPPING.md
  RELEASE_CHECKLIST.md
  SECURITY_SCAN.md
```

## Manuscript-result mapping

| Manuscript result | Reproduction code |
| --- | --- |
| Baseline PNN, uniform | `baseline/pnn_uniform.ipynb` |
| Baseline PNN, Gaussian mixture | `baseline/pnn_gaussian_mixture.ipynb` |
| Baseline PAL, uniform | `baseline/pal_uniform.ipynb` |
| Baseline PAL, Gaussian mixture | `baseline/pal_gaussian_mixture.ipynb` |
| Table 5: lambda sensitivity | `analysis/lambda_sensitivity.py` |
| Table 6: multiple hidden elements | `robustness/multiple_hidden_words.ipynb` |
| Table 7(a): residual-amplitude sweep | `robustness/residual_amplitude.ipynb` |
| Table 7(b): exact-flow stress test | `robustness/exact_flow.ipynb` |
| Table 8: PNN observation-noise sweep | `robustness/observation_noise.ipynb` |
| Table 9: PAL observation-noise sweep | `robustness/pal_observation_noise.ipynb` |

Compact numerical tables are stored under `results/`. See
`docs/RESULT_MAPPING.md` for a direct map from manuscript tables to code and
stored outputs.

## Running the notebooks

Start Jupyter from the **repository root** so that the repository-relative paths
under `results/` are used as intended.

The baseline notebooks were originally executed with PyTorch 2.5.1 and NumPy
2.0.1. The later robustness notebooks recorded PyTorch 2.11.0+cpu and NumPy
2.1.3. Two requirement files are therefore supplied:

```bash
pip install -r requirements-baseline.txt
```

or

```bash
pip install -r requirements-robustness.txt
```

All reported runs are CPU runs. The full repeated-seed robustness experiments
are computationally expensive; the robustness notebooks include `QUICK_TEST`
switches for smoke testing.

Release-validation details, including the smoke-test scope and environment, are
recorded in `docs/RELEASE_VALIDATION.md`.

## Lambda-sensitivity analysis

No retraining is required:

```bash
python analysis/lambda_sensitivity.py
```

The script reads the stored baseline validation losses and verifies the
lower-envelope path

```text
AB -> B -> id
```

for all four baseline settings, including
`lambda_AB_to_B < lambda_B_to_id`.

## Citation

Repository:

`https://github.com/INIAD-HondaLab/mapping-class-puzzle-learning`

Citation metadata are provided in `CITATION.cff`. A Zenodo DOI will be added
after the first GitHub release is archived.

## Data and code availability

All datasets used in this study are generated synthetically by the experiment
code. The source code, scripts, and compact numerical results required to
reproduce the reported experiments are publicly available at

https://github.com/INIAD-HondaLab/mapping-class-puzzle-learning

## License

The source code in this repository is released under the **MIT License**. See
`LICENSE`.
