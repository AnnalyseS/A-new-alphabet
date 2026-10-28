#inputs: the latin alphabet
#outputs: the new alphabet as listed per the site
#edge cases: a paragraph
#numbers and punctuation -- not accounted for, print as is.
#what is the problem asking? It wants us to convert a string written in the latin alphabet to a string word in the new alphabet
#MAKE A MINI COMPILER!

def main():
    #we want to get input from the user and make it match something to output the quivalent of that something
    user_input = input().strip().lower()

    #we should probably find a way to convert that input
    convert(user_input)
    
    

def convert(input):
    #dict containing ASCII alphabet and new alphabet
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

    #loop employed to iterate through the dict

    total = ""
    for char in input:
        if char in New_alphabet:
            new_char = New_alphabet[char]
        else:
            new_char = char
        total = total + new_char # need to concatenate strings together so that it creates a whole word, need to do it as loop happens
    print(total)

main()