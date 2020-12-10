import logging
from datetime import timedelta
from functools import wraps
from time import time


def tempo_total(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time()
        try:
            return func(*args, **kwargs)
        finally:
            tempo_total = int(time() - start)
            tempo_total = str(timedelta(seconds=tempo_total))
            logging.info(f"Tempo de execução total da função {func.__name__}: {tempo_total}")

    return _time_it
