import time

from neptune import Run

import os


def my_custom_callback(run):
    print("Server synchronization is flaky. Stopping the connection in 60 seconds.")
    run.stop(seconds=60.0)


def main():
    os.environ['NEPTUNE_ENABLE_DEFAULT_ASYNC_LAG_CALLBACK'] = 'TRUE'
    os.environ['NEPTUNE_ENABLE_DEFAULT_ASYNC_NO_PROGRESS_CALLBACK'] = 'TRUE'

    now = time.time()
    stop_time = now + 5 * 60  # 5 mins

    with Run(
        async_lag_callback=my_custom_callback,
        async_lag_threshold=20.0,
    ) as run:
        while now < stop_time:
            print(f"{now = }")
            run["time"].append(now)
            time.sleep(10)
            now = time.time()


if __name__ == "__main__":
    main()
