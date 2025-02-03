from typing import Generator


def generate_combinations(user_input:list, r:int) -> Generator[list, None, None]:
  if r == 0:
    yield []
  elif len(user_input) == 0 or r > len(user_input):
    return
  else:
    for combo in generate_combinations(user_input[1:], r - 1):
      yield [user_input[0]] + combo
    yield from generate_combinations(user_input[1:], r)


