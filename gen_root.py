import math
from typing import Generator


def generate_square(number_range: list) -> Generator[float, None, None]:
  first, second = tuple(number_range)
  for i in range(first, second):
    yield math.sqrt(i)


def generate_cube(number_range: list) -> Generator[float, None, None]:
  first, second = tuple(number_range)
  for i in range(first, second):
    yield math.pow(i, (1/3))
