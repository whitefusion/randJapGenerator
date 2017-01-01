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
    yshift = 4;

    # add text on first row
    xstart = topLeft[1]
    xend   = pageS[1]-topLeft[1]-2*cellS[1]
    xstep  = 3*cellS[1]+8
    ystart = topMargin+cellS[0]/2-yshift
    yend   = ystart + rows*cellS[0]
    ystep = cellS[0]

    pageDraw = ImageDraw.Draw(pageIm)
    for x in range(xstart,xend, xstep):
        print x
        # Need to slightly adjust the location of each text
        # in order to make them "look like" in the center of the box
        for y in range(ystart,yend,ystep):
            x+=5
            pageDraw.text((x,topMargin+cellS[0]/2-yshift),"Roma",font = font)

            x+=(cellS[1]+7)
            pageDraw.text((x,topMargin+cellS[0]/2-yshift),"Hira",font = font)
            x+=(cellS[1]+2)
            pageDraw.text((x,topMargin+cellS[0]/2-yshift),"Kata",font = font)

    plt.imshow(pageIm,cmap='gray')
    plt.show()
'''
    pageDraw = ImageDraw.Draw(pageIm)
    pageDraw.text((10, 10), "Happy new year", font=font)
    pageIm.show()
'''


