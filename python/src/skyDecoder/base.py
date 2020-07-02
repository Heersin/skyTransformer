from abc import ABCMeta, abstractmethod

'''
Handle music -> sky music mode

my default key mapping as follows
-------------------------------
| =1  | =2  | =3  | =4  | =5  |
--------------------------------
| =6  | =7  |  1  |  2  |  3  |
-------------------------------
|  4  |  5  |  6  |  7  | #1  |
-------------------------------

you can decide the key map in your decoder, such as:

'''
class BaseDecoder(metaclass=ABCMeta):
    '''
    map your Keys to Coordinate/index in the pic
    Input : A list of keys, which is the output of encoder
    Output: A list of Coordinate/index in the pic
        [(0,0),(0,2),(3,1)...]
    '''
    @abstractmethod
    def map2coord(self, data):
        pass
