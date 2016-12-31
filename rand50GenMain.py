from skimage import io
from skimage.viewer import ImageViewer
from skimage.draw import polygon_perimeter
from drawTable import drawTable
from readCSV import readCsvFile
import numpy as np
import matplotlib.pyplot as plt
import os
import skimage

# import images
sheet_empty = io.imread("material\empty.JPG")
sheet_answer = io.imread("material\sampleSol.JPG")

print sheet_answer.shape
print sheet_empty.shape
viewer = ImageViewer(sheet_answer)
viewer.show()

# initialize parameter
pageS = (1018,720)
cellS = (35,40)
rows = 23
cols = 15

# draw table
page = drawTable(pageS,cellS,rows,cols)
plt.imshow(page,cmap = 'gray')
plt.show()

# read in japanese Syllabary
itemList = readCsvFile("JapSyllabary.csv")

