
from aiohttp import ClientSession
from ujson import dumps
from http import HTTPStatus

from logger import logger


class TestRequests(object):
    BASE_URL: str = 'https://jsonplaceholder.typicode.com'
    HEADERS = {
        'Content-Type': 'application/json',
        'User-Agent': 'PostmanRuntime/7.32.2',
    }

    def __init__(self):
        pass

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with ClientSession(
                    base_url=TestRequests.BASE_URL,
                    headers=TestRequests.HEADERS,
                    json_serialize=dumps,
            ) as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @classmethod
    @create_session
    async def _post(cls, url: str, payload: dict = None, session: ClientSession = None):
        response = await session.post(
            url=url,
            json=payload,
            verify_ssl=False,
        )
        if response.status == HTTPStatus.OK or response.status == HTTPStatus.CREATED:
            return await response.json()

    @classmethod
    @create_session
    async def _get(cls, url: str, query: dict = None, session: ClientSession = None):
        response = await session.get(
            url=url,
            params=query,
            verify_ssl=False,
        )
        try:
            return await response.json()
        except Exception as e:
            logger.error(f"Error: {e.__class__.__name__} - {str(e)}")

    async def testgetfunc(self):
        try:
            response = await self._get(
                url='/posts',
                query={},
            )
        except Exception as e:
            logger.error(f'Ошибка get запроса: {e}')

    async def testpostfunc(self):
        try:
            response = await self._post(
                url='/posts',
                payload={},
            )
        except Exception as e:
            logger.error(f'Ошибка post запроса: {e}')
