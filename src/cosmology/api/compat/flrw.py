"""The Cosmology API standard."""

from __future__ import annotations

# STDLIB
from typing import Protocol

# LOCAL
from cosmology.api.compat.core import CosmologyWrapperAPI
from cosmology.api.flrw import FLRWCosmologyAPI

__all__: list[str] = []


class FLRWCosmologyWrapperAPI(CosmologyWrapperAPI, FLRWCosmologyAPI, Protocol):
    """The Cosmology API standard for FLRW compatability wrappers.

    This is a protocol class that defines the standard API for FLRW classes. It
    is not intended to be used directly, and should not be instantiated.
    Instead, it should be used as a Protocol or ABC for libraries that wish to
    define a wrapper for the standard API.

    Parameters
    ----------
    cosmo: object
        The object to wrap.

    See Also
    --------
    cosmology.api.compat.core.StandardFLRWCosmologyWrapperAPI
        The FLRW Cosmology wrapper API, with the standard set of components:
        matter, radiation, dark energy, dark matter, neutrinos.
    """
