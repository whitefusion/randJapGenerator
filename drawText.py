from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import numpy as np

def drawText(page, charList,pageS,cellS,rows,cols) :
    # define text parameters
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

    # randomize the charList


    # add text
    xstart = topLeft[1]+5
    xend   = pageS[1]-topLeft[1]-2*cellS[1]
    xstep  = 3*cellS[1]+8

    ystart = topMargin+cellS[0]/2-yshift
    yend   = ystart + rows*cellS[0]
    ystep  = cellS[0]

    pageDraw = ImageDraw.Draw(pageIm)

    ycount = 0
    yrange = range(ystart + cellS[0], yend, (ystep+2))
    for x in range(xstart, xend, xstep):
        # Need to slightly adjust the location of each text
        # in order to make them "look like" in the center of the box
        pageDraw.text((x, ystart), "Roma", font=font)

        for item in enumerate(charList[ycount:min(ycount+rows-2,len(charList))]):
            pageDraw.text((x+1,yrange[item[0]]),item[1][0],font = font)

        x += (cellS[1] + 7)
        pageDraw.text((x, ystart), "Hira", font=font)

        for item in enumerate(charList[ycount:min(ycount+rows-2,len(charList))]):
            pageDraw.text((x+1,yrange[item[0]]),unicode(item[1][1],"utf-8"),font = font)

        x += (cellS[1] + 2)
        pageDraw.text((x, ystart), "Kata", font=font)

        for item in enumerate(charList[ycount:min(ycount+rows-2,len(charList))]):
            pageDraw.text((x+1,yrange[item[0]]),unicode(item[1][2],"utf-8"),font = font)

        ycount += rows

    plt.imshow(pageIm,cmap='gray')
    plt.show()
'''
    pageDraw = ImageDraw.Draw(pageIm)
    pageDraw.text((10, 10), "Happy new year", font=font)
    pageIm.show()
'''


