"""
Commonly used type variables.
"""

__all__ = ["S", "T"]

from typing import TypeVar

import numpy as np

S = TypeVar("S", bound=tuple[int, ...], covariant=True)
""" Any array shape (covariant). """

T = TypeVar("T", bound=np.number, covariant=True)
""" Any numpy [`number`][numpy.number] data type (covariant). """
