# import os
#
# os.environ["NEPTUNE_DISABLE_PARENT_DIR_DELETION"] = "TRUE"
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import neptune


def do_work():
    run = neptune.init_run()

    for i in range(100):
        run[f"field/field_{i}"] = i ** 2
        run.sync()

    run.stop()


with ThreadPoolExecutor(max_workers=10) as executor:
    fut = {executor.submit(do_work) for _ in range(10)}
    for future in as_completed(fut):
        print(future)
