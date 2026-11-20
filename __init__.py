"""
util_lib — tiny shared helpers used by other demo libraries.

Flat layout (repo root == package root):

    from util_lib import ensure_finite, identity, clamp_unit, is_close
"""

from .checks import ensure_finite, identity, clamp_unit, is_close

__all__ = ["ensure_finite", "identity", "clamp_unit", "is_close"]
__version__ = "0.3.0"
