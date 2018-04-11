import numpy as np
import cv2


class ImageGen:
    def __init__(self, height, width, cols, rows):
        self.blank_image = np.zeros((height, width, 3), np.uint8)
        self.blank_image[:] = (255, 255, 255)
        #self.makegrid(self.blank_image, cols, rows)
        #self.makecircle(self.blank_image)
        self.makecells(self.blank_image, cols, rows)
        cv2.imshow('image', self.blank_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def makegrid(self, img, cols, rows):
        # Add Row for Header
        rows += 1
        height = img.shape[0]
        width = img.shape[1]
        col_space = int(width / cols)
        row_space = int(height / rows)
        print("Height:{} Width:{} Col_Space:{} Row_Space:{}".format(height, width, col_space, row_space))

        cv2.rectangle(img, (0, 0), (height, width), (0, 0, 0), 1)

        col_start = 0
        row_start = 0

        for i in range(cols):
            self.drawcol(img, col_start)
            col_start += col_space

        for i in range(rows):
            self.drawrow(img, row_start)
            row_start += row_space

    def makecells(self, img, cols, rows):
        # Add Row for Header
        rows += 1
        height = img.shape[0]
        width = img.shape[1]
        col_space = int(width / cols)
        row_space = int(height / rows)
        height = row_space * rows
        width = col_space * cols
        self.blank_image = img = cv2.resize(img, (width, height))
        print("Height:{} Width:{} Col_Space:{} Row_Space:{}".format(height, width, col_space, row_space))

        col_start = 0
        row_start = 0

        cells = []

        for i in range(cols):
            if i == 0 or i == cols:
                col_start = 0
            else:
                col_start += col_space
            for j in range(rows):
                if j == 0 or j == rows:
                    row_start = 0
                else:
                    row_start += row_space
                print(col_start, row_start)
                cells.append(self.makecell(col_start, row_start, col_space, row_space))

        for cell in cells:
            pts = np.array(cell, np.int32)
            cv2.polylines(img, [pts], True, (0, 255, 0))
            self.typeincell("B:{} L:{}".format(cell[3][0], cell[3][1]), self.blank_image, cell)

        #print(cells)

    def makecell(self, col_start, row_start, col_space, row_space):
        tl = [col_start, row_start]
        tr = [tl[0] + col_space, tl[1]]
        bl = [tl[0], tl[1] + row_space]
        br = [tl[0] + col_space, tl[1] + row_space]
        cell = [tl, tr, br, bl]
        return cell

    def typeincell(self, text, img, cell):
        font = cv2.FONT_HERSHEY_DUPLEX
        fontscale = .35
        b = cell[3][1] - int(((cell[3][1] - cell[0][1]) / 2) - fontscale * 2)
        l = cell[3][0] + 5
        origin = (l, b)
        color = (0, 0, 0)
        cv2.putText(img, text, origin, font, fontscale, color)

    def makecircle(self, img):
        circle_dist_x = int(img.shape[1] / 2)
        circle_dist_y = int(img.shape[0] / 2)
        circle_center_x = int(img.shape[1] / 2)
        circle_center_y = int(img.shape[0] / 2)
        cv2.ellipse(img, (circle_center_x, circle_center_y), (circle_dist_x, circle_dist_y), 0, 0, 360, (0, 0, 0), 1)

    def drawcol(self, img, start):
        cv2.line(img, (start, 0), (start, img.shape[0]), (0, 0, 0), 1)

    def drawrow(self, img, start):
        cv2.line(img, (0, start), (img.shape[1], start), (0, 0, 0), 1)