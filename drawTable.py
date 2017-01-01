# The function draws a table based on pageSize, cell size, rows and columns
'''
pageS : tuple(Height, Width) of page(ndArray)
cellS : tuple(Height, Width) of a single Cell
'''
import numpy as np
from skimage.draw import polygon_perimeter
from skimage.draw import line

def drawTable(pageS,cellS,rows,cols) :

    # set up layout parameters
    rows+=1
    cols+=1
    topMargin = int(pageS[0] * 0.1)
    tableWidth = cols * cellS[1]
    tableHeight = rows * cellS[0]
    topLeft = (topMargin, int((pageS[1]-tableWidth)/2))

    if tableWidth > pageS[1] or tableHeight > pageS[0]:
        raise "page is not big enough"

    # create page
    page = np.ones(pageS, dtype=np.uint8)

    # create outer rectangle
    r_rect, c_rect = polygon_perimeter([topLeft[0], topLeft[0], topLeft[0]+tableHeight, topLeft[0]+tableHeight, topLeft[0]],
                               [topLeft[1], topLeft[1]+tableWidth, topLeft[1]+tableWidth, topLeft[1], topLeft[1]],
                               shape=page.shape, clip=True)

    page[r_rect, c_rect] = 0

    # draw lines
    for y in np.linspace(topLeft[0],topLeft[0]+tableHeight,rows) :
        y = int(y)
        r_hline, c_hline = line(y,topLeft[1],y,topLeft[1]+tableWidth)
        page[r_hline,c_hline] = 0
    for x in np.linspace(topLeft[1],topLeft[1]+tableWidth,cols) :
        x = int(x)
        r_vline, c_vline = line(topLeft[0],x,topLeft[0]+tableHeight,x)
        page[r_vline,c_vline] = 0

    return page