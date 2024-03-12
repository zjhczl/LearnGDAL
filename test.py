# tif转png

import time
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
ds = gdal.Open("/home/zj/data/changdi/Production_1_ortho_merge.tif")
print("get band")
print(ds.RasterCount)
band1 = ds.GetRasterBand(1).ReadAsArray()
band2 = ds.GetRasterBand(2).ReadAsArray()
band3 = ds.GetRasterBand(3).ReadAsArray()
colorimg = cv.merge((band3, band2, band1))

print("show")
cv.imshow('Image', colorimg)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("./merge.png", colorimg)
cv.destroyAllWindows()
