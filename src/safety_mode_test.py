import os

os.environ['NEPTUNE_SAFETY_MODE'] = 'TRUE'

import neptune

from neptune import __version__


print(__version__)

with neptune.init_run() as run:
    run["root0"] = "adas"
    run["root0/level1"] = "adas"

    print("Got here")  # this should be executed
