from .base import BaseDisplayer
import cv2
import numpy as np

class picsPlayer(BaseDisplayer):
    def __init__(self):
        # !!! BGR FORMAT !!!
        self.COLOR_MAP = {
            "black":(0,0,0),
            "white":(255,255,255),
            "smokepink":(199,214,236),
            "pink":(104,103,255),
            "smokeblue":(248,237,185),
            "blue":(212,110,31)}

        # default setting now
        self.block_width = 120
        self.block_height = 120

        # The Cavas attr
        self.canvas_height = 360
        self.canvas_width = 600

        # The padding
        self.edge_padding = 50
        self.padding = 10

        # Grid Setting, 5 Canvas / Line
        self.big_board_cols = 5

        # Color setting
        self.bgcolorA = self.COLOR_MAP['smokeblue']
        self.bgcolorB = self.COLOR_MAP['smokepink']

        self.bkcolorA = self.COLOR_MAP['blue']
        self.bkcolorB = self.COLOR_MAP['pink']


    def init_canvas(self,width, height, color=(255,255,255)):
        canvas = np.ones((height, width, 3), dtype="uint8")
        canvas[:] = color
        return canvas

    def add_grid(self,canvas, row, col):
        self.canvas_width = canvas.shape[1]
        self.canvas_height = canvas.shape[0]
        canvas_width = canvas.shape[1]
        canvas_height = canvas.shape[0]


        self.block_width = canvas_width // col
        self.block_height = canvas_height // row
        block_width = canvas_width // col
        block_height = canvas_height // row

        # draw the framework
        cv2.rectangle(canvas,
                (0,0),
                (self.canvas_width - 1, self.canvas_height - 1),
                color=self.COLOR_MAP['black'])



        # draw lines 
        start_x = 0
        end_x = canvas_width

        start_y = 0
        end_y = start_y

        # The Row Part
        for i in range(row):
            start_y = i * block_height 
            end_y = start_y
            cv2.line(img=canvas, 
                    pt1=(start_x, start_y),
                    pt2=(end_x, end_y),
                    color=self.COLOR_MAP['black'])
        
        # The Col Part
        start_y = 0
        end_y = canvas_height

        start_x = 0
        end_x = start_x

        for i in range(col):
            start_x = i * block_width 
            end_x = start_x
            cv2.line(img=canvas,
                    pt1=(start_x, start_y),
                    pt2=(end_x, end_y),
                    color=self.COLOR_MAP['black'])

        return canvas

    def fillBlock(self, canvas, coords, color):
        for coord in coords:
            start_x = coord[1] * self.block_width
            start_y = coord[0] * self.block_height

            end_x = start_x + self.block_width
            end_y = start_y + self.block_height

            cv2.rectangle(canvas,
                    (start_x,start_y),
                    (end_x, end_y),
                    color,
                    -1)
        return canvas

    def generate(self,coords, bgcolor, bkcolor):
        canvas = self.init_canvas(self.canvas_width, self.canvas_height, bgcolor)
        canvas = self.add_grid(canvas, self.canvas_height // self.block_height, self.canvas_width // self.block_width)
        canvas = self.fillBlock(canvas, coords, bkcolor)
        return canvas

    def genMore(self,data):
        imgs = []
        padding,edge_padding = self.padding,self.edge_padding
        cols = self.big_board_cols

        # cnt how many canvas do we need
        cnt = len(data)
        rows = cnt // cols + 1
        if cnt % cols == 0:
            rows = rows - 1

        # prepare for the whole image
        big_board_w = cols * self.canvas_width + (cols - 1) * padding + edge_padding * 2
        big_board_h = rows * self.canvas_height + (rows - 1) * padding + edge_padding * 2
        big_board = self.init_canvas(big_board_w, big_board_h, self.COLOR_MAP['white'])


        # prepare our music canvases
        cnt = 0
        for coords in data:
            if cnt % 2 == 0:
                bgcolor = self.bgcolorA
                bkcolor = self.bkcolorA
            else:
                bgcolor = self.bgcolorB
                bkcolor = self.bkcolorB

            canvas = self.generate(coords, bgcolor, bkcolor)
            cnt += 1
            imgs.append(canvas)


        # set canvas in the whole image
        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                if index >= len(imgs):
                    break
                img = imgs[index]
                
                # draw the canvas on it
                y_start = edge_padding + (self.canvas_height + padding) * i
                y_end = y_start + self.canvas_height
                x_start = edge_padding + (self.canvas_width + padding) * j
                x_end = x_start + self.canvas_width

                big_board[y_start:y_end, x_start:x_end] = img


        return big_board

    def display(self, data):
        print(data)
        big_board = self.genMore(data)
        cv2.imshow('canvas', big_board)
        cv2.waitKey(0)
        cv2.imwrite("music.png", big_board)
        cv2.destroyAllWindows()
