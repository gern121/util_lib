"""
Small validation / identity helpers for the submodule nesting demo.
"""

from __future__ import annotations

import math


def ensure_finite(value: float) -> float:
    """
    Return `value` unchanged when it is a finite number.

    Raises:
        ValueError: if value is NaN or +/- infinity.

    Example:
        ensure_finite(3.5)  -> 3.5
    """
    if not math.isfinite(value):
        raise ValueError(f"Expected a finite number, got {value!r}")
    return value


def identity(value: float) -> float:
    """
    Return `value` unchanged (useful as a no-op callback in demos).

    Example:
        identity(7)  -> 7
    """
    return value


def clamp_unit(value: float) -> float:
    """
    Clamp `value` into the inclusive unit interval [0, 1].

    Example:
        clamp_unit(1.5)  -> 1.0
        clamp_unit(-0.2) -> 0.0
    """
    value = ensure_finite(value)
    if value < 0:
        return 0.0
    if value > 1:
        return 1.0
    return value
