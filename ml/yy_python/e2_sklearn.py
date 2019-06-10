#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

__author__ = "Baboo J. Cui"


def tmp_function():
    pass


if __name__ == "__main__":
    start_time = time.time()
    # --------------------------------------------

    # train test split
    import numpy as np
    from sklearn.model_selection import train_test_split

    # reshape(-1, 1): to one column but unknown num of row
    x, y = np.arange(10).reshape((5, 2)), range(5)
    print("x is: \n", x)
    print("y is: \n", y)
    print("y list is: \n", list(y))

    # test split(*array, **options)
    # split arrays or matrices into random train and test subsets
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.33,
        random_state=123
    )
    # comments: *array MUST have the same length(num of row)
    # output row is randomized

    # --------------------------------------------
    end_time = time.time()
    print("Program is Finished!")
    print("Time cost is: ", end_time - start_time)
