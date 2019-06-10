#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import numpy as np

__author__ = "Baboo J. Cui"


def tmp_function():
	pass


if __name__ == "__main__":
	start_time = time.time()
	# --------------------------------------------

	# setting seed for reproducability
	np.random.seed(seed=1234)

	# declare an array
	x = np.array([[1, 2, 3], [4, 5, 6]])
	print("x ndim: ", x.ndim)
	print("x shape:", x.shape)
	print("x size: ", x.size)
	print("x data type: ", x.dtype)

	# generate arrays
	# VIP: all arg must be a tuple or list!!!
	print("np.zeros((2,2)):\n", np.zeros((2, 2)))
	print("np.ones((2,2)):\n", np.ones((2, 2)))
	print("np.eye((2)):\n", np.eye(2))
	print("np.random.random((2,2)):\n", np.random.random((2, 2)))

	# boolean array indexing
	x = np.array([[1, 2], [3, 4], [5, 6]])
	print("x:\n", x)
	print("x > 2:\n", x > 2)
	print("x[x > 2]:\n", x[x > 2])  # condition can be directly put into the bracket

	# basic math
	x = np.array([[1, 2], [3, 4]], dtype=np.float64)  # type can be directly added in
	y = np.array([[1, 2], [3, 4]], dtype=np.float64)
	print("x + y:\n", np.add(x, y))  # or x + y, MUST use np functions
	print("x - y:\n", np.subtract(x, y))  # or x - y
	print("x * y:\n", np.multiply(x, y))  # or x * y
	print("sum by col: ", np.sum(x, axis=0))  # add numbers in each column
	print("sum by row: ", np.sum(x, axis=1))  # add numbers in each row
	print("x.T:\n", x.T)  # transpose is a member not a function
	# dimension can also be controlled, but not that important
	# --------------------------------------------
	end_time = time.time()
	print("Program is Finished!")
	print("Time cost is: ", end_time - start_time)
