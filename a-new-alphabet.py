#inputs: the latin alphabet
#outputs: the new alphabet as listed per the site
#edge cases: a paragraph
#numbers -- not accounted for.
# what is the problem asking? It wants us to convert a string written in the latin alphabet to a string word in the new alphabet

def main():
    #we want to get input from the user and make it match something to output the quivalent of that something
    user_input = input().strip().lower() # I employed a few string methods instead of doing a match/ case because this was a shortcut to getting the input to match the datastructure we will create
    #we should probably find a way to convert that input
    convert(user_input)
    
    

def convert(input):
    #I will make here my own function that I can use to convert the input and return a value that is desired
    #We could do an if, elif else chain that keeps extending and iterate through it in a while loop, but this would be inefficient so I believe a dict would be better

    New_alphabet = {
        "a": "@",
        "b": "8",
        "c": "(",
        "d": "|)",
        "e": "3",
        "f": "#",
        "g": "6",
        "h": "[-]",
        "i": "|",
        "j": "_|",
        "k": "|<",
        "l": "1",
        "m": "[]\/[]",
        "n": "[]\[]",
        "o": "0",
        "p": "|D",
        "q": "(,)",
        "r": "|Z",
        "s": "$",
        "t": "']['",
        "u": "|_|",
        "v": "\/",
        "w": "\/\/",
        "x": "}{",
        "y": "`/",
        "z": "2"
    }
    # how would we now go about finding a letter in our data structure?
    # we could do an if, elif chain but again that would be inefficient, better to use something that iterates naturally, a loop. For loop will be better than a while loop here
    
    total = ""
    for char in input:
        if char in New_alphabet:
            # print(New_alphabet[char]) -- here i priinted each letter but since the letter is in the loop it doesnt print together as a concatenated string and prints on its own line
            new_char = New_alphabet[char]
        else:
            new_char = char
        total = total + new_char # need to concatenate strings together so that it creates a whole word, need to do it as loop happens
    print(total)

main()