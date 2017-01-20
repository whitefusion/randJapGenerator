from drawTable import drawTable
from readCSV import readCsvFile
from drawText import drawText
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
import sys

# Read in document
def option(x):
    return {
        '-Roma': 1,
        '-Hara': 2,
        '-Help': -1
    }[x]

if(sys.argv.__len__() > 2):
    opt = option(sys.argv[2])
    itemList = readCsvFile(sys.argv[1])
else:
    opt = 0
    itemList = readCsvFile('JapSyllabary.csv')

if(opt == -1):
    print('python *.csv -option \n')
    print('-option: \n')
    print('-Roma: show roma pronounciation only \n')
    print('-Hara: show haragana only')
    sys.exit()

# Default page size and cell size
pageS = (1018,720)
cellS = (36,40)
charPerRow = 5.0

# Number of rows and cols depends on the size of documents
cols = int(3*charPerRow)
rows = int(math.ceil(itemList.__len__()/charPerRow))+1

# Draw table
page = drawTable(pageS,cellS,rows,cols)

# Randomize the itemlist
permute = np.random.permutation(len(itemList))

# Fill items into the cell
exerSheet, Solution = drawText(page, itemList,permute,pageS,cellS,rows,cols,opt)

# Convert image to PDF and export
size = [4*x for x in exerSheet.size]
exerSheet_resized = exerSheet.resize(size, Image.ANTIALIAS)
Solution_resized = Solution.resize(size, Image.ANTIALIAS)
exerSheet_resized.save("dictation.pdf")
Solution_resized.save("solution.pdf")
