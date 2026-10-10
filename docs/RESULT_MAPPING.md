# Result mapping

| Result | Code | Stored compact results |
| --- | --- | --- |
| Baseline candidate-wise PNN/PAL losses | `baseline/*.ipynb` | `results/baseline/candidate_validation_losses.csv` |
| Baseline selected test losses | `baseline/*.ipynb` | `results/baseline/selected_results.csv` |
| Lambda sensitivity / Table 5 | `analysis/lambda_sensitivity.py` | `results/paper_tables/table5_lambda_sensitivity.csv` |
| Multiple hidden elements / Table 6 | `robustness/multiple_hidden_words.ipynb` | `results/paper_tables/table6_multiple_hidden_words.csv` |
| Residual amplitude / Table 7(a) | `robustness/residual_amplitude.ipynb` | `results/paper_tables/table7a_residual_amplitude.csv` |
| Exact flow / Table 7(b) | `robustness/exact_flow.ipynb` | `results/exact_flow/*.csv`, `results/paper_tables/table7b_exact_flow.csv` |
| PNN observation noise / Table 8 | `robustness/observation_noise.ipynb` | `results/observation_noise/*.csv`, `results/paper_tables/table8_observation_noise.csv` |
| PAL observation noise / Table 9 | `robustness/pal_observation_noise.ipynb` | `results/paper_tables/table9_pal_observation_noise.csv` |

The `legacy_*` columns in a few archived/recovered CSVs record the original
exploratory `lambda=1e-7` score or selection.  They are retained only for
auditability; the revised manuscript uses the unpenalized selector.
