yoruba_dictionary = {
    "water":"omi",
    "food":"ounje",
    "house":"ile",
    "man":"okunrin",
    "woman":"obirin",
    "child":"omo",
    "school":"ile-iwe",
    "book":"iwe",
    "sun":"orun",
    "moon":"osupa",
    "dog":"aja",
    "cat":"oko",
    "money":"owo",
    "road":"ona",
    "market":"oja",
    "friend":"ore",
    "teacher":"olko",
    "student":"akewi",
    "love":"ife",
    "work":"aiki"
}
word = input("Enter an English word: ").lower()
if word in yoruba_dictionary:
    print("The Yoruba word for",word,"is",yoruba_dictionary[word])
else:
    print("The Yoruba word for",word,"isn't in the dictionary")