# 创建栅格
import gdal
oldTifPath = "/home/zj/data/ARC/dom/testroad/shandong-zaozhuang-testroad-001_DSM_merge.tif"
newTifPath = "/home/zj/cx/LearnGDAL/new.tif"

ds = gdal.Open(oldTifPath)
geoTransfrom = ds.GetGeoTransform()
proj = ds.GetProjection()

# 使用driver创建栅格
driver = gdal.GetDriverByName("GTiff")
newDs = driver.Create(newTifPath, xsize=ds.RasterXSize, ysize=ds.RasterYSize,
                      bands=1, eType=gdal.GDT_Float32)

# newDs.SetProjection(proj)

newDs.SetProjection(proj)
# newDs.SetGeoTransform(geoTransfrom)
newDs.SetGeoTransform((117.410605825567, 1.5e-06, 0.0,
                      35.1092337786065, 0.0, -1.5e-06))
del (newDs)
