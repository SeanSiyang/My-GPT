import numpy as np
import os

dataset_path = "E:/datasets/GPT/dataset"

x_train = np.load(os.path.join(dataset_path, "mnist", "x_train.npy"))
y_train_label = np.load(os.path.join(dataset_path, "mnist", "y_train_label.npy"))

print(x_train.shape)
