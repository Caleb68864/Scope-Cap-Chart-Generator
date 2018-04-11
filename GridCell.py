from PIL import Image, ImageDraw, ImageFont


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
        font = ImageFont.truetype("Roboto-Regular.ttf", fontsize)

        # Cell Size
        W = self.cell[1][0] - self.cell[0][0]
        H = self.cell[3][1] - self.cell[0][1]

        # Sizing Text to Fit Cell
        # portion of image width you want text width to be
        img_fraction = 0.5
        while font.getsize(text)[1] < img_fraction * H:
            # iterate until the text size is just larger than the criteria
            fontsize += 1
            font = ImageFont.truetype("Roboto-Regular.ttf", fontsize)
        fontsize -= 1
        font = ImageFont.truetype("Roboto-Regular.ttf", fontsize)

        # Centering Text
        w, h = font.getsize(text)
        center_w = int((W - w) / 2)
        center_h = int((H - h) / 2) + 1
        origin = (self.cell[0][0] + center_w, self.cell[0][1] + center_h)
        # print(origin)

        draw.text(origin, text, font=font, fill=fontcolor)

    def getimage(self):
        return self.img