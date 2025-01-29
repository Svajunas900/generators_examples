from itertools import permutations, combinations

def generate_permutations(input_list: list):
  for p in permutations(input_list):
    yield p 
  

def generate_combinations(input_list:list, r):
  for c in combinations(input_list, r):
    yield c


gen_per = generate_permutations([1,2,3])
gen_com = generate_combinations([1,2,3], 2)

print(next(gen_per))
print(next(gen_per))
print(next(gen_com))
print(next(gen_com))