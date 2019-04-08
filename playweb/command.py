import pkgutil
import sys
import re
import logging

from playweb.fetcher import *
from playweb.parser import *
from playweb.fetcher.fetcherabc import FetcherABC
from playweb.parser.parserabc import ParserABC


class Command:
    def __init__(self, urls, config_file = None, max_redirect: int = 5, max_tries: int = 5,
                 regex_filter=None, verbose: bool = True, polite: bool = True, parser=None,
                 fetcher=None, downloader = None, scorer = None, store = None):
        self.config = None
        self.urls = {urls} or self.config.urls
        self.max_redirect= max_redirect or self.config.max_redirect
        self.max_tries = max_tries or self.config.max_tries
        #self.regex_filter = regex_filter or self.config.regex_filter
        #add log levels
        #self.verbose = verbose or self.config.verbose
        #Implement parser, fetcher ... by decorator, filter and abc
        self.fetcher = fetcher
        self.parser = parser

    def parse_config(self, config_file):
        return

    @property
    def fetcher(self):
        print('accessor')
        print(getattr(self, '_fetcher'))
        return self._fetcher

    @fetcher.setter
    def fetcher(self, name: str):
        print('debug')
        list_fetcher = [str(f.__name__) for f in
                type.__subclasses__(FetcherABC)]
        for l in list_fetcher:
            print(l)
        if name in list_fetcher:
            self._fetcher = getattr(sys.modules[__name__], name)
        else:
            raise AttributeError
    @property
    def parser(self):
        print('accessor')
        print(getattr(self, '_parser'))
        return self._parser

    @parser.setter
    def parser(self, name: str):
        print('debug')
        list_parser = [str(f.__name__) for f in
                type.__subclasses__(ParserABC)]
        for l in list_parser:
            print(l)
        if name in list_parser:
            self._parser = getattr(sys.modules[__name__], name)
        else:
            raise AttributeError

