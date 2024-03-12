# 复制栅格

import gdal
oldTifPath = "/home/zj/data/ARC/dom/testroad/shandong-zaozhuang-testroad-001_DSM_merge.tif"
newTifPath = "/home/zj/cx/LearnGDAL/new_copy.tif"

ds = gdal.Open(oldTifPath)

# 使用driver创建栅格
driver = gdal.GetDriverByName("GTiff")
newDs = driver.CreateCopy(newTifPath, ds, strict=0)


del (newDs)
