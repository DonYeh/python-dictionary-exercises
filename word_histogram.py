user_dictionary = {}


def word_frequency(str1):

    sentence_to_list = user_input.split()

    for word in sentence_to_list:
        keys = user_dictionary.keys()
        if word in keys:
            user_dictionary[word] += 1
        else:
            user_dictionary[word] = 1
    return user_dictionary


user_input = input('Please enter a sentence: ')

print(word_frequency(user_input))

print("The top three words are: ")
print(sorted(user_dictionary.values()))

