# -*- coding: utf-8 -*-
"""
    Settings
    ~~~~~~~~~~~~~~

    A divided settings module.

    :copyright: (c) 2012 by arruda.
"""

import sys
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT =os.path.dirname(PROJECT_ROOT)
sys.path.append(SITE_ROOT)

SECRET_KEY = 'vg$zseqb69gmic76sa*a+5i#@ufrcd&nw==x$@89+(195zoo7i'

ON_PRODUCTION = os.environ.has_key('ON_PRODUCTION')

from config import *
from installed_apps import *
from logging import *
from test_settings import *

NO_DEPRECATION_WARNINGS=False
if not ON_PRODUCTION:
    NO_DEPRECATION_WARNINGS=True
    from env_dev import *
else:
    from env_prod import *

if NO_DEPRECATION_WARNINGS:
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)


