import time
import os

os.environ['NEPTUNE_SAFETY_MODE'] = 'TRUE'

from neptune import Run


def my_custom_callback(run):
    print("Server synchronization is flaky. Stopping the connection in 60 seconds.")
    run.stop(seconds=60.0)


def main():
    os.environ['NEPTUNE_ENABLE_DEFAULT_ASYNC_LAG_CALLBACK'] = 'TRUE'
    os.environ['NEPTUNE_ENABLE_DEFAULT_ASYNC_NO_PROGRESS_CALLBACK'] = 'TRUE'

    with Run(
        async_lag_callback=my_custom_callback,
        async_lag_threshold=20.0,
        capture_stderr=False,
        capture_stdout=False,
        capture_hardware_metrics=False,
    ) as run:
        for _ in range(10):
            now = time.time()
            run["time"].append(now)
            time.sleep(10)


if __name__ == "__main__":
    main()
