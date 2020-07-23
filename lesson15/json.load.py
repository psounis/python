import json

with open("numbers.json", "r") as f:
    numbers = json.load(f)

print(numbers)