import asyncio
import time


class Debouncer:
    def __init__(self, rate):
        self.rate = rate  # max number of calls per second
        self.semaphore = asyncio.Semaphore(rate)
        self.start_time = time.time()

    async def debounce(self):
        elapsed = time.time() - self.start_time

        if elapsed >= 1:
            self.start_time = time.time()

        await self.semaphore.acquire()
        try:
            if elapsed < 1:
                remaining_time = 1 - elapsed
                await asyncio.sleep(remaining_time)
        finally:
            self.semaphore.release()
