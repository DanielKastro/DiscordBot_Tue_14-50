import json


list = []
with open("bad_words.txt", "r", encoding="utf-8") as file:
    for i in file:
        word = i.lower().split("\n")[0]
        if word != "" or word != " ":
            list.append(word)


with open("cenz.json", "w", encoding="utf-8") as j:
    json.dump(list, j)

