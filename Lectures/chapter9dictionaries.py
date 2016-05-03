#create a list of dictionary to store word count

import string

def add_word(single_word, word_dict):
    if single_word not in word_dict:
        word_dict[single_word] = 1
    else:
        word_dict[single_word] += 1

def process_line(line_data, word_dict):
    word_list = line_data.split()
    for word in word_list:
        word = word.strip(string.punctuation)
        add_word(word,word_dict)

word_dict= {}
line_data = "John is single, Jenny is married, Jane is single"
process_line(line_data, word_dict)
print(word_dict)

sort_keys = sorted(word_dict, key = word_dict.__getitem__, reverse = True)
print(sort_keys)


# word1 = "John"
# word2 = "Jane"
# word3 = "John"
#
# word_dict = {} #define a new dictionary
#
# print("Before adding " + str(word_dict))
# add_word(word1, word_dict)
# add_word(word2, word_dict)
# add_word(word3, word_dict)
# print("After adding " + str(word_dict))  #need to convert to str