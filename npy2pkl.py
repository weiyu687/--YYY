import numpy as np
import pickle
import os
import argparse


def npy_to_pkl(npy_file_path, pkl_dir, file_name):
    """
    将 .npy 文件转换为 .pkl 文件，其中 pkl 文件包含一个元组，
    第一个元素是一个包含 1 到数据长度的字符串数组，第二个元素是 .npy 文件中的一维数组。

    参数:
    npy_file_path (str): .npy 文件的路径。
    pkl_dir (str): 要保存的 .pkl 文件所在的目录。
    file_name (str): 指定的文件名，用于生成 .pkl 文件名。
    """
    try:
        data = np.load(npy_file_path)

        # 确保数据是一维的
        if data.ndim != 1:
            raise ValueError(f"{npy_file_path} 不是一维数组")

        # 创建包含 1 到数据长度的字符串数组
        category_names = [str(i) for i in range(1, len(data) + 1)]

        data_with_category_names = (category_names, data)

        pkl_file_path = os.path.join(pkl_dir, f'{file_name}.pkl')

        # 保存为 .pkl 文件
        with open(pkl_file_path, 'wb') as f:
            pickle.dump(data_with_category_names, f)

    except Exception as e:
        print(f"转换过程中发生错误: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将 .npy 文件转换为 .pkl 文件")

    parser.add_argument("npy_file_path", type=str, help="输入的 .npy 文件路径")
    parser.add_argument("pkl_dir", type=str, help="输出的 .pkl 文件目录")
    parser.add_argument("file_name", type=str, help="指定的文件名，用于 .pkl 文件名")

    args = parser.parse_args()

    npy_to_pkl(args.npy_file_path, args.pkl_dir, args.file_name)
