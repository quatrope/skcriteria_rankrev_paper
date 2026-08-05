#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: BSD-3 (https://tldrlegal.com/license/bsd-3-clause-license-(revised))
# Copyright (c) 2016-2021, Cabral, Juan; Luczywo, Nadia
# Copyright (c) 2022-2025 QuatroPe
# All rights reserved.

# =============================================================================
# DOCS
# =============================================================================

"""Academic pipelines matching the decision matrices in `all_dm.py`.

Every matrix in `all_dm.py` was extracted from a test in `tests/agg/*.py`
that reproduces a published paper. In those tests, the matrix is not
evaluated as-is: it is normally run through the same preprocessing steps
(scalers, objective inverters, etc.) the paper's authors used before being
fed to the aggregator.

This module ties each `all_dm` matrix back to that exact pipeline, so it
can be reproduced with a single call::

    pipeline, dm = get_pipeline_and_data("topsis_tzeng2011multiple")
    result = pipeline.evaluate(dm)

`pipeline` is always an object exposing `.evaluate(dm)`. Depending on the
case it is:

- a bare aggregator (e.g. `EDAS()`), when the original test applies no
  preprocessing;
- a `skcriteria.pipelines.SKCPipeline` (built with `mkpipe`), when the
  test chains one or more transformers before the aggregator;
- a dict of `{variant_name: pipeline}`, when the paper's matrix is shared
  by more than one aggregator (e.g. the four MOORA variants, or
  PROBID/SimplifiedPROBID).

A handful of methods (SPOTIS, ARAS, RIM, SIMUS, ERVD) need extra keyword
arguments at evaluate() time (bounds, ideal, ranges, etc.) that a plain
pipeline has no way to carry, since `SKCPipeline.evaluate` only takes `dm`.
For those, the pipeline is wrapped in `_EvaluateWithKwargs`, which
pre-binds the extra kwargs so `.evaluate(dm)` still works uniformly.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np

import skcriteria
from skcriteria.core.objectives import Objective
from skcriteria.pipelines import mkpipe

from skcriteria.preprocessing.invert_objectives import (
    BenefitCostInverter,
    InvertMinimize,
    MinMaxInverter,
)
from skcriteria.preprocessing.scalers import SumScaler, VectorScaler

from skcriteria.agg.aras import ARAS
from skcriteria.agg.cocoso import CoCoSo
from skcriteria.agg.codas import CODAS
from skcriteria.agg.copras import COPRAS
from skcriteria.agg.edas import EDAS
from skcriteria.agg.ervd import ERVD
from skcriteria.agg.mabac import MABAC
from skcriteria.agg.moora import (
    FullMultiplicativeForm,
    MultiMOORA,
    RatioMOORA,
    ReferencePointMOORA,
)
from skcriteria.agg.ocra import OCRA
from skcriteria.agg.probid import PROBID, SimplifiedPROBID
from skcriteria.agg.ram import RAM
from skcriteria.agg.rim import RIM
from skcriteria.agg.simus import SIMUS
from skcriteria.agg.spotis import SPOTIS
from skcriteria.agg.topsis import TOPSIS
from skcriteria.agg.vikor import VIKOR
from skcriteria.agg.waspas import WASPAS

import all_dm


# =============================================================================
# HELPERS
# =============================================================================


class _EvaluateWithKwargs:
    """Pre-bind extra ``evaluate()`` keyword arguments to a decision-maker.

    `SKCPipeline.evaluate` (and the plain ``evaluate(dm)`` interface this
    module exposes) only forwards ``dm``. Some methods, however, need extra
    arguments at evaluation time (e.g. SPOTIS' ``bounds``/``isp``, ARAS'
    ``ideal``, RIM's ``ref_ideals``/``ranges``, SIMUS' ``b`` or ERVD's
    ``reference_points``). This wrapper closes over those kwargs so the
    result can still be called as ``pipeline.evaluate(dm)``.
    """

    def __init__(self, dmaker, **evaluate_kwargs):
        self._dmaker = dmaker
        self._evaluate_kwargs = evaluate_kwargs

    def evaluate(self, dm):
        return self._dmaker.evaluate(dm, **self._evaluate_kwargs)

    def transform(self, dm):
        return dm

    def __repr__(self):
        kwargs = ", ".join(self._evaluate_kwargs)
        return f"{type(self._dmaker).__name__}(...).evaluate(dm, {kwargs})"


class _ArasDropIdealRow:
    """Drops the paper's first "ideal" row and rebuilds the dm.

    Balezentiene & Kusta (2012) list the ideal solution as the first row
    of the matrix; ARAS needs it passed separately as ``ideal`` and the
    remaining rows re-assembled as a fresh decision matrix.
    """

    def transform(self, dm):
        return skcriteria.mkdm(
            matrix=dm.matrix.to_numpy()[1:],
            objectives=dm.objectives,
            weights=dm.weights,
        )


class _WaspasMinMaxRatioNormalize:
    """Cost/benefit ratio normalization used by Chakraborty et al. (2015).

    Divides cost criteria by `min/x` and benefit criteria by `x/max`,
    turning every criterion into a maximization one in [0, 1]. This is not
    one of skcriteria's standard scalers, so it is reproduced by hand here.
    """

    def transform(self, dm):
        matrix = dm.matrix.to_numpy().astype(float).copy()
        for j, objective in enumerate(dm.objectives):
            column = matrix[:, j]
            if objective == Objective.MIN:
                matrix[:, j] = np.min(column) / column
            else:
                matrix[:, j] = column / np.max(column)
        return skcriteria.mkdm(
            matrix=matrix,
            objectives=[max] * matrix.shape[1],
            weights=dm.weights.to_numpy(),
            alternatives=dm.alternatives,
            criteria=dm.criteria,
        )


# =============================================================================
# TOPSIS
# =============================================================================


def _topsis_tzeng2011():
    dm = all_dm.topsis_tzeng2011multiple()
    pipeline = mkpipe(VectorScaler(target="matrix"), TOPSIS())
    return pipeline, dm


# =============================================================================
# VIKOR
# =============================================================================


def _vikor_tzeng2011():
    dm = all_dm.vikor_tzeng2011()
    return VIKOR(), dm


def _vikor_opricovic2004():
    dm = all_dm.vikor_opricovic2004compromise()
    return VIKOR(), dm


def _vikor_opricovic2007():
    dm = all_dm.vikor_opricovic2007extended()
    return VIKOR(use_compromise_set=False), dm


# =============================================================================
# CODAS
# =============================================================================


def _codas_badi2017():
    dm = all_dm.codas_badi2017()
    pipeline = mkpipe(BenefitCostInverter(), CODAS())
    return pipeline, dm


def _codas_badi2018():
    dm = all_dm.codas_badi2018()
    pipeline = mkpipe(BenefitCostInverter(), CODAS())
    return pipeline, dm


def _codas_bakir2018():
    dm = all_dm.codas_bakir2018()
    pipeline = mkpipe(BenefitCostInverter(), CODAS())
    return pipeline, dm


def _codas_baki2022():
    dm = all_dm.codas_baki2022()
    pipeline = mkpipe(BenefitCostInverter(), CODAS())
    return pipeline, dm


def _codas_turskis2016():
    dm = all_dm.codas_turskis2016()
    pipeline = mkpipe(BenefitCostInverter(), CODAS())
    return pipeline, dm


# =============================================================================
# EDAS
# =============================================================================


def _edas_mathew2018():
    dm = all_dm.edas_mathew2018()
    return EDAS(), dm


def _edas_ersoy2021():
    dm = all_dm.edas_ersoy2021()
    return EDAS(), dm


def _edas_sharma2021():
    dm = all_dm.edas_sharma2021()
    return EDAS(), dm


def _edas_karabasevic2018():
    dm = all_dm.edas_karabasevic2018()
    return EDAS(), dm


# =============================================================================
# MOORA (RatioMOORA, ReferencePointMOORA, FullMultiplicativeForm, MultiMOORA)
# =============================================================================


def _moora_kracka2010():
    dm = all_dm.moora_kracka2010ranking()
    pipelines = {
        "RatioMOORA": mkpipe(VectorScaler(target="matrix"), RatioMOORA()),
        "ReferencePointMOORA": mkpipe(
            VectorScaler(target="matrix"), ReferencePointMOORA()
        ),
        "FullMultiplicativeForm": mkpipe(
            VectorScaler(target="matrix"), FullMultiplicativeForm()
        ),
        "MultiMOORA": mkpipe(VectorScaler(target="matrix"), MultiMOORA()),
    }
    return pipelines, dm


# =============================================================================
# MABAC
# =============================================================================


def _mabac_pamucar2014():
    dm = all_dm.mabac_pamucar2014()
    pipeline = mkpipe(MinMaxInverter(), MABAC())
    return pipeline, dm


# =============================================================================
# CoCoSo
# =============================================================================


def _cocoso_yazdani2019():
    dm = all_dm.cocoso_yazdani2019()
    return CoCoSo(0.5), dm


# =============================================================================
# SPOTIS
# =============================================================================


def _spotis_dezert2020_example_a():
    dm = all_dm.spotis_dezert2020_example_a()
    bounds = np.array([[-5, 12], [-6, 10], [-8, 5]])
    isp = np.array([12, -6, 5])
    pipeline = _EvaluateWithKwargs(SPOTIS(), bounds=bounds, isp=isp)
    return pipeline, dm


def _spotis_dezert2020_example_b():
    dm = all_dm.spotis_dezert2020_example_b()
    bounds = np.array([[14000, 16000], [3, 8], [80, 140], [35, 60], [650, 1300]])
    isp = np.array([14000, 3, 80, 60, 1300])
    pipeline = _EvaluateWithKwargs(SPOTIS(), bounds=bounds, isp=isp)
    return pipeline, dm


# =============================================================================
# PROBID
# =============================================================================


def _probid_wang2021():
    dm = all_dm.probid_wang2021original()
    pipelines = {
        "SimplifiedPROBID": SimplifiedPROBID(),
        "PROBID": PROBID(),
    }
    return pipelines, dm


# =============================================================================
# COPRAS
# =============================================================================


def _copras_uysal2022():
    dm = all_dm.copras_uysal2022assistants()
    pipeline = mkpipe(SumScaler(target="matrix"), COPRAS())
    return pipeline, dm


def _copras_wieckowski2022():
    dm = all_dm.copras_wieckowski2022criteriamethodscomparison()
    pipeline = mkpipe(SumScaler(target="matrix"), COPRAS())
    return pipeline, dm


# =============================================================================
# WASPAS
# =============================================================================


def _waspas_chakraborty2015():
    dm = all_dm.waspas_chakraborty2015applications()
    # The paper's test sweeps lambda_value across 0..1; 0.5 is used here as
    # a representative value.
    pipeline = mkpipe(_WaspasMinMaxRatioNormalize(), WASPAS(lambda_value=0.5))
    return pipeline, dm


# =============================================================================
# ARAS
# =============================================================================


def _aras_balezentiene2012():
    dm = all_dm.aras_balezentiene2012reducing()
    ideal = [
        0.15462598,
        0.17361968,
        0.10925307,
        0.143316,
        0.18535168,
        0.12721927,
    ]
    pipeline = mkpipe(
        InvertMinimize(),
        SumScaler(target="matrix"),
        _ArasDropIdealRow(),
        _EvaluateWithKwargs(ARAS(), ideal=ideal),
    )
    return pipeline, dm


# =============================================================================
# OCRA
# =============================================================================


def _ocra_isik2016():
    dm = all_dm.ocra_isik2016()
    return OCRA(), dm


# =============================================================================
# ERVD
# =============================================================================


def _ervd_shyur2015():
    dm = all_dm.ervd_shyur2015multiple()
    raw_matrix = dm.matrix.to_numpy()
    reference_points = np.ones(raw_matrix.shape[1]) * 80 / np.sum(
        raw_matrix, axis=0
    )
    pipeline = mkpipe(
        SumScaler(target="matrix"),
        _EvaluateWithKwargs(ERVD(), reference_points=reference_points),
    )
    return pipeline, dm


# =============================================================================
# RAM
# =============================================================================


def _ram_sotoudeh2023():
    dm = all_dm.ram_sotoudeh2023()
    pipeline = mkpipe(SumScaler(target="both"), RAM())
    return pipeline, dm


# =============================================================================
# RIM
# =============================================================================


def _rim_example():
    dm = all_dm.rim_example()
    ranges = [(23, 60), (0, 15), (0, 10), (1, 3), (1, 3), (1, 5)]
    ref_ideals = [(30, 35), (10, 15), (0, 0), (3, 3), (3, 3), (4, 5)]
    pipeline = _EvaluateWithKwargs(
        RIM(), ref_ideals=ref_ideals, ranges=ranges
    )
    return pipeline, dm


# =============================================================================
# SIMUS
# =============================================================================


def _simus_munier2024():
    dm = all_dm.simus_munier2024()
    b = [None, 500, None, None]
    pipeline = _EvaluateWithKwargs(SIMUS(), b=b)
    return pipeline, dm


# =============================================================================
# REGISTRY / PUBLIC API
# =============================================================================

_PIPELINE_FACTORIES = {
    "topsis_tzeng2011multiple": _topsis_tzeng2011,
    "vikor_tzeng2011": _vikor_tzeng2011,
    "vikor_opricovic2004compromise": _vikor_opricovic2004,
    "vikor_opricovic2007extended": _vikor_opricovic2007,
    "codas_badi2017": _codas_badi2017,
    "codas_badi2018": _codas_badi2018,
    "codas_bakir2018": _codas_bakir2018,
    "codas_baki2022": _codas_baki2022,
    "codas_turskis2016": _codas_turskis2016,
    "edas_mathew2018": _edas_mathew2018,
    "edas_ersoy2021": _edas_ersoy2021,
    "edas_sharma2021": _edas_sharma2021,
    "edas_karabasevic2018": _edas_karabasevic2018,
    "moora_kracka2010ranking": _moora_kracka2010,
    "mabac_pamucar2014": _mabac_pamucar2014,
    #"cocoso_yazdani2019": _cocoso_yazdani2019,
    #"spotis_dezert2020_example_a": _spotis_dezert2020_example_a,
    "spotis_dezert2020_example_b": _spotis_dezert2020_example_b,
    "probid_wang2021original": _probid_wang2021,
    "copras_uysal2022assistants": _copras_uysal2022,
    "copras_wieckowski2022criteriamethodscomparison": _copras_wieckowski2022,
    "waspas_chakraborty2015applications": _waspas_chakraborty2015,
    #"aras_balezentiene2012reducing": _aras_balezentiene2012,
    "ocra_isik2016": _ocra_isik2016,
    "ervd_shyur2015multiple": _ervd_shyur2015,
    "ram_sotoudeh2023": _ram_sotoudeh2023,
    #"rim_example": _rim_example,
    #"simus_munier2024": _simus_munier2024,
}


def get_pipeline_and_data(name):
    """Return the `(pipeline, dm)` pair reproducing a paper from `all_dm`.

    Parameters
    ----------
    name : str
        Name of one of the functions in `all_dm.get_all_matrices()`
        (e.g. ``"topsis_tzeng2011multiple"``).

    Returns
    -------
    pipeline
        An object exposing ``evaluate(dm)``. For matrices shared by more
        than one aggregator (e.g. the MOORA variants), this is instead a
        dict of ``{variant_name: pipeline}``.
    dm : skcriteria.DecisionMatrix
        The decision matrix returned by `all_dm.<name>`, ready to be fed
        into `pipeline`.

    Examples
    --------
    >>> pipeline, dm = get_pipeline_and_data("topsis_tzeng2011multiple")
    >>> pipeline.evaluate(dm)

    >>> pipelines, dm = get_pipeline_and_data("moora_kracka2010ranking")
    >>> pipelines["RatioMOORA"].evaluate(dm)
    """
    try:
        factory = _PIPELINE_FACTORIES[name]
    except KeyError:
        raise ValueError(
            f"No pipeline registered for {name!r}. "
            f"Available names: {sorted(_PIPELINE_FACTORIES)}"
        ) from None
    return factory()


def list_available_pipelines():
    """Return the sorted list of names accepted by `get_pipeline_and_data`."""
    return sorted(_PIPELINE_FACTORIES)
