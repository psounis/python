# interface.py
from abc import ABC, abstractmethod


class MyInterface(ABC):
    @abstractmethod
    def interface_method1(self):
        pass

    @abstractmethod
    def interface_method2(self):
        pass


class MyRealClass(MyInterface):
    ...
