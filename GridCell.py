from PIL import Image, ImageDraw, ImageFont
import sys
import os.path


class GridCell:
    def __init__(self, img, col_index, col_start, row_index, row_start, col_space, row_space):
        self.img = img
        self.col_index = col_index
        self.row_index = row_index

        tl = [col_start, row_start]
        tr = [tl[0] + col_space, tl[1]]
        bl = [tl[0], tl[1] + row_space]
        br = [tl[0] + col_space, tl[1] + row_space]
        self.cell = [tl, tr, br, bl]

    def drawcell(self, background=(255, 255, 255, 255), linecolor=(0, 0, 0)):
        t_cells = [tuple(l) for l in self.cell]
        draw = ImageDraw.Draw(self.img)
        draw.polygon(t_cells, fill=background, outline=linecolor)

    def typeincell(self, text, fontcolor=(0, 0, 0)):
        draw = ImageDraw.Draw(self.img)
        fontsize = 1
        if hasattr(sys, "_MEIPASS"):
            font_str = os.path.join(sys._MEIPASS, 'res/Roboto-Regular.ttf')
        else:
            font_str = 'res/Roboto-Regular.ttf'
        font = ImageFont.truetype(font_str, fontsize)

        # Cell Size
        W = self.cell[1][0] - self.cell[0][0]
        H = self.cell[3][1] - self.cell[0][1]

        # Sizing Text to Fit Cell
        # portion of image width you want text width to be
        h_img_fraction = 0.5
        w_img_fraction = 0.85

        while font.getsize(text)[1] < h_img_fraction * H:
            # iterate until the text size is just larger than the criteria
            fontsize += 1
            font = ImageFont.truetype(font_str, fontsize)
        fontsize -= 1
        font = ImageFont.truetype(font_str, fontsize)

        while font.getsize(text)[0] > W * w_img_fraction:
            # iterate until the text size is just larger than the criteria
            fontsize -= 1
            font = ImageFont.truetype(font_str, fontsize)
            #print("Decreasing Width:", font.getsize(text))
        fontsize -= 1
        font = ImageFont.truetype(font_str, fontsize)


        # Centering Text
        w, h = font.getsize(text)
        center_w = int((W - w) / 2)
        center_h = int((H - h) / 2) + 1
        origin = (self.cell[0][0] + center_w, self.cell[0][1] + center_h)
        # print(origin)

        draw.text(origin, text, font=font, fill=fontcolor)

    def getimage(self):
        return self.img