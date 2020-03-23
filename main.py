import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        fword = get_close_matches(word, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % fword)
        if yn == "Y":
            return data[fword]
        elif yn == "N":
            return "The word doesn't exist"
        else:
            return "We didn't understand your query"
    else:
        return "The word doesn't exist"

word = input("Enter any word: ");

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

##############################
# data.keys()
# print(get_close_matches("rainn", data.keys(), n=5)[0])