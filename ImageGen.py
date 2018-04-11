from PIL import Image, ImageDraw, ImageFont
from GridCell import GridCell


class ImageGen:
    def __init__(self, height, width, data):
        self.blank_image = Image.new('RGB', (height, width), (255, 255, 255))
        #self.makegrid(self.blank_image, cols, rows)
        #self.makecircle(self.blank_image)
        self.makecells(self.blank_image, data)
        print("Saving Image")
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
        self.blank_image = img = img.resize((width + 1, height +1), Image.ANTIALIAS)

        print("Height:{} Width:{} Cols:{} Col_Space:{} Rows: {} Row_Space:{}".format(height, width, cols, col_space, rows, row_space))

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
            # Change Background of Header Row
            if cell.row_index == 0:
                row_color = (255, 255, 0)
                cell.drawcell(background=row_color)
                cell.typeincell("{}".format(list(data.columns.values)[cell.col_index]))
                #print(list(data.columns.values)[cell.col_index])
            else:
                row_color = (255, 255, 255, 255)

                cell.drawcell(background=row_color)
                # cell.typeincell("B:{} L:{}".format(cell.cell[3][0], cell.cell[3][1]))

                print(cell.col_index, cell.row_index, data.iloc[cell.row_index - 1, cell.col_index])
                cell.typeincell("{}".format(data.iloc[cell.row_index - 1, cell.col_index]))

        #print(cells)

    def makecircle(self, img):
        circle_dist_x = int(img.shape[1] / 2)
        circle_dist_y = int(img.shape[0] / 2)
        circle_center_x = int(img.shape[1] / 2)
        circle_center_y = int(img.shape[0] / 2)
        #cv2.ellipse(img, (circle_center_x, circle_center_y), (circle_dist_x, circle_dist_y), 0, 0, 360, (0, 0, 0), 1)

    def drawcol(self, img, start):
        draw = ImageDraw.Draw(img)
        line = ((start, 0), (start, img.height))
        draw.line(line, fill=(0, 0, 0))

    def drawrow(self, img, start):
        draw = ImageDraw.Draw(img)
        line = ((0, start), (img.width, start))
        draw.line(line, fill=(0, 0, 0))