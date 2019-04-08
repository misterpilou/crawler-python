from abc import ABCMeta

class ParserABC(type, metaclass=ABCMeta):
    def __new__(cls, name, bases, namespace):
        return ABCMeta.__new__(cls, name, bases, namespace)

