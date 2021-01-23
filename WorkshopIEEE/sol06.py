text = "He earned a number of honours, including two Peabody " \
       "awards, but was also criticised for his non-confrontational" \
       " approach and open-ended questions. King boasted of not doing" \
       " much research for the interviews so, he said, he could learn along" \
       " with viewers."

characters = list(text)
print(characters)

my_dictionary = {}


for character in characters:
    if character in my_dictionary.keys():
        my_dictionary[character] += 1
    else:
        my_dictionary[character] = 1

print(my_dictionary)