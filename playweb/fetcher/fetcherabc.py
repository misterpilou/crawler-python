from playweb.meta.register import Register
from abc import ABCMeta

class FetcherABC(type, metaclass=ABCMeta):
    def __new__(cls, name, bases, namespace):
        return ABCMeta.__new__(cls, name, bases, namespace)

