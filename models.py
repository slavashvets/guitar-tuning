"""Contains Pydantic models for guitar tuning data and analysis results."""

from typing import Dict, List

from pydantic import BaseModel


class GuitarStringMeasurement(BaseModel):
    """Model for a single guitar string measurement."""
    name: str
    open_freq: float
    measurements: Dict[int, float]


class GuitarConfig(BaseModel):
    """Model for guitar configuration, including all strings."""
    strings: List[GuitarStringMeasurement]


class GuitarStringResult(BaseModel):
    """Result model for a single string analysis."""
    name: str
    open_freq: float
    deviations: Dict[int, float]  # deviations per fret (in cents)
    avg_low: float  # average for frets 1 and 3
    avg_mid: float  # average for frets 5 and 7
    avg_high: float  # average for frets 9 and 12
    recommendation_saddle: str  # recommendation for saddle adjustment
    recommendation_nut: str  # recommendation for nut adjustment
    recommendation_bridge: str  # recommendation for bridge (action) adjustment
    truss_diff: float  # difference (mid - high), for truss rod adjustment


class GuitarAnalysisResult(BaseModel):
    """Result model for overall guitar analysis."""
    strings: List[GuitarStringResult]
    overall_truss: float  # average truss difference over all strings
    overall_recommendation: str  # overall recommendation for the truss rod
