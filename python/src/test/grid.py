import cv2
import numpy as np

# !!! BGR FORMAT !!!
# normal format is RGB, should convert to BGR
COLOR_MAP = {
        "black":(0,0,0),
        "white":(255,255,255),
        "smokepink":(199,214,236),
        "pink":(104,103,255),
        "smokeblue":(248,237,185),
        "blue":(212,110,31)}

global block_width
global block_height
global canvas_height
global canvas_width

block_width = 120
block_height = 120
canvas_height = 360
canvas_width = 600

def init_canvas(width, height, color=(255,255,255)):
    canvas = np.ones((height, width, 3), dtype="uint8")
    canvas[:] = color
    return canvas

def add_grid(canvas, row, col):

    canvas_width = canvas.shape[1]
    canvas_height = canvas.shape[0]
    block_width = canvas_width // col
    block_height = canvas_height // row

    # draw the wholeline
    cv2.rectangle(canvas,
            (0,0),
            (canvas_width - 1,canvas_height - 1),
            color=COLOR_MAP['black'])

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
                color=COLOR_MAP['black'])
    
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
                color=COLOR_MAP['black'])

    return canvas

def fillBlock(canvas, coords, color=COLOR_MAP['black']):
    for coord in coords:
        start_x = coord[1] * block_width
        start_y = coord[0] * block_height

        end_x = start_x + block_width
        end_y = start_y + block_height

        print(start_x, start_y, end_x, end_y)

        cv2.rectangle(canvas,
                (start_x,start_y),
                (end_x, end_y),
                color,
                -1)
    return canvas

def generate(coords, bgcolor=COLOR_MAP['white'], bkcolor=COLOR_MAP['black']):
    canvas = init_canvas(600, 360, bgcolor)
    canvas = add_grid(canvas, 3, 5)
    canvas = fillBlock(canvas, coords, bkcolor)
    return canvas

def genMore(data):
    imgs = []
    padding = 10
    edge_padding = 50
    # the cnt of coords
    cnt = len(data)
    # 每行5音
    cols = 5
    rows = cnt // cols + 1
    if cnt % cols == 0:
        rows = rows - 1
    big_board_width = cols * canvas_width + (cols - 1) * padding + edge_padding * 2
    big_board_height = rows * canvas_height + (rows - 1) * padding + edge_padding * 2
    big_board = init_canvas(big_board_width, big_board_height)

    # prepare for canvas
    cnt = 0

    for coords in data:
        if cnt % 2 == 0:
            bgcolor = COLOR_MAP["smokeblue"]
            bkcolor = COLOR_MAP["blue"]
        else:
            bgcolor = COLOR_MAP["smokepink"]
            bkcolor = COLOR_MAP["pink"]
        canvas = generate(coords, bgcolor, bkcolor)
        cnt += 1
        imgs.append(canvas)


    # set in a single pic
    for i in range(rows):
        for j in range(cols):
            index = i * cols + j
            if index >= len(imgs):
                break
            img = imgs[i * cols + j]
            y_start = edge_padding + (canvas_height + padding) * i
            y_end = y_start + canvas_height
            
            x_start = edge_padding + (canvas_width + padding) * j
            x_end = x_start + canvas_width
            big_board[ y_start:y_end, x_start:x_end ] = img

    return big_board


data = [[(0,3)],[(0,1)],[(1,2)], [(2,1)], [(1,3)],
        [(1,1)], [(2,2)], [(4,1)], [(3,3)]]
canvas = genMore(data)
cv2.imshow('canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
