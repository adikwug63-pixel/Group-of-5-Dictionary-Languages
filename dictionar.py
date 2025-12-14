idoma_dictionary = {
    "water": "ankpor",
    "food": "ogira",
    "house": "ole",
    "person": "oche",
    "man": "ochigbo",
    "woman": "onya",
    "child": "oyi",
    "sun": "oleno",
    "moon": "owia",
    "fire": "inya",
    "road": "okpokwu",
    "market": "ogwu",
    "friend": "okpakun",
    "love": "ihotu",
    "work": "ukro",
    "money": "eja",
    "tree": "ochi",
    "book": "okpa",
    "school": "enokpa",
    "king": "oche"
}
print("This are the list of word")
for language in idoma_dictionary:
    print(f"- {language}")

while True:
     language = input("choose a word from the dictionary ").lower().strip()

     if  language in idoma_dictionary:
         print(f" '{language}' means '{idoma_dictionary[language]}'")
         break
     else:
         print(f"sorry '{language}' not in dictionary ")
         break