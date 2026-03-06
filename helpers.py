import string

def get_alphabet_data():
    """Generates test data of the following format: (letter, expected_result)"""
    vowels = 'euioa'
    data = [(v, True) for v in vowels] + [(c, False) for c in string.ascii_lowercase if c not in vowels]
    return data