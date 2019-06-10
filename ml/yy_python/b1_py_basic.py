#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

__author__ = "Baboo J. Cui"


# function example
def bc_add(x, y):
	return x+y


# class example
class Staff(object):
	"""docstring for Staff"""
	def __init__(self, name):
		self.name = name

	# don't forget add self when declaring func in class
	def get_name(self):
		return self.name


if __name__ == "__main__":
	start_time = time.time()
	
	# use type() to see type of an object
	a = 5
	b = "Hi"
	print("a has type: ", type(a))
	print("b has type: ", type(b))
	# there are int, float, str, bool

	# int var vs str var
	c = 3
	d = 4
	e = "3"
	f = "4"
	print("c+d is: ", c+d)
	print("e+f is: ", e+f)

	# list case
	list_x = list([3, "hello", 1])
	list_x.append(7)
	print(list_x[-1])  # =7
	print(len(list_x))  # =4
	print(list_x)

	# tuple case(tuple is immutable)
	tuple_x = (3, "hello", 1)
	tuple_x = tuple_x + (7,)  # tuple has no method .append(), attention to comma
	print(tuple_x[-1])  # =7
	print(len(tuple_x))  # =4

	# dictionary
	dic = {"Baboo": "Cui", "Xinwen": "Xu"}
	print(dic["Baboo"])

	# function
	print(bc_add(11, 22))

	baboo = Staff("Baboo")
	print(baboo.get_name())

	# model
	end_time = time.time()
	print("Program is Finished!")
	print("Time cost is: ", end_time - start_time)
