def generate_permutations(input_list: list):
  if len(input_list) == 0:
        yield []
  elif len(input_list) == 1:
      yield input_list
  else:
    for i in range(len(input_list)):
      rest = input_list[:i] + input_list[i+1:]
      for perm in generate_permutations(rest):
        yield [input_list[i]] + perm
