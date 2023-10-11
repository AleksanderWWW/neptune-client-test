import time

import neptune


with neptune.init_run(
    enable_remote_signals=False,
) as run:
    time.sleep(100)
    # tried to remotely abort the run in the UI but didn't work - so I guess it's good :)
