def generate_prime(first, second):
  for i in range(first, second):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
      continue
    else:
      yield i

