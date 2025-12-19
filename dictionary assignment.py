hausa_dictionary = {
    "water":"ruwa",
    "food":"abinci",
    "house":"gida",
    "man":"namiji",
    "woman":"mace",
    "child":"yaro",
    "school":"makaranta",
    "book":"littafi",
    "sun":"rana",
    "moon":"wata",
    "dog":"kare",
    "cat":"kuliya",
    "money":"kudi",
    "road":"hanya",
    "market":"kasuwa",
    "friend":"aboki",
    "teacher":"malami",
    "student":"dalibi",
    "love":"so",
    "work":"aiki"
}
word = input("Enter an English word: ").lower()
if word in hausa_dictionary:
    print("The Hausa word for",word,"is",hausa_dictionary[word])
else:
    print("The Hausa word for",word,"isn't in the dictionary")