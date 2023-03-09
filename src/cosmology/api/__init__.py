"""The Cosmology API standard."""

from cosmology.api._components import (
    HasBaryonComponent,
    HasDarkEnergyComponent,
    HasDarkMatterComponent,
    HasGlobalCurvatureComponent,
    HasMatterComponent,
    HasNeutrinoComponent,
    HasPhotonComponent,
)
from cosmology.api._constants import CosmologyConstantsAPINamespace
from cosmology.api._core import CosmologyAPI
from cosmology.api._distances import HasDistanceMeasures
from cosmology.api._extras import HasHubbleParameter, HasTcmb
from cosmology.api._namespace import CosmologyAPINamespace
from cosmology.api._standard import StandardCosmologyAPI
from cosmology.api.compat import (
    CosmologyWrapperAPI,
    StandardCosmologyWrapperAPI,
)

__all__ = [
    "CosmologyAPI",
    "HasDistanceMeasures",
    "StandardCosmologyAPI",
    # components
    "HasGlobalCurvatureComponent",
    "HasMatterComponent",
    "HasBaryonComponent",
    "HasNeutrinoComponent",
    "HasDarkEnergyComponent",
    "HasDarkMatterComponent",
    "HasPhotonComponent",
    # parametrizations
    "HasHubbleParameter",
    "HasTcmb",
    # wrappers
    "CosmologyWrapperAPI",
    "StandardCosmologyWrapperAPI",
    # Namespaces
    "CosmologyAPINamespace",
    "CosmologyConstantsAPINamespace",
]
