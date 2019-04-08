from playweb.parser.parserabc import ParserABC
import urllib.parse
from lxml.html import fromstring

__all__ = ['DefaultParser']

class DefaultParser(ParserABC):
    def __init__(self, fetch):
        Parser.__init__(fetch=fetch)
        self.command = None

    async def parse(response):
        try:
            html_body = fromstring(response[0])
            raw_links = html_body.xpath('//a/@href')
            links = [urllib.parse.urljoin(str(response[1]), link) for link in
                    raw_links if link is not None]
            return links
        except Exception:
            pass
