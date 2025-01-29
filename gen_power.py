import math


def generate_pow(first, second):
  for i in range(first, second):
    yield math.pow(i, 2)

