"""Contains formulas and functions to analyze guitar tuning measurements."""

import math
from typing import Callable

from i18n import Translator
from models import (
    GuitarAnalysisResult,
    GuitarConfig,
    GuitarStringMeasurement,
    GuitarStringResult,
)

# Constant conversion factor to estimate truss rod turns per cent difference
ADJUSTMENT_FACTOR = 0.1


def ideal_frequency(f_open: float, fret: int) -> float:
    """Calculate the ideal frequency of a note at a given fret.

    Args:
        f_open: Open string frequency.
        fret: Fret number.

    Returns:
        The ideal frequency for the given fret.
    """
    return f_open * (2 ** (fret / 12.0))


def cents_difference(f_meas: float, f_ideal: float) -> float:
    """Calculate the difference in cents between the measured and ideal frequencies.

    Args:
        f_meas: Measured frequency.
        f_ideal: Ideal frequency.

    Returns:
        Difference in cents.
    """
    return 1200 * math.log2(f_meas / f_ideal)


def analyze_string(
    gstring: GuitarStringMeasurement,
    threshold: float = 3.0,
    threshold_action: float = 2.0,
    translator: Translator = lambda key, **kwargs: key,
) -> GuitarStringResult:
    """Analyze a single guitar string's measurements and generate tuning recommendations.

    Args:
        gstring: Guitar string measurement model.
        threshold: Threshold for significant deviation.
        threshold_action: Threshold for bridge (action) deviation.
        translator: Function to retrieve localized messages.

    Returns:
        A GuitarStringResult containing deviations and recommendations.
    """
    frets = [1, 3, 5, 7, 9, 12]
    deviations = {}

    # Calculate cents deviation for each fret
    for fret in frets:
        ideal = ideal_frequency(gstring.open_freq, fret)
        meas = gstring.measurements[fret]
        deviations[fret] = cents_difference(meas, ideal)

    # Calculate average deviations for grouped frets
    avg_low = (deviations[1] + deviations[3]) / 2
    avg_mid = (deviations[5] + deviations[7]) / 2
    avg_high = (deviations[9] + deviations[12]) / 2

    # Recommendation for saddle adjustment based on high frets
    if avg_high > 0:
        if avg_high >= threshold:
            rec_saddle = translator("saddle_sharp_significant")
        else:
            rec_saddle = translator("saddle_sharp_slight")
    elif avg_high < 0:
        if abs(avg_high) >= threshold:
            rec_saddle = translator("saddle_flat_significant")
        else:
            rec_saddle = translator("saddle_flat_slight")
    else:
        rec_saddle = translator("saddle_perfect")

    # Recommendation for nut adjustment based on the difference between low and high frets
    diff_low_high = avg_low - avg_high
    if diff_low_high > 0:
        if diff_low_high >= threshold:
            rec_nut = translator("nut_sharp_significant")
        else:
            rec_nut = translator("nut_sharp_slight")
    elif diff_low_high < 0:
        if abs(diff_low_high) >= threshold:
            rec_nut = translator("nut_flat_significant")
        else:
            rec_nut = translator("nut_flat_slight")
    else:
        rec_nut = translator("nut_perfect")

    # Recommendation for bridge (action) adjustment based on the difference between high and mid frets
    action_diff = avg_high - avg_mid
    if action_diff > threshold_action:
        rec_bridge = translator("bridge_high")
    elif action_diff < -threshold_action:
        rec_bridge = translator("bridge_low")
    else:
        rec_bridge = translator("bridge_normal")

    return GuitarStringResult(
        name=gstring.name,
        open_freq=gstring.open_freq,
        deviations=deviations,
        avg_low=avg_low,
        avg_mid=avg_mid,
        avg_high=avg_high,
        recommendation_saddle=rec_saddle,
        recommendation_nut=rec_nut,
        recommendation_bridge=rec_bridge,
        truss_diff=avg_mid - avg_high,
    )


def analyze_guitar(
    config: GuitarConfig,
    threshold: float = 3.0,
    threshold_action: float = 2.0,
    translator: Translator = lambda key, **kwargs: key,
) -> GuitarAnalysisResult:
    """Analyze the entire guitar configuration and produce overall tuning recommendations.

    Args:
        config: Guitar configuration model.
        threshold: Threshold for significant deviation.
        threshold_action: Threshold for bridge (action) deviation.
        translator: Function to retrieve localized messages.

    Returns:
        A GuitarAnalysisResult containing per-string and overall results.
    """
    results = []
    truss_diffs = []

    # Process each string in the guitar configuration
    for gstring in config.strings:
        result = analyze_string(gstring, threshold, threshold_action, translator)
        results.append(result)
        truss_diffs.append(result.truss_diff)

    overall_truss = sum(truss_diffs) / len(truss_diffs)

    # Determine overall truss rod adjustment recommendation
    if overall_truss > 0:
        direction = translator("clockwise")
        turns = overall_truss * ADJUSTMENT_FACTOR
        if overall_truss >= threshold:
            overall_rec = translator("mid_sharp_significant", direction=direction)
        else:
            overall_rec = translator("mid_sharp_slight")
        degrees = turns * 360
        tip = translator("truss_tip", direction=direction, turns=f"{turns:.2f}", degrees=f"{degrees:.0f}")
        overall_rec += tip
    elif overall_truss < 0:
        direction = translator("counterclockwise")
        turns = abs(overall_truss) * ADJUSTMENT_FACTOR
        if abs(overall_truss) >= threshold:
            overall_rec = translator("mid_flat_significant", direction=direction)
        else:
            overall_rec = translator("mid_flat_slight")
        degrees = turns * 360
        tip = translator("truss_tip", direction=direction, turns=f"{turns:.2f}", degrees=f"{degrees:.0f}")
        overall_rec += tip
    else:
        overall_rec = translator("no_adjustment")

    return GuitarAnalysisResult(
        strings=results,
        overall_truss=overall_truss,
        overall_recommendation=overall_rec,
    )
