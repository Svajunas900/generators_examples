from itertools import permutations, combinations
from typing import Generator


def itertools_permutations(input_list: list) -> Generator[list, None, None]:
  for p in permutations(input_list):
    yield p 
  

def itertools_combinations(input_list:list, r: int) -> Generator[list, None, None]:
  for c in combinations(input_list, r):
    yield c
