"""
rest-builder - Build REST APIs quickly

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import RestBuilder, build, process, main

__all__ = ["RestBuilder", "build", "process", "main"]
