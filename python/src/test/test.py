import cv2
import numpy as np

board = np.zeros((320,320))
block_width = 320 // 8
black_block = np.full((block_width, block_width), 255)

for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            row_begin = row * block_width
            row_end = row_begin + block_width
            col_begin = col * block_width
            col_end = col_begin + block_width

            board[row_begin:row_end, col_begin:col_end] = black_block

cv2.imshow("Test Board", board)
cv2.waitKey(0)
