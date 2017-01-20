from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import numpy as np
import math
from getTextDimensions import GetTextDimensions

def drawText(page, charList,idPermute,pageS,cellS,rows,cols,option) :

    # Set up page and text parameters
    fontsize = 12
    fontType = "yumindb"
    font = ImageFont.truetype("material/yumindb.ttf", fontsize)
    page_copy = np.copy(page)
    pageIm = Image.fromarray(np.uint8(page) * 255)
    pageIm_copy = Image.fromarray(np.uint8(page_copy) * 255)

    topMargin = int(pageS[0] * 0.1)
    tableWidth = cols * cellS[1]
    tableHeight = rows * cellS[0]
    topLeft = (topMargin, int((pageS[1]-tableWidth)/2))
    yshift = fontsize/2; #font size is the height of the font

    xstart = topLeft[1]+int(cellS[1]/2)
    xend   = pageS[1]-topLeft[1]-int(cellS[1]/2)
    xstep  = 3*cellS[1]

    ystart = topMargin+int(cellS[0]/2)-yshift
    yend   = ystart + tableHeight
    ystep  = cellS[0]

    pageDraw = ImageDraw.Draw(pageIm)
    pageDrawNoAnswer = ImageDraw.Draw(pageIm_copy)
    ycount = 0
    yrange = range(ystart + cellS[0], yend, (ystep))


    charArray = np.asarray(charList)
    # Add text row by row
    # Need to slightly adjust the location of each text
    # in order to make them "look like" in the center of the box
    xR,_ = GetTextDimensions("Roma", fontsize, fontType)
    xH,_ = GetTextDimensions("Hira", fontsize, fontType)
    xK,_ = GetTextDimensions("Kata", fontsize, fontType)
    for x in range(xstart, xend, xstep):
        randCharList = charArray[idPermute[ycount:min(ycount+rows-1,len(charList))],:]

        pageDraw.text((x-(xR/2)-3, ystart), "Roma", font=font)
        pageDrawNoAnswer.text((x-(xR/2), ystart), "Roma", font=font)
        for item in enumerate(randCharList):
            x0,_=GetTextDimensions(item[1][0],fontsize,fontType)
            pageDraw.text((x-(x0/2)-2,yrange[item[0]]),item[1][0],font = font)
            if(option < 2):
                pageDrawNoAnswer.text((x-(x0/2)-2, yrange[item[0]]), item[1][0], font=font)

        x += (cellS[1] )
        pageDraw.text((x-xH/2-3, ystart), "Hira", font=font)
        pageDrawNoAnswer.text((x-xH/2, ystart), "Hira", font=font)
        for item in enumerate(randCharList):
            x1, _ = GetTextDimensions(item[1][1], fontsize, fontType)
            pageDraw.text((x-x1/2,yrange[item[0]]),unicode(item[1][1],"utf-8"),font = font)
            if(option == 2):
                pageDrawNoAnswer.text((x-(x0/2)-2, yrange[item[0]]), unicode(item[1][1],"utf-8"), font=font)

        x += (cellS[1] )
        pageDraw.text((x-xK/2-2, ystart), "Kata", font=font)
        pageDrawNoAnswer.text((x-xK/2, ystart), "Kata", font=font)
        for item in enumerate(randCharList):
            x2, _ = GetTextDimensions(item[1][2], fontsize, fontType)
            pageDraw.text((x-x2/2,yrange[item[0]]),unicode(item[1][2],"utf-8"),font = font)

        ycount += rows-1

    return pageIm_copy, pageIm



