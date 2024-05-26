import time
from contextlib import contextmanager


@contextmanager
def timer():
    start_time = time.time()
    yield time
    end_time = time.time()
    timerr = end_time - start_time
    print(f"ketgan vaqt: {timerr:.1f}")


with timer():
    result = 1
    for i in range(1, 100000):
        result *= i
