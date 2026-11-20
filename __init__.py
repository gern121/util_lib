"""
util_lib — tiny shared helpers used by other demo libraries.

Flat layout (repo root == package root):

    from util_lib import ensure_finite, identity, clamp_unit
"""

from .checks import ensure_finite, identity, clamp_unit

__all__ = ["ensure_finite", "identity", "clamp_unit"]
__version__ = "0.2.0"
