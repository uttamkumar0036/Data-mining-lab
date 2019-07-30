import cv2
import os
import xlsxwriter
import numpy as np
import re

os.chdir(r'D:\code\Train and test ETH 80 dataset\TrainETH80data2952')
allImage = os.listdir(".")

workbook = xlsxwriter.Workbook(r'D:\code\Train and test ETH 80 dataset\out.xlsx')
sheet = workbook.add_worksheet()

sheet.write('A1', 'Label')

sheet.write('B1', 'Mean')
sheet.write('C1', 'Standard Deviation')

row = 1
col = 0
for img in allImage:
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    imgArray = np.array(image)

    nameArray = re.split('1|2|3|4|5|6|7|8|9', img)
    label = nameArray[0]
    mean = np.mean(imgArray)
    SD = np.std(imgArray)

    sheet.write(row, col, label)
    sheet.write(row, col+1, mean)
    sheet.write(row, col+2, SD)
    row += 1
    
    print("label :",label," Mean :",mean," Standard Deviation :",SD)
  

workbook.close()
