import json, string

def check(text):
    if {i.lower().translate(str.maketrans("", "", string.punctuation))\
        for i in text.split(" ")}.intersection(set(json.load(open("cenz.json")))) != set():
        return True
    else:
        return False

print(check(""))

