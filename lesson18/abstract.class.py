# abstract.class.py
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    def __init__(self, attr):
        self.attr = attr

    @abstractmethod
    def my_abstract_method(self):
        pass


ob = MyAbstractClass(1)
