import json

numbers = [1,2,3,4,5,6,7]

with open("numbers.json", "w") as f:
    json.dump(numbers, f)
