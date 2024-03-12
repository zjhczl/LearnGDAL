# no data values

import gdal
# tifPath = "/home/zj/cx/LearnGDAL/new_changevalue.tif"
tifPath = "/home/zj/data/ARC/dom/testroad/shandong-zaozhuang-testroad-001_DSM_merge.tif"
ds = gdal.Open(tifPath)
band = ds.GetRasterBand(1)

print(band.GetNoDataValue())
bandArray = band.ReadAsArray()
bandArray[bandArray == band.GetNoDataValue()] = 22

print(bandArray.min())
