# Experiments

Companion code and notebooks for the case studies in:

> Cabral, J. B., Giarda, G., Gimenez Irusta, D. N., Pacheco, P., Schachner,
> A. R., & Borda, A. *Algorithmic Detection of Rank Reversals, Transitivity
> Violations, and Decomposition Inconsistencies in Multi-Criteria Decision
> Analysis*.

The paper introduces `RankInvariantChecker` (RRT1) and
`RankTransitivityChecker` (RRT2/RRT3), two algorithmic implementations of
Wang and Triantaphyllou's (2008) rank reversal test criteria, built on top
of [`scikit-criteria`](https://github.com/quatrope/scikit-criteria). This
folder reproduces the two case studies used to illustrate them.

## Contents

- **`case1.ipynb`** — Case 1: TOPSIS robustness on a cryptocurrency
  evaluation dataset (Van Heerden 2021). Applies RRT1 and RRT2/RRT3 to a
  TOPSIS pipeline over two decision matrices (7- and 15-day return/risk
  windows) for nine cryptocurrencies, showing that a pipeline can be fully
  stable under RRT1 while still violating transitivity under RRT2/RRT3.

- **`case2.ipynb`** — Case 2: prevalence of rank reversal across published
  MCDM examples. Reproduces 27 worked examples drawn from 20 published
  MCDM methods (CODAS, COPRAS, EDAS, ERVD, MABAC, MOORA, OCRA, PROBID,
  RAM, SPOTIS, TOPSIS, VIKOR, WASPAS, among others), each with its
  originally published preprocessing, and runs RRT1-RRT3 uniformly across
  all of them to measure how often rank reversal actually occurs in the
  literature's own reference cases.

- **`all_dm.py`** — Collection of the decision matrices used in Case 2,
  one function per matrix, each with a reference to the paper it was
  extracted from.

- **`all_pipelines.py`** — Maps every matrix in `all_dm.py` to the exact
  preprocessing pipeline (scalers, objective inverters, method-specific
  parameters) used by that paper's original authors, so each example can
  be reproduced with a single `pipeline.evaluate(dm)` call.

## Reproducing

```
pip install -r requirements.txt
```

Both notebooks are executed as part of the paper's build (see the
`images` target in the top-level `Makefile`), which runs them with
`jupyter nbconvert --execute --inplace`.
