from drawTable import drawTable
from readCSV import readCsvFile
from drawText import drawText
from PIL import Image
import numpy as np
import math
import sys

# read in document
itemList = readCsvFile(str(sys.argv[1]))

# initialize parameter
pageS = (1018,720)
cellS = (35,40)
charPerRow = 5
# assume 5 chars per row
cols = 15
rows = math.ceil(itemList.__len__()/charPerRow)

'''
rows = 23
cols = 15
topMargin = int(pageS[0] * 0.1)
tableWidth = cols * cellS[1]
tableHeight = rows * cellS[0]
topLeft = (topMargin, int((pageS[1] - tableWidth) / 2))
'''


# draw table
page = drawTable(pageS,cellS,rows,cols)
#plt.imshow(page,cmap = 'gray')
#plt.show()

# randomize the itemlist
permute = np.random.permutation(len(itemList))

# fill items into the cell
exerSheet, Solution = drawText(page, itemList,permute,pageS,cellS,rows,cols)

# convert image to PDF and export
size = [4*x for x in exerSheet.size]
exerSheet_resized = exerSheet.resize(size, Image.ANTIALIAS)
Solution_resized = Solution.resize(size, Image.ANTIALIAS)
exerSheet_resized.save("dictation.pdf")
Solution_resized.save("solution.pdf")
