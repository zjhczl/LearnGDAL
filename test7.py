# 修改图像分辨率
import gdal

# 打开源图像
source_filename = 'source_image.tif'
source_ds = gdal.Open(source_filename)

# 获取源图像的元数据
source_geotransform = source_ds.GetGeoTransform()
source_projection = source_ds.GetProjection()
source_band = source_ds.GetRasterBand(1)
source_x_res = source_geotransform[1]
source_y_res = abs(source_geotransform[5])

# 设置目标图像的分辨率
target_x_res = 10  # 目标横向分辨率
target_y_res = 10  # 目标纵向分辨率

# 创建重采样选项
options = gdal.WarpOptions(
    xRes=target_x_res,
    yRes=target_y_res,
    resampleAlg='bilinear'  # 选择重采样方法，可选 'near', 'bilinear', 'cubic', 等
)

# 创建目标图像
target_filename = 'target_image.tif'
target_ds = gdal.Warp(
    target_filename,
    source_ds,
    options=options
)

# 关闭源和目标图像
source_ds = None
target_ds = None

print(f'目标图像已保存到 {target_filename}')
