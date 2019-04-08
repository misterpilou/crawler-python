import asyncio
import logging
import aiohttp

from playweb.fetcher.fetcherabc import FetcherABC

__all__ = ['DefaultFetcher']

i = 0

class DefaultFetcher(FetcherABC):
    def __init__(self, url, max_redirect, max_tries):
        self.url = url
        self.max_tries = max_tries
        self.max_redirect = max_redirect
        self.session = aiohttp.ClientSession(loop=asyncio.get_running_loop())
        self.command = None

    async def fetch(url):
        i = 1
        print(f'fetching {url}')
        try:
            async with aiohttp.request("GET", url) as resp:
                try:
                    res = await resp.read(), resp.url
                    return res
                except Exception:
                    return
        except Exception:
            return
    def __call__(self):
        self.fetch(self.url)
        return
