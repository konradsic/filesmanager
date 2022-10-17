"""
filesmanager - Python file management and downloading
=======================
A module that allows users to easily create, manipulate and download files from the Internet

:copyright: 2022-present konradsic 
:license: Licensed under the MIT License see LICENSE file https://github.com/konradsic/pyfiles/blob/master/LICENSE
"""

__title__ = "filesmanager"
__author__ = "konradsic"
__version__ = "0.0.1"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2022-present konradsic"

# package imports
from .abc import *
from .managers import *
from .utils import *
from .download import *

# other initialization processes
import colorama
colorama.init(autoreset=True)