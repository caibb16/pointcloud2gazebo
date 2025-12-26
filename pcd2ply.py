import open3d as o3d

# 读取 PCD
pcd = o3d.io.read_point_cloud("scans.pcd")

# 保存为 PLY
o3d.io.write_point_cloud("output.ply", pcd)