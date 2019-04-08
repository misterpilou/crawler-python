import asyncio
import time

import fire
from aiomultiprocess import Pool, Worker
from aiohttp import request, ClientSession
import aiofiles

from playweb.command import Command

async def work():
    i = 0
    t1 = time.time()
    seen_urls = set()
    while True:
        async with Pool() as pool:
            if i == 0:
                urls = cmd.urls
            #p = Worker(fetch("www.jeuxvideo.com"), {})
            #w = await p
            #print(w)
            fetches = await pool.map(cmd.fetcher.fetch, urls)
            parses = await pool.map(cmd.parser.parse, fetches)
            print(parses)
            seen_urls.update(url for url in urls)
            t2 = time.time()
            urls = ({parse for parse_item in parses
                if parse_item
                for parse in parse_item
                if parse
                and parse not in seen_urls})
            i+=1
            t_i = t2-t1
            n_fetch = len(seen_urls)
            async with aiofiles.open('stats.txt', mode='wb') as f:
                await f.write(bytes(f'{n_fetch} at time {t_i}', 'utf-8'))

if __name__ == '__main__':
    cmd = fire.Fire(Command)
    print(type(cmd))
    print('DEBUG')
    if(cmd.fetcher is None):
        print('No fetcher')
    else:
        print('value of fetcher: %s', cmd.fetcher)
        print('type of fetcher: %s', type(cmd.fetcher))
    asyncio.run(work())
