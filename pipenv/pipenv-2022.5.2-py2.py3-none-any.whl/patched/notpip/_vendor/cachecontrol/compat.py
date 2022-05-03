# SPDX-FileCopyrightText: 2015 Eric Larson
#
# SPDX-License-Identifier: Apache-2.0

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


try:
    import cPickle as pickle
except ImportError:
    import pickle

# Handle the case where the requests module has been patched to not have
# urllib3 bundled as part of its source.
try:
    from pipenv.patched.notpip._vendor.requests.packages.urllib3.response import HTTPResponse
except ImportError:
    from pipenv.patched.notpip._vendor.urllib3.response import HTTPResponse

try:
    from pipenv.patched.notpip._vendor.requests.packages.urllib3.util import is_fp_closed
except ImportError:
    from pipenv.patched.notpip._vendor.urllib3.util import is_fp_closed

# Replicate some six behaviour
try:
    text_type = unicode
except NameError:
    text_type = str
