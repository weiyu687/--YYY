import pickle
import numpy as np
import os


def pkl_to_npy(pkl_file_path, npy_output_dir):
    """
    将.pkl文件转换为.npy文件。

    参数:
    pkl_file_path (str): .pkl文件的路径。
    npy_output_dir (str): 输出.npy文件的目录。
    """
    # 读取.pkl文件
    with open(pkl_file_path, 'rb') as f:
        data_dict = pickle.load(f)

    keys = sorted(data_dict.keys(), key=int)
    num_samples = len(keys)

    # 创建一个空的numpy数组，用于存储所有的置信度值
    confidence_scores = np.zeros((num_samples, 155))

    for i, key in enumerate(keys):
        confidence_scores[i] = data_dict[key]

    base_name = os.path.basename(pkl_file_path)
    npy_file_name = 'pred.npy'
    npy_file_path = os.path.join(npy_output_dir, npy_file_name)

    # 保存为.npy文件
    np.save(npy_file_path, confidence_scores)
    print(f"File saved to: {npy_file_path}")


if __name__ == "__main__":
    # pkl_file_path = '../epoch1_test_score.pkl'
    # npy_output_dir = '../temp'
    # pkl_to_npy(pkl_file_path, npy_output_dir, 1)
    pass
