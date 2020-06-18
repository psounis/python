dictionary = {
    "ιταμός" : "Προκλητικός, αυθάδης, αναιδής",
    "όνειδος": "ντροπή, καταισχύνη",
    "πομφόλυγες": "αερολογίες, ανοησίες"
}

print(dictionary)

dictionary["φληναφήματα"] = "ανοησίες, σαχλαμάρες"

print(dictionary)

key = input("Δώσε τη λέξη: ")
value = input("Δώσε την επεξήγηση: ")

dictionary[key] = value

print(dictionary)