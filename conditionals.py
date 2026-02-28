# tweet_limit = 280
# tweet_string = 'a' * 281
# if (diff := tweet_limit - len(tweet_string)) >= 0:
#     print('A fitting tweet')
# else:
#     print(f'Too many ({abs(diff)}) letters. ')

##########################################################
##########################################################

# vowels = ('e', 'u', 'o', 'a', 'i')
# letter = input('Enter a latin letter: ')
# if letter in vowels:
#     print(f'"{letter}" is a vowel!')
# else:
#     print(f'"{letter}" is not a vowel')

###########################################################
###########################################################
# import random
#
# secret = random.randint(1, 10)
# guess = int(input('Enter a number from 1 to 10: '))
# while guess != secret:
#     if guess < secret:
#         print('Too low. Try again.')
#         guess = int(input('Enter a number from 1 to 10: '))
#     elif guess > secret:
#         print('Too high. Try again.')
#         guess = int(input('Enter a number from 1 to 10: '))
# print(f'Just right! The numbr is {secret}.')


#############################################################
#############################################################

# elements_set = [{'вишня': {'small': True, 'green': False}}, {'горошек': {'small': True, 'green': True}},
#                 {'арбуз': {'small': False, 'green': True}}, {'тыква': {'small': False, 'green': False}}]
#
#
# def get_bool_from_str(str):
#     bools = {'true': True, 'false': False}
#     normalized_str = str.lower().strip()
#     return bools[normalized_str]
#
#
# small = get_bool_from_str(input('Is the item small (true/false)?: '))
# green = get_bool_from_str(input('Is the item green (true/false)?: '))
# right_elems = []
#
# for elem in elements_set:
#     for key, value in elem.items():
#         if value['small'] == small and value['green'] == green:
#             right_elems.append(key)
#
# print(f'These are the suitable fruits: {", ".join(right_elems)}')

###############################################################################
###############################################################################
