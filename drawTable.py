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
    topMargin = int(pageS[0] * 0.1)
    tableWidth = cols * cellS[1]
    tableHeight = rows * cellS[0]
    topleft = (topMargin, int((pageS[1]-tableWidth)/2))

    if tableWidth > pageS[1] or tableHeight > pageS[0]:
        raise "page is not big enough"

    # create page
    page = np.ones(pageS, dtype=np.uint8)

    # create outer rectangle
    r_rect, c_rect = polygon_perimeter([topleft[0], topleft[0], topleft[0]+tableHeight, topleft[0]+tableHeight, topleft[0]],
                               [topleft[1], topleft[1]+tableWidth, topleft[1]+tableWidth, topleft[1], topleft[1]],
                               shape=page.shape, clip=True)

    page[r_rect, c_rect] = 0

    # draw lines
    for y in np.linspace(topleft[0],topleft[0]+tableHeight,rows) :
        y = int(y)
        r_hline, c_hline = line(y,topleft[1],y,topleft[1]+tableWidth)
        page[r_hline,c_hline] = 0
    for x in np.linspace(topleft[1],topleft[1]+tableWidth,cols) :
        x = int(x)
        r_vline, c_vline = line(topleft[0],x,topleft[0]+tableHeight,x)
        page[r_vline,c_vline] = 0

    return page