import math
import numpy as np

if __name__ == '__main__':
    data_set = [[0.1, 0.2, 'A'],
                [0.2, 0.1, 'A'],
                [1.1, 1.2, 'B'],
                [1.0, 0.9, 'B']]
    num_char = 2
    k = 3

    sample = [1, 1]

    for element in data_set:
        tmp = 0
        for val in range(num_char):
            tmp = tmp + (element[val]-sample[val])**2
        tmp_distance = math.sqrt(tmp)
        element.append(tmp_distance)

    data_set = np.array(data_set)

    idx = np.lexsort([data_set[:, 3]])
    data_set = data_set[idx, :]

    label = []

    for i in range(k):
        label.append(data_set[i, -2])

    # quiet tricky
    print(max(label, key=lambda x: len(x)))
