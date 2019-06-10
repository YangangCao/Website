#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from argparse import Namespace
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


__author__ = "Baboo J. Cui"


def tmp_function():
	pass


def generate_data(num_samples):
	x_array = np.array(range(num_samples))
	random_noise = np.random.uniform(-10, 10, size=num_samples)
	y_array = 3*x_array + 10 + random_noise
	return x_array, y_array


if __name__ == "__main__":
	start_time = time.time()
	# --------------------------------------------
	# arguments
	args = Namespace(
		seed=1234,
		num_samples=100,
		train_size=0.75,
		test_size=0.25,
		num_epochs=100,
	)
	# set for reproducability
	np.random.seed(args.seed)

	# generate data
	x, y = generate_data(args.num_samples)
	data = np.vstack([x, y]).T
	# print(data)

	# put to pandas
	df = pd.DataFrame(data, columns=["X", "Y"])
	print(df.head())

	# get plot
	# plt.title("Synthesis Data")
	# plt.scatter(x=df["X"], y=df["Y"])
	# plt.show()

	# SGD Regressor will be used instead of Normal eqn. method
	# stochastic gradient
	from sklearn.linear_model.stochastic_gradient import SGDRegressor
	from sklearn.preprocessing import StandardScaler
	from sklearn.model_selection import train_test_split

	# create data split part for training and part for testing
	# the shuffle of x and y are linked!
	x_train, x_test, y_train, y_test = train_test_split(
		df["X"].values.reshape(-1, 1),
		df["Y"],
		test_size=args.test_size,
		random_state=args.seed
	)

	# standardize the data (mean=0, std=1) using training data
	x_scaler = StandardScaler().fit(x_train)
	y_scaler = StandardScaler().fit(y_train.values.reshape(-1, 1))

	# Apply scaler on training and test data
	standardized_x_train = x_scaler.transform(x_train)
	standardized_y_train = y_scaler.transform(y_train.values.reshape(-1, 1)).ravel()
	standardized_x_test = x_scaler.transform(x_test)
	standardized_y_test = y_scaler.transform(y_test.values.reshape(-1, 1)).ravel()
	# normalize the data

	# --------------------------------------------
	end_time = time.time()
	print("Program is Finished!")
	print("Time cost is: ", end_time - start_time)
