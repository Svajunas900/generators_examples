from gen_combinations import generate_combinations
from gen_itertools import itertools_combinations, itertools_permutations
from gen_permutations import generate_permutations
from gen_prime import generate_prime
from gen_root import generate_cube, generate_square


class GeneratorTools:
  def iter_combinations(self, user_input, r, second):
    result = ""
    gen_object = itertools_combinations(user_input, r)
    for _ in range(second):
      result = next(gen_object)
    return result

  def iter_permutations(self, user_input, second):
    result = ""
    gen_object = itertools_permutations(user_input)
    for _ in range(second):
      result = next(gen_object)
    return result

  def combinations(self, user_input, r, second):
    result = ""
    gen_object = generate_combinations(user_input, r)
    for _ in range(second):
      result = next(gen_object)
    return result

  def permutations(self, user_input, second):
    result = ""
    gen_object = generate_permutations(user_input)
    for _ in range(second):
      result = next(gen_object)
    return result

  def square(self, number_range, second):
    result = ""
    gen_object = generate_square(number_range)
    for _ in range(second):
      result = next(gen_object)
    return result

  def cube(self, number_range, second):
    result = ""
    gen_object = generate_cube(number_range)
    for _ in range(second):
      result = next(gen_object)
    return result

  def prime(self, number_range, second):
    result = ""
    gen_object = generate_prime(number_range)
    for _ in range(second):
      result = next(gen_object)
    return result
  
