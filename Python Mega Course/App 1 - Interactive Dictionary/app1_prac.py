import json
from difflib import get_close_matches

dictionary = json.load(open("data.json", 'r'))

def define(word):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    elif word.title() in dictionary:
        return dictionary[word.title()]
    elif word.upper() in dictionary:
        return dictionary[word.upper()]
    elif get_close_matches(word, dictionary.keys()):
        first_match = get_close_matches(word, dictionary.keys())[0]
        while True:
            answ = input("Did you mean %s? Enter Y if yes, or N if no. " % first_match)
            if answ == "Y" or answ == "y":
                return dictionary[first_match]
            elif answ == "N" or answ == "n":
                return ("%s is not a word, please try again" % word)
            else:
                print("Not a valid answer, please enter a valid answer")
    else:
        return "That word does not exist. Please try again."

word = input("Enter a word to define: ")

output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else: print (output)
