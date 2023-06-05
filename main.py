import asyncio

from api import TestRequests
from logger import logger


async def foo():
    req = TestRequests()
    while True:
        await req.testgetfunc()
        logger.debug('Отправляем запрос')


async def main():
    try:
        tasks = [asyncio.create_task(foo()) for _ in range(10)]
        for task in tasks:
            await task
    except Exception as e:
        logger.error(f'Ошибка функции main(): {e}')


if __name__ == '__main__':
    asyncio.run(main())
