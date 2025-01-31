import math


def generate_square(number_range):
  first, second = number_range
  for i in range(first, second):
    yield math.sqrt(i)


def generate_cube(number_range):
  first, second = tuple(number_range)
  for i in range(first, second):
    yield math.pow(i, (1/3))
