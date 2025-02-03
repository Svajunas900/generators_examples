import math
from typing import Generator


def generate_pow(range: list) -> Generator[float, None, None]:
  first, second = range
  for i in range(first, second):
    yield math.pow(i, 2)

