# 栅格相减

import gdal
# 打开第一个栅格文件
raster1_filename = 'raster1.tif'
raster1_ds = gdal.Open(raster1_filename)
raster1_band = raster1_ds.GetRasterBand(1)
raster1_data = raster1_band.ReadAsArray()

# 打开第二个栅格文件
raster2_filename = 'raster2.tif'
raster2_ds = gdal.Open(raster2_filename)
raster2_band = raster2_ds.GetRasterBand(1)
raster2_data = raster2_band.ReadAsArray()

# 检查两个栅格的尺寸是否匹配
assert raster1_data.shape == raster2_data.shape, "两个栅格文件的尺寸不匹配"

# 执行栅格相减操作
result_data = raster1_data - raster2_data

# 获取栅格的元数据
geotransform = raster1_ds.GetGeoTransform()
projection = raster1_ds.GetProjection()

# 创建一个新的目标栅格文件来保存相减结果
output_filename = 'result.tif'
driver = gdal.GetDriverByName('GTiff')
result_ds = driver.Create(
    output_filename, raster1_data.shape[1], raster1_data.shape[0], 1, gdal.GDT_Float32)

# 设置目标栅格的元数据
result_ds.SetGeoTransform(geotransform)
result_ds.SetProjection(projection)

# 将结果写入目标栅格文件
result_band = result_ds.GetRasterBand(1)
result_band.WriteArray(result_data)

# 刷新并关闭文件
result_band.FlushCache()
result_ds = None

# 关闭源栅格文件
raster1_ds = None
raster2_ds = None

print(f'栅格相减结果已保存到 {output_filename}')
