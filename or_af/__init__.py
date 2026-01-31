"""
OR-AF: Operation Research Agentic Framework

An agentic framework for Operations Research application development.
"""

__version__ = "0.1.0"
__author__ = "Aakash Roy"
__email__ = "iaakashroy@gmail.com"

from or_af.agent import Agent
from or_af.framework import ORFramework

__all__ = [
    "Agent",
    "ORFramework",
    "__version__",
]
