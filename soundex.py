#Name: Dakota Long
#Date: 02/19/2018
#soundex.py

import nltk
import sys

# Define any global helper strings at this point
remove_chars_vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']
remove_chars = ['h', 'w']
remove_empty = ['']

# Define tuple list and mapping code to create dictionary for consonant
# transformations at this point
transform_dict = {'b':1, 'f':1, 'p':1, 'v':1, 'c':2, 'g':2, 'j':2, 'k':2, 'q':2, 's':2, 'x':2, 'z':2,
                  'd':3, 't':3, 'l':4, 'm':5, 'n':5, 'r':6}

# function that takes token, transforms it into its new form, and returns it

def wordmap(token):
    converted_token = []
    # Save first letter
    first_letter = token[0]
    #Remove all occurances of 'h' and 'w' except for first letter.
    token_reduced = ''.join([character for character in token if character not in remove_chars])
    if first_letter in remove_chars:
        token_reduced = first_letter + token_reduced

    #Replace all consonants with digits.
    for char in token:
        if char in transform_dict:
            temp = transform_dict[char]
            converted_token.append(temp)
        else:
            converted_token.append(char)

    #Remove all occurances of a, e, i, o, u, y except first letter.
    for i in range(1, len(converted_token)):
        if converted_token[i] in remove_chars_vowels:
            converted_token[i] = ''

    #Removes the delete character placeholders ''.
    converted_token = [x for x in converted_token if x != '']

    #Replace all adjacent digits with one digit.
    if len(converted_token) > 4:
        for i in range(0, len(converted_token)-2):
            if converted_token[i] == converted_token[i+1]:
                del converted_token[i]

    #Replace first digit with letter.
    if isinstance(converted_token[0], int):
        converted_token[0] = first_letter

    #Append 0's if length < 4 and remove digits if length > 4.
    if len(converted_token) < 4:
        for i in range(len(converted_token), 4):
            converted_token.append(0)
    elif len(converted_token) > 4:
        for i in range(4, len(converted_token)):
            del converted_token[i]

    #Final answer as a string.
    answer = ''.join(str(i) for i in converted_token)

    #Return final soundex.
    return (answer.upper())

# Driver code for the program
# sys.argv[1] should be the name of the input file
# sys.argv[0] will be the name of this file

for line in open(sys.argv[1]).readlines():
    text = nltk.word_tokenize(line.lower())
    for token in text:
        print(token + ': \t' + wordmap(token))
    print ()  # This prints new line at the end of processing a line