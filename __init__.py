"""
util_lib — tiny shared helpers used by other demo libraries.

Flat layout (repo root == package root):

    from util_lib import ensure_finite, identity
"""

from .checks import ensure_finite, identity

__all__ = ["ensure_finite", "identity"]
__version__ = "0.1.0"
