from abc import ABCMeta, abstractmethod

class BaseEncoder(metaclass=ABCMeta):
    '''
    readfile : about how to read your file
            it depends on your file format
        Input: filename
        Output: the data for processing in your process method
        Commend: keyword -- 'with' is recommended
    '''
    @abstractmethod
    def readfile(self, filename):
        pass


    '''
    process : about how to handle your data
            and process it to the proper format
        Input: data from readfile return
        Output: a list of Keys, for example:
        ['5','5','4','4','#1', '#1', '=5'...]
        Commend: Chars in UPCASE
    '''
    @abstractmethod
    def process(self, data):
        pass


