from gen_combinations import generate_combinations
from gen_itertools import itertools_combinations, itertools_permutations
from gen_permutations import generate_permutations
from gen_prime import generate_prime
from gen_root import generate_cube, generate_square


class GeneratorTools:
  def iter_combinations(self, user_input, r):
    result = []
    for i in itertools_combinations(user_input, r):
      result.append(i)
    return result

  def iter_permutations(self, user_input):
    result = []
    for i in itertools_permutations(user_input):
      result.append(i)
    return result

  def combinations(self, user_input, r):
    result = []
    for i in generate_combinations(user_input, r):
      result.append(i)
    return result

  def permutations(self, user_input):
    result = []
    for i in generate_permutations(user_input):
      result.append(i)
    return result

  def square(self, first, second):
    result = []
    for i in generate_square(first, second):
      result.append(i)
    return result

  def cube(self, first, second):
    result = []
    for i in generate_cube(first, second):
      result.append(i)
    return result

  def prime(self, first, second):
    result = []
    for i in generate_prime(first, second):
      result.append(i)
    return result
  
