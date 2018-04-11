from PIL import Image, ImageDraw, ImageFont


class ImageGen:
    def __init__(self, height, width, cols, rows):
        self.blank_image = Image.new('RGB', (height, width), (255, 255, 255))
        #self.makegrid(self.blank_image, cols, rows)
        #self.makecircle(self.blank_image)
        self.makecells(self.blank_image, cols, rows)
        self.blank_image.save("chart.jpg")

    def makegrid(self, img, cols, rows):
        # Add Row for Header
        rows += 1
        height = img.height
        width = img.width
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

    def makecells(self, img, cols, rows):
        # Add Row for Header
        rows += 1
        height = img.height
        width = img.width
        col_space = int(width / cols)
        row_space = int(height / rows)
        height = row_space * rows
        width = col_space * cols
        self.blank_image = img = img.resize((width, height), Image.ANTIALIAS)

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
            self.drawcell(cell, img)

        #print(cells)

    def drawcell(self, cell, img):
        t_cells = [tuple(l) for l in cell]
        draw = ImageDraw.Draw(img)
        draw.polygon(t_cells, fill=(255, 255, 255, 255), outline=(0, 0, 0))
        self.typeincell("B:{} L:{}".format(cell[3][0], cell[3][1]), self.blank_image, cell)

    def makecell(self, col_start, row_start, col_space, row_space):
        tl = [col_start, row_start]
        tr = [tl[0] + col_space, tl[1]]
        bl = [tl[0], tl[1] + row_space]
        br = [tl[0] + col_space, tl[1] + row_space]
        cell = [tl, tr, br, bl]
        return cell

    def typeincell(self, text, img, cell):
        fontsize = 15
        font = ImageFont.truetype("Roboto-Regular.ttf", fontsize)
        color = (0, 0, 0)

        draw = ImageDraw.Draw(img)
        W = cell[1][0] - cell[0][0]
        H = cell[3][1] - cell[0][1]
        w, h = draw.textsize(text)
        center_w = int((W - w) / 2)
        center_h = int((H - h) / 2)
        origin = (cell[0][0] + center_w, cell[0][1] + center_h)
        #print(origin)
        draw.text(origin, text, font=font, fill=(0, 0, 0))

    def makecircle(self, img):
        circle_dist_x = int(img.shape[1] / 2)
        circle_dist_y = int(img.shape[0] / 2)
        circle_center_x = int(img.shape[1] / 2)
        circle_center_y = int(img.shape[0] / 2)
        cv2.ellipse(img, (circle_center_x, circle_center_y), (circle_dist_x, circle_dist_y), 0, 0, 360, (0, 0, 0), 1)

    def drawcol(self, img, start):
        draw = ImageDraw.Draw(img)
        line = ((start, 0), (start, img.height))
        draw.line(line, fill=(0, 0, 0))

    def drawrow(self, img, start):
        draw = ImageDraw.Draw(img)
        line = ((0, start), (img.width, start))
        draw.line(line, fill=(0, 0, 0))