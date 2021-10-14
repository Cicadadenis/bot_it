import asyncio
from contextlib import closing

import aiohttp
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from contextlib import closing

import aiohttp

bot = Bot(token='1858148404:AAG0aLGBfrpmJPbr44wmtK_kxAyKEhhc16I')
dp = Dispatcher(bot, storage=MemoryStorage())
CHUNK_SIZE = 4 * 1024  # 4 KB


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


@coroutine
def chunk_printer(url: str):
    while True:
        chunk = yield
        print('got chunk: {}: {} bytes'.format(url, len(chunk)))

@dp.message_handler()
async def download_file(session: aiohttp.ClientSession, url: str, sink):
    async with session.get(url) as response:
        assert response.status == 200
        while True:
            chunk = await response.content.read(CHUNK_SIZE)
            if not chunk:
                break
            sink.send(chunk)
    return url


@asyncio.coroutine
def download_multiple(session: aiohttp.ClientSession):
    urls = (
        'http://cnn.com',
        'http://nytimes.com',
        'http://google.com',
        'http://leagueoflegends.com',
        'http://python.org',
    )
    download_futures = [download_file(session, url, sink=chunk_printer(url)) for url in urls]
    print('Results')
    for download_future in asyncio.as_completed(download_futures):
        result = yield from download_future
        print('finished:', result)
    return urls


def main():
    with closing(asyncio.get_event_loop()) as loop:
        with aiohttp.ClientSession() as session:
            result = loop.run_until_complete(download_multiple(session))
            print('finished:', result)


main()

if __name__ == "__main__":
    executor.start_polling(dp)