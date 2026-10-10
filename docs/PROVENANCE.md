# Provenance and cleanup notes

Source archive used to build this draft: `02_results_in-20260925T005102Z-1-001.zip`.

The public-facing notebooks are renamed copies of the following research notebooks:

- `baseline/pnn_uniform.ipynb` <- `02_results_in/mcg/NN_unif.ipynb`
- `baseline/pnn_gaussian_mixture.ipynb` <- `02_results_in/mcg/NN_gauss.ipynb`
- `baseline/pal_uniform.ipynb` <- `02_results_in/mcg/pal_unif2.ipynb`
- `baseline/pal_gaussian_mixture.ipynb` <- `02_results_in/mcg/pal_gauss.ipynb`
- `robustness/multiple_hidden_words.ipynb` <- `02_results_in/multiple_words_20260923/multiple_hidden_words_pnn_5seeds.ipynb`
- `robustness/residual_amplitude.ipynb` <- `02_results_in/_epsilon_20260922/residual_amplitude_sweep_pnn_5seeds.ipynb`
- `robustness/exact_flow.ipynb` <- `02_results_in/2026-0924/exact_flow_focused_5seed_R2_1.ipynb`
- `robustness/observation_noise.ipynb` <- `02_results_in/noisy validation loss/observation_noise_sweep_pnn_5seeds.ipynb`
- `robustness/pal_observation_noise.ipynb` <- five-seed PAL observation-noise notebook added during the revision experiments

Packaging changes only:

- notebook outputs and execution counts were cleared;
- Colab `/content/...` output paths were replaced by repository-relative `results/...` paths;
- the public/default word-length parameter was changed from the legacy exploratory value `1e-7` to `0.0`, matching the revised manuscript;
- the obsolete artificial word-penalty auxiliary notebook was intentionally excluded;
- duplicate `.ipynb_checkpoints` and duplicate diagnostic notebooks were intentionally excluded;
- the older `pal-unif.ipynb` was excluded in favor of `pal_unif2.ipynb`, whose reported values match the manuscript baseline PAL results.

No model architecture, training budget, target definition, candidate set, random-seed design, or numerical integrator was intentionally changed by this packaging pass.
