#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License: BSD-3 (https://tldrlegal.com/license/bsd-3-clause-license-(revised))
# Copyright (c) 2016-2021, Cabral, Juan; Luczywo, Nadia
# Copyright (c) 2022-2025 QuatroPe
# All rights reserved.

# =============================================================================
# DOCS
# =============================================================================

"""Academic Decision Matrices Collection.

This module contains decision matrices extracted from academic papers and
research publications. Each function returns a DecisionMatrix object that
can be used for testing and validating MCDM methods.

The matrices are organized by MCDM method and include complete references
to their original sources.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np
import skcriteria

# =============================================================================
# TOPSIS
# =============================================================================


def topsis_tzeng2011multiple():
    """TOPSIS - Multiple attribute decision making.

    Reference:
        Tzeng, G. H., & Huang, J. J. (2011).
        Multiple attribute decision making: methods and applications.
        CRC press.

    Domain: Generic MCDM problem
    Shape: 4 alternatives × 3 criteria
    """
    # Test: tests/agg/test_topsis.py:76
    return skcriteria.mkdm(
        matrix=[
            [5, 8, 4],
            [7, 6, 8],
            [8, 8, 6],
            [7, 4, 6],
        ],
        objectives=[max, max, max],
        weights=[0.3, 0.4, 0.3],
    )


# =============================================================================
# VIKOR
# =============================================================================


def vikor_tzeng2011():
    """VIKOR - Multiple attribute decision making.

    Reference:
        Tzeng, G. H., & Huang, J. J. (2011).
        Multiple attribute decision making: methods and applications.
        CRC press. (Same data as TOPSIS example)

    Domain: Generic MCDM problem (Durability, Capacity, Reliability)
    Shape: 4 alternatives × 3 criteria
    """
    # Test: tests/agg/test_vikor.py:56
    return skcriteria.mkdm(
        matrix=[
            [5, 8, 4],
            [7, 6, 8],
            [8, 8, 6],
            [7, 4, 6],
        ],
        objectives=[max, max, max],
        weights=[0.3, 0.4, 0.3],
        alternatives=["A1", "A2", "A3", "A4"],
        criteria=["DUR", "CAP", "REL"],
    )


def vikor_opricovic2004compromise():
    """VIKOR - Compromise solution analysis.

    Reference:
        Opricovic, S., & Tzeng, G. H. (2004).
        Compromise solution by MCDM methods:
        A comparative analysis of VIKOR and TOPSIS.
        European Journal of Operational Research, 156(2), 445-455.

    Domain: Risk and altitude assessment
    Shape: 3 alternatives × 2 criteria
    """
    # Test: tests/agg/test_vikor.py:130
    return skcriteria.mkdm(
        matrix=[
            [1.0, 3000.0],
            [2.0, 3750.0],
            [5.0, 4500.0],
        ],
        objectives=[min, max],
        weights=[0.5, 0.5],
        alternatives=["A1", "A2", "A3"],
        criteria=["Risk", "Altitude"],
    )


def vikor_opricovic2007extended():
    """VIKOR - Extended method comparison.

    Reference:
        Opricovic, S., & Tzeng, G. H. (2007).
        Extended VIKOR method in comparison with outranking methods.
        European journal of operational research, 178(2), 514-529.

    Domain: Hydroelectric power plant selection
    Shape: 6 alternatives × 8 criteria
    """
    # Test: tests/agg/test_vikor.py:178
    return skcriteria.mkdm(
        matrix=[
            [4184.3, 2914.0, 407.2, 251.0, 195, 244, 15, 2.41],
            [5211.9, 3630.0, 501.7, 308.3, 282, 346, 21, 1.41],
            [5021.3, 3920.5, 504.0, 278.6, 12, 56, 3, 4.42],
            [5566.1, 3957.9, 559.5, 335.3, 167, 268, 16, 3.36],
            [5060.5, 3293.5, 514.1, 284.2, 69, 90, 7, 4.04],
            [4317.9, 2925.9, 432.8, 239.3, 12, 55, 3, 4.36],
        ],
        objectives=[max, min, max, max, min, min, min, max],
        weights=[0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125],
        alternatives=["A1", "A2", "A3", "A4", "A5", "A6"],
        criteria=[
            "Profit [10e6 Din]",
            "Cost [10e6 Din]",
            "Energy produced [GW hour]",
            "Peak energy produced [GW hour]",
            "Homes to be relocated [Num]",
            "Reservoirs area [ha]",
            "Villages to displace [Num]",
            "Environmental protection [Grade]",
        ],
    )


# =============================================================================
# CODAS
# =============================================================================


def codas_badi2017():
    """CODAS - Supplier selection for multi-criteria decision-making.

    Reference:
        Badi, I., Shetwan, A. G., & Abdulshahed, A. M. (2017, September).
        Supplier selection using COmbinative Distance-based ASsessment (CODAS)
        method for multi-criteria decision-making.
        In Proceedings of the 1st international conference on management,
        engineering and environment (ICMNEE) (pp. 395-407).

    Domain: Supplier selection
    Shape: 6 alternatives × 4 criteria
    """
    # Test: tests/agg/test_codas.py:58
    return skcriteria.mkdm(
        matrix=[
            [45, 3600, 45, 0.9],
            [25, 3800, 60, 0.8],
            [23, 3100, 35, 0.9],
            [14, 3400, 50, 0.7],
            [15, 3300, 40, 0.8],
            [28, 3000, 30, 0.6],
        ],
        objectives=[max, min, max, max],
        weights=[0.2857, 0.3036, 0.2321, 0.1786],
    )


def codas_badi2018():
    """CODAS - Site selection of desalination plant in Libya.

    Reference:
        Badi, I., Ballem, M., & Shetwan, A. (2018).
        SITE SELECTION OF DESALINATION PLANT IN LIBYA BY USING
        COMBINATIVE DISTANCE-BASED ASSESSMENT (CODAS) METHOD.
        International Journal for Quality Research, 12(3).

    Domain: Desalination plant site selection
    Shape: 5 alternatives × 5 criteria
    """
    # Test: tests/agg/test_codas.py:98
    return skcriteria.mkdm(
        matrix=[
            [8, 8, 10, 9, 5],
            [8, 9, 9, 9, 8],
            [9, 9, 7, 8, 6],
            [8, 8, 7, 8, 9],
            [9, 8, 7, 7, 4],
        ],
        objectives=[min, max, max, max, min],
        weights=[0.19, 0.26, 0.24, 0.17, 0.14],
    )


def codas_bakir2018():
    """CODAS - Service quality assessment for airlines.

    Reference:
        BAKIR, M., & ALPTEKİN, N. (2018).
        A new approach in service quality assessment: An application on
        airlines through CODAS method.
        Business & Management Studies: An International Journal, 6(4), 1336.

    Domain: Airline service quality assessment
    Shape: 11 alternatives × 7 criteria
    """
    # Test: tests/agg/test_codas.py:136
    return skcriteria.mkdm(
        matrix=[
            [3.100, 2.714, 2.750, 3.500, 3.167, 2.700, 3.219],
            [3.750, 3.929, 4.000, 3.938, 3.667, 3.750, 3.563],
            [4.750, 4.125, 4.000, 4.800, 4.500, 4.625, 4.800],
            [3.500, 3.250, 3.750, 3.300, 3.000, 3.375, 4.200],
            [3.900, 4.071, 4.125, 4.000, 3.667, 3.000, 3.907],
            [3.500, 4.071, 3.750, 3.688, 3.667, 4.417, 3.625],
            [4.250, 3.571, 3.875, 4.875, 4.500, 3.875, 4.187],
            [2.800, 3.000, 3.000, 3.250, 2.667, 3.500, 3.000],
            [3.750, 4.143, 3.375, 4.000, 3.667, 3.800, 3.687],
            [3.900, 4.214, 4.000, 4.125, 4.000, 4.125, 3.969],
            [3.500, 4.429, 3.750, 3.875, 4.000, 4.100, 3.844],
        ],
        objectives=[max, max, max, max, max, max, max],
        weights=[0.1468, 0.1661, 0.1116, 0.1287, 0.1799, 0.1466, 0.1203],
    )


def codas_baki2022():
    """CODAS - Cloud service provider selection.

    Reference:
        Baki, R. (2022).
        Application of ROC and CODAS techniques for cloud service
        provider selection.
        Gaziantep University Journal of Social Sciences, 21(1), 217-230.

    Domain: Cloud service provider selection
    Shape: 4 alternatives × 8 criteria
    """
    # Test: tests/agg/test_codas.py:194
    return skcriteria.mkdm(
        matrix=[
            [3.464, 2.942, 2.667, 2.936, 3.595, 3.026, 3.659, 3.957],
            [2.749, 3.634, 2.182, 2.804, 2.994, 3.360, 2.182, 3.464],
            [4.263, 3.175, 4.107, 2.621, 2.942, 4.472, 3.772, 3.360],
            [2.621, 2.289, 2.289, 3.634, 2.621, 3.086, 2.289, 2.749],
        ],
        objectives=[max, max, max, max, max, max, max, max],
        weights=[0.11, 0.092, 0.217, 0.02105, 0.198, 0.037, 0.267, 0.058],
    )


def codas_turskis2016():
    """CODAS - A new combinative distance-based assessment method.

    Reference:
        TURSKIS, Z., & ANTUCHEVICIENE, J. (2016).
        A NEW COMBINATIVE DISTANCE-BASED ASSESSMENT (CODAS)
        METHOD FOR MULTI-CRITERIA DECISION-MAKING.

    Domain: Generic MCDM problem
    Shape: 14 alternatives × 6 criteria
    """
    # Test: tests/agg/test_codas.py:232
    return skcriteria.mkdm(
        matrix=[
            [7.6, 46, 18, 390, 0.1, 11],
            [5.5, 32, 21, 360, 0.05, 11],
            [5.3, 32, 21, 290, 0.05, 11],
            [5.7, 37, 19, 270, 0.05, 9],
            [4.2, 38, 19, 240, 0.1, 8],
            [4.4, 38, 19, 260, 0.1, 8],
            [3.9, 42, 16, 270, 0.1, 5],
            [7.9, 44, 20, 400, 0.05, 6],
            [8.1, 44, 20, 380, 0.05, 6],
            [4.5, 46, 18, 320, 0.1, 7],
            [5.7, 48, 20, 320, 0.05, 11],
            [5.2, 48, 20, 310, 0.05, 11],
            [7.1, 49, 19, 280, 0.1, 12],
            [6.9, 50, 16, 250, 0.05, 10],
        ],
        objectives=[max, max, max, max, min, min],
        weights=[0.21, 0.16, 0.26, 0.17, 0.12, 0.08],
    )


# =============================================================================
# EDAS
# =============================================================================


def edas_mathew2018():
    """EDAS - Mobile phone selection.

    Reference:
        Manoj Mathew. (2018, July 17).
        Evaluation Based on Distance from Average Solution - EDAS.
        https://www.youtube.com/watch?v=0ZHz4EeYB2Y

    Domain: Mobile phone selection
    Shape: 5 alternatives × 4 criteria
    """
    # Test: tests/agg/test_edas.py:29
    return skcriteria.mkdm(
        matrix=[
            [250, 16, 12, 5],
            [200, 16, 8, 3],
            [300, 32, 16, 4],
            [275, 32, 8, 4],
            [225, 16, 16, 2],
        ],
        objectives=[min, max, max, max],
        weights=[0.35, 0.25, 0.25, 0.15],
    )


def edas_ersoy2021():
    """EDAS - Notebook selection for e-commerce company.

    Reference:
        Ersoy, Y. (2021).
        Equipment selection for an e-commerce company using Entropy-based
        TOPSIS, EDAS and CODAS methods during the COVID-19.
        LogForum, 17(3).

    Domain: Notebook/laptop selection
    Shape: 6 alternatives × 6 criteria
    """
    # Test: tests/agg/test_edas.py:64
    return skcriteria.mkdm(
        matrix=[
            [256, 8, 41, 1.6, 1.77, 7347.16],
            [256, 8, 32, 1.0, 1.8, 6919.99],
            [256, 8, 53, 1.6, 1.9, 8400],
            [256, 8, 41, 1.0, 1.75, 6808.9],
            [512, 8, 35, 1.6, 1.7, 8479.99],
            [256, 4, 35, 1.6, 1.7, 7499.99],
        ],
        objectives=[max, max, max, max, min, min],
        weights=[0.405, 0.221, 0.134, 0.199, 0.007, 0.034],
    )


def edas_sharma2021():
    """EDAS - Electric motorcycle selection.

    Reference:
        Sharma, R., Ramachandran, M., Saravanan, V., & Nanjundan, P.
        Application of the EDAS Technique for Selecting the Electric
        Motor Vehicles.

    Domain: Electric motorcycle selection
    Shape: 9 alternatives × 5 criteria
    """
    # Test: tests/agg/test_edas.py:101
    return skcriteria.mkdm(
        matrix=[
            [3.20, 150, 80, 129.400, 4.5],
            [2.80, 75, 25, 102.249, 4.5],
            [4.00, 180, 105, 192.499, 5.0],
            [3.60, 200, 80, 114.999, 6.0],
            [2.88, 110, 85, 114.999, 5.0],
            [4.32, 140, 80, 166.250, 6.0],
            [4.40, 200, 100, 99.999, 2.0],
            [3.50, 140, 85, 154.999, 6.0],
            [3.00, 135, 75, 99.999, 3.0],
        ],
        objectives=[max, max, max, min, min],
        weights=[0.2, 0.2, 0.2, 0.2, 0.2],
    )


def edas_karabasevic2018():
    """EDAS - Personnel selection in IT industry.

    Reference:
        Karabasevic, D., Zavadskas, E. K., Stanujkic, D., Popovic, G.,
        & Brzakovic, M. (2018).
        An approach to personnel selection in the IT industry based
        on the EDAS method.
        In Transformations in business & economics
        (Vol. 17, No. 2 (44), pp. 54-65).

    Domain: IT personnel/research assistant selection
    Shape: 6 alternatives × 7 criteria
    """
    # Test: tests/agg/test_edas.py:152
    return skcriteria.mkdm(
        matrix=[
            [5, 4, 3, 4, 4, 5, 3],
            [3, 4, 5, 4, 3, 3, 4],
            [4, 3, 2, 3, 2, 3, 4],
            [3, 3, 3, 4, 4, 3, 4],
            [4, 3, 3, 4, 4, 4, 3],
            [5, 4, 4, 5, 5, 5, 4],
        ],
        objectives=[max, max, max, max, max, max, max],
        weights=[0.31, 0.21, 0.17, 0.13, 0.09, 0.06, 0.03],
    )


# =============================================================================
# MOORA (includes RatioMOORA, ReferencePointMOORA, FMF, MultiMOORA)
# =============================================================================


def moora_kracka2010ranking():
    """MOORA - Ranking heating losses in a building.

    Reference:
        KRACKA, M; BRAUERS, W. K. M.; ZAVADSKAS, E. K. Ranking
        Heating Losses in a Building by Applying the MULTIMOORA . -
        ISSN 1392 - 2785 Inz

    Domain: Building heating losses assessment
    Shape: 6 alternatives × 7 criteria

    Note: This matrix is shared by RatioMOORA, ReferencePointMOORA,
    FullMultiplicativeForm, and MultiMOORA methods.
    """
    # Tests:
    #   tests/agg/test_moora.py:38
    #   tests/agg/test_moora.py:91
    #   tests/agg/test_moora.py:154
    #   tests/agg/test_moora.py:272
    return skcriteria.mkdm(
        matrix=[
            [33.95, 23.78, 11.45, 39.97, 29.44, 167.10, 3.852],
            [38.9, 4.17, 6.32, 0.01, 4.29, 132.52, 25.184],
            [37.59, 9.36, 8.23, 4.35, 10.22, 136.71, 10.845],
            [30.44, 37.59, 13.91, 74.08, 45.10, 198.34, 2.186],
            [36.21, 14.79, 9.17, 17.77, 17.06, 148.3, 6.610],
            [37.8, 8.55, 7.97, 2.35, 9.25, 134.83, 11.935],
        ],
        objectives=[min, min, min, min, max, min, max],
        alternatives=["A1", "A2", "A3", "A4", "A5", "A6"],
        criteria=["x1", "x2", "x3", "x4", "x5", "x6", "x7"],
    )


# =============================================================================
# MABAC
# =============================================================================


def mabac_pamucar2014():
    """MABAC - Transport and handling resources selection in logistics centers.

    Reference:
        Pamucar, D., & Ćirović, G. (2014).
        The selection of transport and handling resources in logistics centers
        using Multi-Attributive Border Approximation area Comparison
        (MABAC).

    Domain: Forklift selection for logistics centers
    Shape: 7 alternatives × 10 criteria
    """
    # Test: tests/agg/test_mabac.py:32
    return skcriteria.mkdm(
        matrix=[
            [22600, 3800, 2, 5, 1.06, 3.00, 3.5, 2.8, 24.5, 6.5],
            [19500, 4200, 3, 2, 0.95, 3.00, 3.4, 2.2, 24.0, 7.0],
            [21700, 4000, 1, 3, 1.25, 3.20, 3.3, 2.5, 24.5, 7.3],
            [20600, 3800, 2, 5, 1.05, 3.25, 3.2, 2.0, 22.5, 11.0],
            [22500, 3800, 4, 3, 1.35, 3.20, 3.7, 2.1, 23.0, 6.3],
            [23250, 4210, 3, 5, 1.45, 3.60, 3.5, 2.8, 23.5, 7.0],
            [20300, 3850, 2, 5, 0.90, 3.25, 3.0, 2.6, 21.5, 6.0],
        ],
        objectives=[min, max, max, max, min, min, max, max, max, max],
        weights=[
            0.146,
            0.144,
            0.119,
            0.121,
            0.115,
            0.101,
            0.088,
            0.068,
            0.050,
            0.048,
        ],
        alternatives=[
            "Forklift 1",
            "Forklift 2",
            "Forklift 3",
            "Forklift 4",
            "Forklift 5",
            "Forklift 6",
            "Forklift 7",
        ],
        criteria=["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"],
    )


# =============================================================================
# CoCoSo
# =============================================================================


def cocoso_yazdani2019():
    """CoCoSo - Combined compromise solution method.

    Reference:
        Yazdani, Morteza and Zaraté, Pascale and Kazimieras Zavadskas,
        Edmundas and Turskis, Zenonas
        A Combined Compromise Solution (CoCoSo) method for multi-criteria
        decision-making problems.
        (2019) Management Decision, 57 (9). 2501-2519. ISSN 0025-1747

    Domain: Generic MCDM problem
    Shape: 7 alternatives × 5 criteria
    """
    # Test: tests/agg/test_cocoso.py:31
    return skcriteria.mkdm(
        matrix=[
            [1, 0, 1, 0.0566, 0.4127],
            [0.067, 0.7813, 0.2303, 1, 0.4563],
            [0.0748, 0.9375, 0.5895, 0.434, 1],
            [0.1304, 0.625, 0.2222, 0.6226, 0.3913],
            [0, 0.9375, 0, 0.0566, 0.3485],
            [0.0348, 1, 0.2303, 0, 0],
            [0.0087, 0.9375, 0.6152, 0.2453, 0.3527],
        ],
        objectives=[max, max, max, max, max],
        weights=[0.036, 0.192, 0.326, 0.326, 0.12],
    )


# =============================================================================
# SPOTIS
# =============================================================================


def spotis_dezert2020_example_a():
    """SPOTIS - Reference example A.

    Reference:
        Dezert, J., Tchamova, A., Han, D., & Tacnet, J. M. (2020, July).
        The SPOTIS rank reversal free method for multi-criteria
        decision-making support. In 2020 IEEE 23rd International Conference
        on Information Fusion (FUSION) (pp. 1-8). IEEE.

    Domain: Generic MCDM problem
    Shape: 4 alternatives × 3 criteria
    """
    # Test: tests/agg/test_spotis.py:36
    return skcriteria.mkdm(
        matrix=[
            [10.5, -3.1, 1.7],
            [-4.7, 0, 3.4],
            [8.1, 0.3, 1.3],
            [3.2, 7.3, -5.3],
        ],
        objectives=[max, min, max],
        weights=[0.2, 0.3, 0.5],
        criteria=["C1", "C2", "C3"],
    )


def spotis_dezert2020_example_b():
    """SPOTIS - Reference example B.

    Reference:
        Dezert, J., Tchamova, A., Han, D., & Tacnet, J. M. (2020, July).
        The SPOTIS rank reversal free method for multi-criteria
        decision-making support. In 2020 IEEE 23rd International Conference
        on Information Fusion (FUSION) (pp. 1-8). IEEE.

    Domain: Generic MCDM problem
    Shape: 4 alternatives × 5 criteria
    """
    # Test: tests/agg/test_spotis.py:66
    return skcriteria.mkdm(
        matrix=[
            [15000, 4.3, 99, 42, 737],
            [15290, 5.0, 116, 42, 892],
            [15350, 5.0, 114, 45, 952],
            [15490, 5.3, 123, 45, 1120],
        ],
        objectives=[min, min, min, max, max],
        weights=[0.2941, 0.2353, 0.2353, 0.0588, 0.1765],
        criteria=["C1", "C2", "C3", "C4", "C5"],
    )


# =============================================================================
# PROBID
# =============================================================================


def probid_wang2021original():
    """PROBID - Preference ranking on the basis of ideal-average distance.

    Reference:
        Wang, Z., Rangaiah, G. P., & Wang, X. (2021).
        Preference ranking on the basis of ideal-average distance method for
        multi-criteria decision-making.
        Industrial & Engineering Chemistry Research, 60(30), 11216–11230.

    Domain: Generic MCDM problem
    Shape: 11 alternatives × 5 criteria

    Note: This matrix is shared by both PROBID and SimplifiedPROBID methods.
    """
    # Tests:
    #   tests/agg/test_probid.py:31
    #   tests/agg/test_probid.py:98
    return skcriteria.mkdm(
        matrix=[
            [0.1299, 0.1754, 0.3256, 0.3255, 0.0892],
            [0.1712, 0.1500, 0.2825, 0.2827, 0.2029],
            [0.1903, 0.1662, 0.3349, 0.3358, 0.0169],
            [0.2207, 0.1772, 0.3450, 0.3449, 0.0488],
            [0.2403, 0.1751, 0.3284, 0.3294, 0.0889],
            [0.2764, 0.1690, 0.2865, 0.2866, 0.1951],
            [0.3041, 0.2274, 0.2719, 0.2723, 0.3481],
            [0.3390, 0.1486, 0.2731, 0.2736, 0.3037],
            [0.3858, 0.1944, 0.3274, 0.3281, 0.2587],
            [0.4251, 0.6560, 0.2618, 0.2593, 0.5786],
            [0.4448, 0.5353, 0.2622, 0.2606, 0.5358],
        ],
        objectives=[max, min, min, min, min],
        weights=[0.1819, 0.2131, 0.1838, 0.1832, 0.2379],
    )


# =============================================================================
# COPRAS
# =============================================================================


def copras_uysal2022assistants():
    """COPRAS - Performance evaluation of research assistants.

    Reference:
        Uysal, Ö., & İnan, T. (2022).
        Performance Evaluation Of Research Assistants By Copras Method.
        International Journal of Social Science and Economic Research.

    Domain: Research assistant performance evaluation
    Shape: 5 alternatives × 7 criteria

    Note: Matrix values should be normalized by sum before use.
    """
    # Test: tests/agg/test_copras.py:32
    return skcriteria.mkdm(
        matrix=[
            [3.57, 4.00, 4.00, 83.75, 3, 9, 1],
            [3.07, 3.95, 4.00, 83.00, 3, 1, 3],
            [3.23, 3.54, 3.46, 66.00, 4, 0, 2],
            [3.42, 3.96, 4.00, 70.00, 5, 5, 7],
            [2.56, 3.37, 3.79, 82.00, 4, 4, 5],
        ],
        objectives=[max, max, max, max, min, max, max],
        weights=[1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7],
        alternatives=["x1", "x2", "x3", "x4", "x5"],
        criteria=[
            "Undergraduate GPA",
            "Master GPA",
            "PhD GPA",
            "Foreign Language",
            "Lesson Completion Duration",
            "Number of Congress",
            "Number of Essays",
        ],
    )


def copras_wieckowski2022criteriamethodscomparison():
    """COPRAS - Multi-criteria methods comparison study.

    Reference:
        Więckowski, J., & Szyjewski, Z. (2022).
        Practical Study of Selected Multi-Criteria Methods Comparison.
        Procedia Computer Science, 207, 4565–4573.
        https://doi.org/10.1016/j.procs.2022.09.520

    Domain: Generic MCDM comparison
    Shape: 7 alternatives × 10 criteria

    Note: Matrix values should be normalized by sum before use.
    """
    # Test: tests/agg/test_copras.py:130
    return skcriteria.mkdm(
        matrix=[
            [3.5, 6.0, 1256.0, 4.0, 16.0, 3.0, 17.3, 8.0, 2.82, 4100.0],
            [3.1, 4.0, 1000.0, 2.0, 8.0, 1.0, 15.6, 5.0, 3.08, 3800.0],
            [3.6, 6.0, 2000.0, 4.0, 16.0, 3.0, 17.3, 5.0, 2.90, 4000.0],
            [3.0, 4.0, 1000.0, 2.0, 8.0, 2.0, 17.3, 5.0, 2.60, 3500.0],
            [3.3, 6.0, 1008.0, 4.0, 12.0, 3.0, 15.6, 8.0, 2.30, 3800.0],
            [3.6, 6.0, 1000.0, 2.0, 16.0, 3.0, 15.6, 5.0, 2.80, 4000.0],
            [3.5, 6.0, 1256.0, 2.0, 16.0, 1.0, 15.6, 6.0, 2.90, 4000.0],
        ],
        objectives=[max, max, max, max, max, max, max, max, min, min],
        weights=[
            0.297,
            0.025,
            0.035,
            0.076,
            0.154,
            0.053,
            0.104,
            0.017,
            0.025,
            0.214,
        ],
    )


# =============================================================================
# WASPAS
# =============================================================================


def waspas_chakraborty2015applications():
    """WASPAS - Applications as a multi-criteria decision-making tool.

    Reference:
        Chakraborty, S., Zavadskas, E. K., & Antucheviciene, J. (2015).
        Applications of WASPAS method as a multi-criteria decision-making tool.
        Economic Computation and Economic Cybernetics Studies and Research,
        49(1), 5-22. Example 2.

    Domain: Generic MCDM problem
    Shape: 10 alternatives × 4 criteria

    Note: Matrix needs normalization before use with WASPAS.
    """
    # Test: tests/agg/test_waspas.py:291
    return skcriteria.mkdm(
        matrix=[
            [581818, 54.49, 3, 5500],
            [595454, 49.73, 3, 4500],
            [586060, 51.24, 3, 5000],
            [522727, 45.71, 3, 5800],
            [561818, 52.66, 3, 5200],
            [543030, 74.46, 4, 5600],
            [522727, 75.42, 4, 5800],
            [486970, 62.62, 4, 5600],
            [509394, 65.87, 4, 6400],
            [513333, 70.67, 4, 6000],
        ],
        objectives=[min, min, min, max],
        weights=[0.467, 0.160, 0.095, 0.278],
        criteria=["PC", "FS", "MN", "P"],
    )


# =============================================================================
# ARAS
# =============================================================================


def aras_balezentiene2012reducing():
    """ARAS - Reducing greenhouse gas emissions in grassland ecosystems.

    Reference:
        Balezentiene, L., & Kusta, A. (2012).
        Reducing Greenhouse Gas Emissions in Grassland Ecosystems of the
        Central Lithuania: Multi-Criteria Evaluation on a Basis of the ARAS
        Method.

    Domain: Grassland management and greenhouse gas emissions
    Shape: 11 alternatives × 6 criteria (includes ideal solution as first row)

    Note: First row contains the ideal solution. Use rows 1-10 for alternatives.
    """
    # Tests:
    #   tests/agg/test_aras.py:33
    #   tests/agg/test_aras.py:161
    return skcriteria.mkdm(
        matrix=[
            [3020.0, 827.6948, 98, 0.015479, 2.166783, 0.0141],  # Ideal
            [957.5, 190.1977, 70, 0.039592, 2.166783, 0.0141],  # Control
            [892.5, 203.8013, 53, 0.025849, 2.994347, 0.016642],  # N_60
            [1002.5, 235.0942, 75, 0.015479, 4.742146, 0.019484],  # N_120
            [1150.0, 271.4, 76, 0.022, 7.055962, 0.022147],  # N_180
            [1520.0, 192.5579, 70, 0.025442, 8.424319, 0.024235],  # N_240
            [
                1700.0,
                386.1619,
                90,
                0.029429,
                5.888983,
                0.022218,
            ],  # N_180 P_120
            [1355.0, 342.1966, 80, 0.0293, 8.635847, 0.024861],  # N_180 K_150
            [
                2127.5,
                495.4876,
                90,
                0.038453,
                3.652983,
                0.020537,
            ],  # N_60 P_40 K_50
            [
                3020.0,
                827.6948,
                97,
                0.031774,
                11.03944,
                0.024359,
            ],  # N_180 P_120 K_150
            [
                2786.0,
                795.0,
                98,
                0.021151,
                8.952235,
                0.023349,
            ],  # CP(N_180 P_120 K_150)
        ],
        objectives=[max, max, max, min, min, min],
        weights=[0.166667, 0.166667, 0.166667, 0.166667, 0.166667, 0.166667],
    )


# =============================================================================
# OCRA
# =============================================================================


def ocra_isik2016():
    """OCRA - Hotel selection problem.

    Reference:
        Işık, A. T., & Adalı, E. A. A new integrated decision making approach
        based on SWARA and OCRA methods for the hotel selection problem. -
        International Journal of Advanced Operations Management (2016).

    Domain: Hotel selection
    Shape: 6 alternatives × 5 criteria
    """
    # Test: tests/agg/test_ocra.py:30
    return skcriteria.mkdm(
        matrix=[
            [7.7, 256, 7.2, 7.3, 7.3],
            [8.1, 250, 7.9, 7.8, 7.7],
            [8.7, 352, 8.6, 7.9, 8.0],
            [8.1, 262, 7.0, 8.1, 7.2],
            [6.5, 271, 6.3, 6.4, 6.1],
            [6.8, 228, 7.1, 7.2, 6.5],
        ],
        objectives=[max, min, max, max, max],
        weights=[0.239, 0.225, 0.197, 0.186, 0.153],
        alternatives=["A1", "A2", "A3", "A4", "A5", "A6"],
        criteria=["C1", "C2", "C3", "C4", "C5"],
    )


# =============================================================================
# ERVD
# =============================================================================


def ervd_shyur2015multiple():
    """ERVD - Multiple criteria decision making based on relative value distances.

    Reference:
        Shyur, H. J., Yin, L., Shih, H. S., & Cheng, C. B. (2015).
        A multiple criteria decision making method based on relative
        value distances.
        Foundations of Computing and Decision Sciences, 40(4), 299-315.

    Domain: Generic MCDM problem
    Shape: 17 alternatives × 7 criteria
    """
    # Test: tests/agg/test_ervd.py:90
    return skcriteria.mkdm(
        matrix=[
            [80, 70, 87, 77, 76, 80, 75],
            [85, 65, 76, 80, 75, 65, 75],
            [78, 90, 72, 80, 85, 90, 85],
            [75, 84, 69, 85, 65, 65, 70],
            [84, 67, 60, 75, 85, 75, 80],
            [85, 78, 82, 81, 79, 80, 80],
            [77, 83, 74, 70, 71, 65, 70],
            [78, 82, 72, 80, 78, 70, 60],
            [85, 90, 80, 88, 90, 80, 85],
            [89, 75, 79, 67, 77, 70, 75],
            [65, 55, 68, 62, 70, 50, 60],
            [70, 64, 65, 65, 60, 60, 65],
            [95, 80, 70, 75, 70, 75, 75],
            [70, 80, 79, 80, 85, 80, 70],
            [60, 78, 87, 70, 66, 70, 65],
            [92, 85, 88, 90, 85, 90, 95],
            [86, 87, 80, 70, 72, 80, 85],
        ],
        objectives=[max, max, max, max, max, max, max],
        weights=[0.066, 0.196, 0.066, 0.130, 0.130, 0.216, 0.196],
    )


# =============================================================================
# RAM
# =============================================================================


def ram_sotoudeh2023():
    """RAM - Root Assessment Method for sustainability challenges.

    Reference:
        Sotoudeh-Anvari, A. (2023). Root Assessment Method (RAM):
        A novel multi-criteria decision making method and its applications
        in sustainability challenges.
        Journal of Cleaner Production, 423, 138695.
        Page 7, Tables 2 to 5.
        https://www.sciencedirect.com/science/article/abs/pii/S0959652623028536

    Domain: Sustainability assessment
    Shape: 10 alternatives × 7 criteria
    """
    # Test: tests/agg/test_ram.py:51
    return skcriteria.mkdm(
        matrix=[
            [0.068, 0.066, 0.150, 0.098, 0.156, 0.114, 0.098],
            [0.078, 0.076, 0.108, 0.136, 0.082, 0.171, 0.105],
            [0.157, 0.114, 0.128, 0.083, 0.108, 0.113, 0.131],
            [0.106, 0.139, 0.058, 0.074, 0.132, 0.084, 0.120],
            [0.103, 0.187, 0.125, 0.176, 0.074, 0.064, 0.057],
            [0.105, 0.083, 0.150, 0.051, 0.134, 0.094, 0.113],
            [0.137, 0.127, 0.056, 0.133, 0.122, 0.119, 0.114],
            [0.100, 0.082, 0.086, 0.060, 0.062, 0.109, 0.093],
            [0.053, 0.052, 0.043, 0.100, 0.050, 0.078, 0.063],
            [0.094, 0.074, 0.097, 0.087, 0.080, 0.054, 0.106],
        ],
        objectives=[max, min, min, max, max, max, max],
        weights=[0.132, 0.135, 0.138, 0.162, 0.09, 0.223, 0.12],
    )


# =============================================================================
# RIM
# =============================================================================


def rim_example():
    """RIM - Reference Ideal Method example.

    Reference:
        Original RIM paper example (reference details from test file)

    Domain: Generic MCDM problem
    Shape: 5 alternatives × 6 criteria
    """
    # Test: tests/agg/test_rim.py:33
    return skcriteria.mkdm(
        matrix=[
            [30, 0, 2, 3, 3, 2],  # A
            [40, 9, 1, 3, 2, 2],  # B
            [25, 0, 3, 1, 3, 2],  # C
            [27, 0, 5, 3, 3, 1],  # D
            [45, 15, 2, 2, 3, 4],  # E
        ],
        objectives=[max, max, max, max, max, max],
        weights=[0.2262, 0.2143, 0.1786, 0.1429, 0.1190, 0.1190],
        alternatives=["A", "B", "C", "D", "E"],
    )


# =============================================================================
# SIMUS
# =============================================================================


def simus_munier2024():
    """SIMUS - Multi-objective programming method.

    Reference:
        Munier, N., Carignano, C., & Alberto, C.
        UN MÉTODO DE PROGRAMACIÓN MULTIOBJETIVO.
        Revista de la Escuela de Perfeccionamiento en Investigación
        Operativa, 24(39).

    Domain: Project selection
    Shape: 3 alternatives × 4 criteria
    """
    # Test: tests/agg/test_simus.py:31
    return skcriteria.mkdm(
        matrix=[
            [250, 120, 20, 800],
            [130, 200, 40, 1000],
            [350, 340, 15, 600],
        ],
        objectives=[max, max, min, max],
        alternatives=["Proyecto 1", "Proyecto 2", "Proyecto 3"],
        criteria=["Criterio 1", "Criterio 2", "Criterio 3", "Criterio 4"],
    )


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================


def get_all_matrices():
    """Get a dictionary of all available decision matrices.

    Returns:
        dict: Dictionary mapping function names to decision matrix functions.
    """
    return {
        # TOPSIS
        "topsis_tzeng2011multiple": topsis_tzeng2011multiple,
        # VIKOR
        "vikor_tzeng2011": vikor_tzeng2011,
        "vikor_opricovic2004compromise": vikor_opricovic2004compromise,
        "vikor_opricovic2007extended": vikor_opricovic2007extended,
        # CODAS
        "codas_badi2017": codas_badi2017,
        "codas_badi2018": codas_badi2018,
        "codas_bakir2018": codas_bakir2018,
        "codas_baki2022": codas_baki2022,
        "codas_turskis2016": codas_turskis2016,
        # EDAS
        "edas_mathew2018": edas_mathew2018,
        "edas_ersoy2021": edas_ersoy2021,
        "edas_sharma2021": edas_sharma2021,
        "edas_karabasevic2018": edas_karabasevic2018,
        # MOORA
        "moora_kracka2010ranking": moora_kracka2010ranking,
        # MABAC
        "mabac_pamucar2014": mabac_pamucar2014,
        # CoCoSo
        "cocoso_yazdani2019": cocoso_yazdani2019,
        # SPOTIS
        "spotis_dezert2020_example_a": spotis_dezert2020_example_a,
        "spotis_dezert2020_example_b": spotis_dezert2020_example_b,
        # PROBID
        "probid_wang2021original": probid_wang2021original,
        # COPRAS
        "copras_uysal2022assistants": copras_uysal2022assistants,
        "copras_wieckowski2022criteriamethodscomparison": copras_wieckowski2022criteriamethodscomparison,
        # WASPAS
        "waspas_chakraborty2015applications": waspas_chakraborty2015applications,
        # ARAS
        "aras_balezentiene2012reducing": aras_balezentiene2012reducing,
        # OCRA
        "ocra_isik2016": ocra_isik2016,
        # ERVD
        "ervd_shyur2015multiple": ervd_shyur2015multiple,
        # RAM
        "ram_sotoudeh2023": ram_sotoudeh2023,
        # RIM
        "rim_example": rim_example,
        # SIMUS
        "simus_munier2024": simus_munier2024,
    }


def list_matrices_by_method():
    """Get matrices organized by MCDM method.

    Returns:
        dict: Dictionary mapping method names to lists of matrix function names.
    """
    return {
        "TOPSIS": [
            "topsis_tzeng2011multiple",
        ],
        "VIKOR": [
            "vikor_tzeng2011",
            "vikor_opricovic2004compromise",
            "vikor_opricovic2007extended",
        ],
        "CODAS": [
            "codas_badi2017",
            "codas_badi2018",
            "codas_bakir2018",
            "codas_baki2022",
            "codas_turskis2016",
        ],
        "EDAS": [
            "edas_mathew2018",
            "edas_ersoy2021",
            "edas_sharma2021",
            "edas_karabasevic2018",
        ],
        "MOORA": [
            "moora_kracka2010ranking",
        ],
        "MABAC": [
            "mabac_pamucar2014",
        ],
        "CoCoSo": [
            "cocoso_yazdani2019",
        ],
        "SPOTIS": [
            "spotis_dezert2020_example_a",
            "spotis_dezert2020_example_b",
        ],
        "PROBID": [
            "probid_wang2021original",
        ],
        "COPRAS": [
            "copras_uysal2022assistants",
            "copras_wieckowski2022criteriamethodscomparison",
        ],
        "WASPAS": [
            "waspas_chakraborty2015applications",
        ],
        "ARAS": [
            "aras_balezentiene2012reducing",
        ],
        "OCRA": [
            "ocra_isik2016",
        ],
        "ERVD": [
            "ervd_shyur2015multiple",
        ],
        "RAM": [
            "ram_sotoudeh2023",
        ],
        "RIM": [
            "rim_example",
        ],
        "SIMUS": [
            "simus_munier2024",
        ],
    }


def print_summary():
    """Print a summary of all available matrices."""
    matrices = get_all_matrices()
    by_method = list_matrices_by_method()

    print("=" * 80)
    print("ACADEMIC DECISION MATRICES COLLECTION")
    print("=" * 80)
    print(f"\nTotal matrices: {len(matrices)}")
    print(f"Total methods: {len(by_method)}")
    print("\nMatrices by method:")
    print("-" * 80)

    for method, matrix_names in sorted(by_method.items()):
        print(f"\n{method} ({len(matrix_names)} matrices):")
        for name in matrix_names:
            dm = matrices[name]()
            shape = dm.matrix.shape
            print(f"  - {name}: {shape[0]} alternatives × {shape[1]} criteria")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    # Print summary when executed directly
    print_summary()
