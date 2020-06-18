merchandise = {
    "book": 10.18,
    "parsley": 0.22,
    "cement": 5.17,
    "cd": 0.05
}

rate = 2.2

new_values = { key: value*rate for key, value in merchandise.items()}

print(new_values)
