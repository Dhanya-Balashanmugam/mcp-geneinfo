"""
mcpatlas - Get tissue and cancer specific protein expression info from Human Protein Atlas
"""

__version__ = "0.1.0"
__author__ = "dhanya"
__email__ = "dhanyabalashanmugam24@gmail.com"

from .bridge import Bridge, Config

__all__ = ["Bridge", "Config"] 