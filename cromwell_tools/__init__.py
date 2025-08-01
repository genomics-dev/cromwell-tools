"""
The importlib.metadata module gets the version from the installed package metadata.
This works when the package is properly installed.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("cromwell-tools-genomics")
except PackageNotFoundError:
    # package is not installed
    __version__ = "Unknown Ver."

# By using the below import statement when you call import cromwell_tools you get:
# cromwell_tools.api.status
# cromwell_tools.api.metadata
# cromwell_tools.api.run
# ...
from cromwell_tools.cromwell_api import CromwellAPI as api  # noqa
