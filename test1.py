# tif基本信息
import gdal
tifPath = "/home/zj/data/ARC/dom/xiangtan/Production_3_DSM_merge_msl.tif"

ds = gdal.Open(tifPath)
# 获取tif大小
print(ds.RasterXSize, ds.RasterYSize)

# 投影
# GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AXIS["Latitude",NORTH],AXIS["Longitude",EAST],AUTHORITY["EPSG","4326"]]
# GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AXIS["Latitude",NORTH],AXIS["Longitude",EAST],AUTHORITY["EPSG","4326"]]
# 让我们分解这个字符串以更好地理解它的各个部分：
# GEOGCS["WGS 84", ...]: 表示这是一个地理坐标系统，名为"WGS 84"。
# DATUM["WGS_1984", ...]: 指定了使用的地球基准面，即"WGS 1984"。
# SPHEROID["WGS 84",6378137,298.257223563, ...]: 描述了参考椭球体。这里的椭球体也命名为"WGS 84"，它的半长轴（赤道半径）是6378137米，扁率的倒数是298.257223563。
# AUTHORITY["EPSG","7030"]: 指定了椭球体的EPSG代码是7030。
# AUTHORITY["EPSG","6326"]: 指定了基准面的EPSG代码是6326。
# PRIMEM["Greenwich",0]: 定义了本初子午线在格林威治，其值为0度。
# UNIT["degree",0.0174532925199433, ...]: 定义了坐标单位是度（degree），并给出了度到弧度的转换因子（π/180）。
# AXIS["Latitude",NORTH], AXIS["Longitude",EAST]: 定义了坐标轴的方向，纬度（Latitude）向北，经度（Longitude）向东。
# AUTHORITY["EPSG","4326"]: 最后，这个是整个地理坐标系统的EPSG代码，4326。
# 这个坐标系统定义是非常重要的，因为它告诉GIS软件和其他使用这些数据的工具如何解释坐标值。在WGS 84坐标系统中，坐标值通常表示为经度和纬度，这是一个全球参照系统，被用于全球定位系统（GPS）和许多国际地图产品中。
print(ds.GetProjection())

# 坐标转换 坐标定义 (117.410605825567, 1.5e-06, 0.0, 35.1092337786065, 0.0, -1.5e-06)
# 这些数值定义了像素坐标和地理坐标之间的关系
# 参数 1 (117.410605825567): 栅格图像的x坐标原点（通常是左上角）的东坐标（或经度）。
# 参数 2 (1.5e-06): 一个像素宽度的东向地理单位数（通常表示一个像素的经度跨度）。
# 参数 3 (0.0): 旋转项，如果北方向与行的方向一致，则通常为0。
# 参数 4 (35.1092337786065): 栅格图像的y坐标原点（通常是左上角）的北坐标（或纬度）。
# 参数 5 (0.0): 旋转项，如果东方向与列的方向一致，则通常为0。
# 参数 6 (-1.5e-06): 一个像素高度的北向地理单位数（通常表示一个像素的纬度跨度）。这里的负号表示纬度随着行号增加而减小，这通常意味着图像的原点在左上角。
print(ds.GetGeoTransform())

# 波段数
print(f"波段数：{ds.RasterCount}")
band1 = ds.GetRasterBand(1)
print(band1)
# 无数据值用于标记栅格数据中的某些像素不包含有效信息，这通常用于表示图像的空白区域或者在分析过程中应该忽略的数据。
# 例：如果您发现无数据值是 -9999.0，这意味着在该栅格数据集的波段中，所有值为 -9999.0 的像素应被视为无效数据，不应该被包括在数据分析中。
print(f"无数据值：{band1.GetNoDataValue()}")

# 最大值最小值
# 暂时有点问题 需要关联文件
print(f"最大值：{band1.GetMaximum()}")
print(f"最小值：{band1.GetMinimum()}")
print(f"data type：{band1.GetUnitType()}")

bandArry = band1.ReadAsArray()
print(bandArry)
print(bandArry.shape)

# 数组中的最大值
print(bandArry.max())

# 数组中的最小值
print(bandArry.min())

# 平均值
print(bandArry.mean())

# 求和
print(bandArry.sum())
