import numpy as np
import cv2


class ImageGen:
    def __init__(self, height, width, cols, rows):
        self.blank_image = np.zeros((height, width, 3), np.uint8)
        self.blank_image[:] = (255, 255, 255)
        self.makegrid(self.blank_image, cols, rows)
        cv2.imshow('image', self.blank_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def makegrid(self, img, cols, rows):
        # Add Row for Header
        rows += 1
        height = self.blank_image.shape[0]
        width = self.blank_image.shape[1]
        col_space = int(width / cols)
        row_space = int(height / rows)
        print("Height:{} Width:{} Col_Space:{} Row_Space:{}".format(height, width, col_space, row_space))

        col_start = 0
        row_start = 0

        for i in range(cols):
            self.drawcol(img, col_start)
            col_start += col_space

        for i in range(rows):
            self.drawrow(img, row_start)
            row_start += row_space

    def drawcol(self, img, start):
        cv2.line(img, (start, 0), (start, img.shape[0]), (0, 0, 0))

    def drawrow(self, img, start):
        cv2.line(img, (0, start), (img.shape[1], start), (0, 0, 0))