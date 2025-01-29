def generator_prime(first, second):
  for i in range(first, second):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
      continue
    else:
      yield i


gen = generator_prime(10, 50)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))