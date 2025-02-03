from typing import Generator


def generate_prime(range: list) -> Generator[int, None, None]:
  first, second = range
  for i in range(first, second):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
      continue
    else:
      yield i

