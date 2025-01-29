from gen_class import GeneratorTools
from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/")
def home():
  return "Hello world"


@app.post("/generators")
def generators():
  data = request.get_json()
  method = data["gen_method"]
  gen_list = data["gen_list"]
  first_number = data["first"]
  second_number = data["second"]
  gen_tools = GeneratorTools()
  if method == "itertools_combination":
    result = gen_tools.iter_combinations(gen_list, first_number)
  if method == "itertools_permutation":
    result = gen_tools.iter_permutations(gen_list)
  if method == "combination":
    result = gen_tools.combinations(gen_list, first_number)
  if method == "permutation":
    result = gen_tools.iter_permutations(gen_list)
  if method == "square":
    result = gen_tools.square(first_number, second_number)
  if method == "cube":
    result = gen_tools.cube(first_number, second_number)
  if method == "prime":
    result = gen_tools.prime(first_number, second_number)
  return json.dumps({"Method": method,
                     "Result": result})


if __name__ == "__main__":
  app.run(debug=True)