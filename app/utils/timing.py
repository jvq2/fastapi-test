

import asyncio
import time
from contextlib import asynccontextmanager


@asynccontextmanager
async def normalize_timing(min_seconds: float):
    """Wrap code with this context to ensure that the code takes at least the
    provided `min_seconds` to execute. This is primarily helpful to prevent
    timing based login scraping.

    :param float min_seconds: The minimum number of seconds this code is allowed
        to take to execute.
    """
    start = time.perf_counter()

    try:
        yield

    finally:
        end = time.perf_counter()
        elapsed = end - start

        # Sleep to ensure short code execution time is hidden
        if elapsed < min_seconds:
            await asyncio.sleep(min_seconds - elapsed)
