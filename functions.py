import random


def check_tweet_limit(tweet_str, tweet_limit=280):
    if (diff := tweet_limit - len(tweet_str)) >= 0:
        return 'A fitting tweet'
    else:
        return f'Too many ({abs(diff)}) letters. '

##############################################################################
##############################################################################

def check_vowel(letter):
    vowels = ('e', 'u', 'o', 'a', 'i')
    if letter in vowels:
        return 'It is a vowel!'
    else:
        return 'It is not a vowel!'

##############################################################################
##############################################################################

def get_number_from_user(start_num, end_num):
    return int(input(f'Please, enter a number from {start_num} to {end_num}: '))


def generate_random_num(start, end):
    return random.randint(start, end)


def check_guess(secret_num, guess_num):
    if guess_num < secret_num:
        return f'Too low! The number is {secret_num}'
    elif guess_num > secret_num:
        return f'Too high! The number is {secret_num}'
    else:
        return f'Just right! The number is {secret_num}'


def guess_number(start_num, end_num):
    secret = generate_random_num(start_num, end_num)
    guess = get_number_from_user(start_num, end_num)
    print(check_guess(secret, guess))

##############################################################################
##############################################################################

def get_matching_elems_from_list(is_small, is_green, elements_list):
    matching_elems = []
    for elem in elements_list:
        for key, value in elem.items():
            if value['small'] == is_small and value['green'] == is_green:
                matching_elems.append(key)
    return matching_elems


def get_bool_from_str(str):
    bools = {'true': True, 'false': False, 'yes': True, 'no': False}
    normalized_str = str.lower().strip()
    return bools[normalized_str]


def print_fruits():
    fruits_list = [{'вишня': {'small': True, 'green': False}}, {'горошек': {'small': True, 'green': True}},
                   {'арбуз': {'small': False, 'green': True}}, {'тыква': {'small': False, 'green': False}}]
    is_small = get_bool_from_str(input('Is the item small (true/false)?: '))
    is_green = get_bool_from_str(input('Is the item green (true/false)?: '))
    matching_fruits = get_matching_elems_from_list(is_small, is_green, fruits_list)
    print(f'These are the suitable fruits: {", ".join(matching_fruits)}')
