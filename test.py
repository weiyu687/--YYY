import numpy as np


def print_npy_info(file_path):
    """
    打印.npy文件的形状和内容。

    参数:
    file_path (str): .npy文件的路径。
    """
    # 加载npy文件
    data = np.load(file_path)

    # 打印数组的形状
    print(f"Shape of the array: {data.shape}")

    # 打印数组的内容
    print("Content of the array:")
    print(data)


# 使用函数
npy_file_path = 'pred.npy'  # 假设你的npy文件名为output.npy
print_npy_info(npy_file_path)
