import numpy as np

zeros_array = np.zeros(4599, dtype=int)

np.save('./data/test_B_label.npy', zeros_array)