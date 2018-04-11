from PIL import Image, ImageDraw, ImageFont
from GridCell import GridCell


class ImageGen:
    def __init__(self, data, height=5000, width=5000):
        print("Creating Blank Images...")
        self.blank_image = Image.new('RGB', (height, width), (255, 255, 255))
        self.grid_image = Image.new('RGB', (height, width), (255, 255, 255))
        #self.makegrid(self.blank_image, cols, rows)

        print("Populating Images...")
        self.makecircle(self.blank_image)
        self.makecells(self.grid_image, data)

        sqside = int((self.blank_image.width / 2) * 1.41421)

        self.grid_image = self.grid_image.resize((sqside, sqside), Image.ANTIALIAS)

        grid_origin_x = int((self.blank_image.width - self.grid_image.width) / 2)
        grid_origin_y = int((self.blank_image.height - self.grid_image.height) / 2)

        print("Combining Images...")
        self.blank_image.paste(self.grid_image, (grid_origin_x, grid_origin_y))
        print("Saving Image...")
        self.blank_image.save("chart.pdf")
        print("Image Saved")

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

    def makecells(self, img, data):
        rows, cols = data.shape
        #print(cols, rows)
        # Add Row for Header
        rows += 1
        height = img.height
        width = img.width
        col_space = int(width / cols)
        row_space = int(height / rows)
        height = row_space * rows
        width = col_space * cols
        self.grid_image = img = img.resize((width + 1, height +1), Image.ANTIALIAS)

        # print("Height:{} Width:{} Cols:{} Col_Space:{} Rows: {} Row_Space:{}".format(height, width, cols, col_space, rows, row_space))

        col_start = 0
        row_start = 0

        col_index = 0
        row_index = 0

        cells = []

        for i in range(cols):
            if i == 0 or i == cols:
                col_start = 0
                col_index = 0
            else:
                col_start += col_space
                col_index += 1
            for j in range(rows):
                if j == 0 or j == rows:
                    row_start = 0
                    row_index = 0
                else:
                    row_start += row_space
                    row_index += 1
                # print(col_start, row_start)
                # print(col_index, row_index)

                gridcell = GridCell(img, col_index, col_start, row_index, row_start, col_space, row_space)
                cells.append(gridcell)

        for cell in cells:
            # Change Background of Header Row and Populate
            if cell.row_index == 0:
                row_color = (255, 255, 0)
                cell.drawcell(background=row_color)
                cell.typeincell("{}".format(list(data.columns.values)[cell.col_index]))
                #print(list(data.columns.values)[cell.col_index])
            else:
                if cell.row_index % 2 == 0:
                    row_color = (0, 255, 0)
                else:
                    row_color = (255, 255, 255)

                cell.drawcell(background=row_color)
                # cell.typeincell("B:{} L:{}".format(cell.cell[3][0], cell.cell[3][1]))

                #print(cell.col_index, cell.row_index, data.iloc[cell.row_index - 1, cell.col_index])
                cell.typeincell("{}".format(data.iloc[cell.row_index - 1, cell.col_index]))

        #print(cells)

    def makecircle(self, img):
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, img.width, img.height), fill=(0, 0, 0), outline=(0, 0, 0))

    def drawcol(self, img, start):
        draw = ImageDraw.Draw(img)
        line = ((start, 0), (start, img.height))
        draw.line(line, fill=(0, 0, 0))

    def drawrow(self, img, start):
        draw = ImageDraw.Draw(img)
        line = ((0, start), (img.width, start))
        draw.line(line, fill=(0, 0, 0))