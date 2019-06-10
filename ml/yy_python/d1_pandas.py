#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import pandas as pd
# urllib is for url protocal
import urllib.request


__author__ = "Baboo J. Cui"


def get_csv_file():
	url = "https://raw.githubusercontent.com/GokuMohandas/practicalAI/master/data/titanic.csv"
	response = urllib.request.urlopen(url)
	html = response.read()
	with open("titanic.csv", "wb") as f:
		f.write(html)


if __name__ == "__main__":
	start_time = time.time()
	# --------------------------------------------
	# get file
	# get_csv_file()

	# get data_frame->df
	df = pd.read_csv("titanic.csv", header=0)
	# get top 5 example
	print(df.head())
	# get statistic data
	print(df.describe())
	# get histogram
	df["age"].hist()
	# get unique items
	print(df["embarked"].unique())
	# selecting data by feature
	print(df["name"].head())
	# filtering
	print(df[df["sex"] == "female"].head())  # only the female data appear, add condition in
	# sorting
	print(df.sort_values("age", ascending=False).head())
	# grouping
	survived_group = df.groupby("survived")
	print("Survive group mean info: ", survived_group.mean())
	# drop rows with Nan value
	df = df.dropna()  # removes rows with any NaN values

	# Saving data frame to CSV
	# df.to_csv("processed_titanic.csv", index=False)

	# --------------------------------------------
	end_time = time.time()
	print("Program is Finished!")
	print("Time cost is: ", end_time - start_time)
