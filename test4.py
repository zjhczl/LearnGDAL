# 创建栅格
import gdal
oldTifPath = "/home/zj/data/ARC/dom/testroad/shandong-zaozhuang-testroad-001_DSM_merge.tif"
newTifPath = "/home/zj/cx/LearnGDAL/new_changevalue.tif"

ds = gdal.Open(oldTifPath)
geoTransfrom = ds.GetGeoTransform()
proj = ds.GetProjection()
# band = ds.GetRasterBand(1).ReadAsArray()

# 使用driver创建栅格
driver = gdal.GetDriverByName("GTiff")
newDs = driver.Create(newTifPath, xsize=1000, ysize=1000,
                      bands=1, eType=gdal.GDT_Float32)

# newDs.SetProjection(proj)

newDs.SetProjection(proj)
newDs.SetGeoTransform(geoTransfrom)
band = newDs.GetRasterBand(1).ReadAsArray()
band[:500][:] = 100
newDs.GetRasterBand(1).WriteArray(band)
del (newDs)
