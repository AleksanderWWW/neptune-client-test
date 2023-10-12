import time
import os

os.environ['NEPTUNE_SAFETY_MODE'] = 'TRUE'

from neptune import Run
from neptune.utils import stop_synchronization_callback



def my_custom_callback(run):
    print("Server synchronization is flaky. Stopping the connection in 60 seconds.")
    run.stop(seconds=60.0)


def main():
    os.environ['NEPTUNE_ENABLE_DEFAULT_ASYNC_LAG_CALLBACK'] = 'TRUE'
    os.environ['NEPTUNE_ENABLE_DEFAULT_ASYNC_NO_PROGRESS_CALLBACK'] = 'TRUE'

    with Run(
        async_lag_callback=my_custom_callback,
        async_lag_threshold=20.0,
    ) as run:
        for _ in range(10):
            now = time.time()
            print(now)
            run["time"].append(now)
            time.sleep(10)


def main():
    os.environ['NEPTUNE_ENABLE_DEFAULT_ASYNC_LAG_CALLBACK'] = 'TRUE'
    os.environ['NEPTUNE_ENABLE_DEFAULT_ASYNC_NO_PROGRESS_CALLBACK'] = 'TRUE'

    with Run(async_no_progress_callback=stop_synchronization_callback,
             async_no_progress_threshold=70,
             ) as run:

        print("doing work")
        run["abc"] = 56

        print("syncing")
        time.sleep(20)  # time to disconnect
        run.sync()


if __name__ == "__main__":
    main()
