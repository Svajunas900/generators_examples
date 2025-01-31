def generate_prime(range):
  first, second = range
  for i in range(first, second):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
      continue
    else:
      yield i

