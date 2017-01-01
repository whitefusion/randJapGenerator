from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import numpy as np

def drawText(page, charList,pageS,cellS,rows,cols) :
    fontsize = 12
    font = ImageFont.truetype("material/yumindb.ttf", fontsize)
    pageIm = Image.fromarray(np.uint8(page) * 255)
    rows+=1
    cols+=1
    topMargin = int(pageS[0] * 0.1)
    tableWidth = cols * cellS[1]
    tableHeight = rows * cellS[0]
    topLeft = (topMargin, int((pageS[1]-tableWidth)/2))

    # add text on first row
    pageDraw = ImageDraw.Draw(pageIm)
    for x in range(topLeft[1],pageS[1]-topLeft[1]-2*cellS[1], 3*cellS[1]+10):
        print x
        pageDraw.text((x,topMargin+cellS[0]/2-fontsize/2),"Roma",font = font)

    pageIm.show()
'''
    pageDraw = ImageDraw.Draw(pageIm)
    pageDraw.text((10, 10), "Happy new year", font=font)
    pageIm.show()
'''


