import numpy as np


def calculate_accuracy(labels_path, predictions_path):
    """
    计算预测的准确率。

    参数:
    labels_path (str): 包含真实标签的npy文件路径。
    predictions_path (str): 包含预测结果（每个类别的置信度）的npy文件路径。

    返回:
    float: 预测的准确率。
    """
    labels = np.load(labels_path)
    predictions = np.load(predictions_path)

    # 确保标签和预测结果的样本数量一致
    assert labels.shape[0] == predictions.shape[0], "The number of samples in the labels and predictions must match."

    # 对于每个样本，找到预测置信度最高的类别
    predicted_classes = np.argmax(predictions, axis=1)

    correct_predictions = (predicted_classes == labels).sum()
    accuracy = correct_predictions / len(labels)

    print(f"Accuracy: {accuracy * 100:.2f}%")

    return accuracy


if __name__ == "__main__":
    # labels_file_path = 'test_A_label.npy'
    # predictions_file_path = '../temp.npy'
    # calculate_accuracy(labels_file_path, predictions_file_path)
    pass

