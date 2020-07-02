from abc import ABCMeta, abstractmethod

class BaseDisplayer(metaclass=ABCMeta):
    @abstractmethod
    def display(self, tuple_list):
        pass
