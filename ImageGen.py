from PIL import Image, ImageDraw, ImageFont
from GridCell import GridCell
import wx
import PIL

class ImageGen:
    def __init__(self, data, callback, height=5000, width=5000):
        self.callback = callback

        self.height = height
        self.width = width
        self.data = data

        self.header_color = (255, 255, 0)
        self.row_color = (255, 255, 255)
        self.alt_row_color = (0, 255, 0)
        self.headerfontcolor = (0, 0, 0)
        self.fontcolor = (0, 0, 0)
        self.linecolor = (0, 0, 0)

    def genimage(self):
        print("Creating Blank Image...")
        self.callback("Creating Blank Image...")
        self.blank_image = Image.new('RGB', (self.height, self.width), (255, 255, 255))
        if not self.data.empty:
            print("Creating Grid Image...")
            self.callback("Creating Grid Image...")
            self.grid_image = Image.new('RGB', (self.height, self.width), (255, 255, 255))
            #self.makegrid(self.blank_image, cols, rows)

            print("Populating Images...")
            self.callback("Populating Images...")
            self.makecircle(self.blank_image)
            self.makecells(self.grid_image, self.data)

            sqside = int((self.blank_image.width / 2) * 1.41421)

            self.grid_image = self.grid_image.resize((sqside, sqside), Image.ANTIALIAS)

            grid_origin_x = int((self.blank_image.width - self.grid_image.width) / 2)
            grid_origin_y = int((self.blank_image.height - self.grid_image.height) / 2)

            print("Combining Images...")
            self.callback("Combining Images...")
            self.blank_image.paste(self.grid_image, (grid_origin_x, grid_origin_y))
            print("Images Combined")
            self.callback("Images Combined.")
        else:
            print("Data Empty")
            self.callback("Data Empty Please Load A Ballistics File.")

    def getimage(self):
        return self.blank_image

    def setheadercolor(self, color):
        self.header_color = tuple(color)
        self.callback("Header Color:".format(self.header_color))

    def setrowcolor(self, color):
        self.row_color = tuple(color)
        self.callback("Row Color:".format(self.row_color))

    def setaltrowcolor(self, color):
        self.alt_row_color = tuple(color)
        self.callback("Alt Row Color:".format(self.alt_row_color))

    def setlinecolor(self, color):
        self.linecolor = tuple(color)
        self.callback("Line Color:".format(self.alt_row_color))

    def setheaderfontcolor(self, color):
        self.headerfontcolor = tuple(color)
        self.callback("Header Font Color:".format(self.alt_row_color))

    def setfontcolor(self, color):
        self.fontcolor = tuple(color)
        self.callback("Font Color:".format(self.alt_row_color))

    def getwximage(self):
        myPilImage = self.blank_image
        copyAlpha = True
        hasAlpha = myPilImage.mode[-1] == 'A'
        if copyAlpha and hasAlpha:  # Make sure there is an alpha layer copy.

            myWxImage = wx.EmptyImage(*myPilImage.size)
            myPilImageCopyRGBA = myPilImage.copy()
            myPilImageCopyRGB = myPilImageCopyRGBA.convert('RGB')  # RGBA --> RGB
            myPilImageRgbData = myPilImageCopyRGB.tostring()
            myWxImage.SetData(myPilImageRgbData)
            myWxImage.SetAlphaData(myPilImageCopyRGBA.tobytes()[3::4])  # Create layer and insert alpha values.

        else:  # The resulting image will not have alpha.

            myWxImage = wx.Image(*myPilImage.size)
            myPilImageCopy = myPilImage.copy()
            myPilImageCopyRGB = myPilImageCopy.convert('RGB')  # Discard any alpha from the PIL image.
            myPilImageRgbData = myPilImageCopyRGB.tobytes()
            myWxImage.SetData(myPilImageRgbData)

        return myWxImage

    def getwxbitmap(self):
        return wx.Bitmap(self.getwximage())

    def imgsave(self, filename="chart.pdf"):
        print("Saving Image...")
        self.callback("Saving Image...")
        self.blank_image.save(filename)
        print("Image Saved")
        self.callback("Image Saved.")

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
                cell.drawcell(self.header_color, self.linecolor)
                cell.typeincell("{}".format(list(data.columns.values)[cell.col_index]), self.headerfontcolor)
                #print(list(data.columns.values)[cell.col_index])
            else:
                if cell.row_index % 2 == 0:
                    row_color = self.alt_row_color
                else:
                    row_color = self.row_color

                cell.drawcell(row_color, self.linecolor)
                # cell.typeincell("B:{} L:{}".format(cell.cell[3][0], cell.cell[3][1]))

                #print(cell.col_index, cell.row_index, data.iloc[cell.row_index - 1, cell.col_index])
                cell.typeincell("{}".format(data.iloc[cell.row_index - 1, cell.col_index]), self.fontcolor)

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