from itertools import permutations, combinations

def itertools_permutations(input_list: list):
  for p in permutations(input_list):
    yield p 
  

def itertools_combinations(input_list:list, r):
  for c in combinations(input_list, r):
    yield c
