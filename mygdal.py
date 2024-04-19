# 自己的gdal库
import gdal
from osgeo import ogr


def tif_cat_by_shp():

    # 打开TIF文件
    tif_filename = 'input_image.tif'
    tif_ds = gdal.Open(tif_filename)

    # 打开SHP文件
    shp_filename = 'clip_boundary.shp'
    shp_ds = ogr.Open(shp_filename)
    shp_layer = shp_ds.GetLayer()

    # 创建一个新的文件名用于存储裁剪后的TIF文件
    output_tif_filename = 'clipped_image.tif'

    # 设置裁剪选项
    options = gdal.WarpOptions(
        format='GTiff',  # 输出格式为GeoTIFF
        cutlineDSName=shp_filename,  # 指定裁剪用的SHP文件
        cutlineLayer='clip_boundary',  # 指定SHP文件的图层
        cropToCutline=True,  # 只裁剪到指定的cutline
        dstSRS=tif_ds.GetProjection(),  # 保持目标图像的投影与源图像一致
        resampleAlg='bilinear'  # 重采样方法，可选 'near', 'bilinear', 'cubic' 等
    )

    # 执行裁剪操作
    clipped_ds = gdal.Warp(
        output_tif_filename,
        tif_ds,
        options=options
    )

    # 关闭文件
    tif_ds = None
    shp_ds = None
    clipped_ds = None

    print(f'裁剪后的TIF文件已保存到 {output_tif_filename}')


# 使用gdal.Warp进行重采样
def resampling(source_tif, target_tif, kml_path=None):

    # 打开源图像
    source_filename = source_tif
    source_ds = gdal.Open(source_filename)

    # 获取源图像的元数据
    # source_geotransform = source_ds.GetGeoTransform()
    # source_projection = source_ds.GetProjection()
    # source_band = source_ds.GetRasterBand(1)
    # source_x_res = source_geotransform[1]
    # source_y_res = abs(source_geotransform[5])

    # 设置目标图像的分辨率
    target_x_res = 10  # 目标横向分辨率
    target_y_res = 10  # 目标纵向分辨率

    # 创建重采样选项
    options = gdal.WarpOptions(
        cutlineDSName=kml_path,  # 指定KML文件用于裁剪
        xRes=target_x_res,
        yRes=target_y_res,
        resampleAlg='bilinear'  # 选择重采样方法，可选 'near', 'bilinear', 'cubic', 等
    )

    # 创建目标图像
    target_filename = target_tif
    target_ds = gdal.Warp(
        target_filename,
        source_ds,
        options=options
    )

    # 关闭源和目标图像
    source_ds = None
    target_ds = None

    print(f'目标图像已保存到 {target_filename}')


# 转换坐标系
def transfrom_crs(input_file, output_file, epsg):
    pass

    # 初始化输入和输出栅格数据集
    input_raster = gdal.Open(input_file)
    output_raster = output_file

    # 设置目标坐标系
    # 以EPSG:32633 (WGS 84 / UTM zone 33N)为例
    dst_crs = epsg

    # 创建一个新的重投影数据集
    gdal.Warp(output_raster, input_raster, dstSRS=dst_crs)

    # 清理
    input_raster = None


# 输入和输出文件路径
input_file = '/home/zj/data/ARC/dom/wulumuqi/Production_5_DSM_merge.tif'
output_file = '/home/zj/data/ARC/dom/wulumuqi/Production_5_DSM_merge-90e.tif'
resampling_file = "/home/zj/data/ARC/dom/wulumuqi/Production_5_DSM_merge-90e-resampling.tif"
kml_path = "/home/zj/data/ARC/kml/k2.kml"
dst_crs = 'EPSG:4539'
# transfrom_crs(input_file, output_file, dst_crs)
resampling(output_file, resampling_file, kml_path)
