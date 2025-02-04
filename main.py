from gen_class import GeneratorTools
from flask import Flask, request, session
import json
from typing import Union
from models import User


app = Flask(__name__)


@app.get("/")
def home(q: Union[str, None] = None):
  return {"Hello world": "Hello world", "q": q}


@app.post("/generators")
def generators():
  data = request.get_json()
  method = data["gen_method"]
  number_range = data["range"]
  second_number = data["second"]
  gen_tools = GeneratorTools()
  if method == "itertools_combination":
    result = gen_tools.iter_combinations(number_range, 2, second_number)
  if method == "itertools_permutation":
    result = gen_tools.iter_permutations(number_range, second_number)
  if method == "combination":
    result = gen_tools.combinations(number_range, second_number)
  if method == "permutation":
    result = gen_tools.iter_permutations(number_range, second_number)
  if method == "square":
    result = gen_tools.square(number_range, second_number)
  if method == "cube":
    result = gen_tools.cube(number_range, second_number)
  if method == "prime":
    result = gen_tools.prime(number_range, second_number)
  return json.dumps({"Method": method,
                     "Result": result})


if __name__ == "__main__":
  app.run(debug=True)