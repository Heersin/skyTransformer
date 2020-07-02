
from .base import BaseDecoder
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
keymap = {
   "=1":(0,0),
   "=2":(0,1),
   "=3":(0,2),
   "=4":(0,3),
   "=5":(0,4),
   "=6":(1,0),
   "=7":(1,1),
   "1":(1,2),
   "2":(1,3),
   "3":(1,4),
   "4":(2,0),
   "5":(2,1),
   "6":(2,2),
   "7":(2,3),
   "#1":(2,4),
   "0":(-1,-1)

}

class originDecoder(BaseDecoder):
    '''
    map your Keys to Coordinate/index in the pic
    Input : A list of keys, which is the output of encoder
            [["#1","2"], ["1","2", "3"]]
    Output: A list of Coordinate/index in the pic
        [[(0,0),(0,2),(3,1)...],[(0,1),(0,2)]]
    '''
    def map2coord(self, data):
        result = []

        for index in range(len(data)):
            tmp = []
            current_keys = data[index]
            for current_key in current_keys:
                if current_key in keymap:
                    tmp.append(keymap[current_key])
                else:
                    tmp.append((-1,-1))
                    print("[Warning] not support key found '{}',set it as stop".format(current_key))
            result.append(tmp)
        return result
