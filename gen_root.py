import math


def generate_square(first, second):
  for i in range(first, second):
    yield math.sqrt(i)


def generate_cube(first, second):
  for i in range(first, second):
    yield math.pow(i, (1/3))
