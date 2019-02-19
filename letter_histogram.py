def char_frequency(str1):

    user_input = input('Please enter a word: ')
    user_dictionary = {}
    for i in user_input:
        keys = user_dictionary.keys()
        if i in keys:
            user_dictionary[i] += 1
        else:
            user_dictionary[i] = 1
    return user_dictionary

print (char_frequency('google.com'))