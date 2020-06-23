string = """
How the hell could a person enjoy being awakened at 6:30AM, 
by an alarm clock, leap out of bed, dress, force-feed, shit, piss, 
brush teeth and hair, and fight traffic to get to a place 
where essentially you made lots of money for somebody else 
and were asked to be grateful for the opportunity to do so?"""

lower = string.lower()
letters = set(lower)
dictionary = {letter: 0 for letter in letters}

for char in lower:
    dictionary[char] += 1

for char in " ,-036:?\n":
    dictionary.pop(char)

for key in sorted(dictionary.keys()):
    print(key + ": " + str(dictionary[key]))
