import string
import pytest
from functions import check_tweet_limit_excess, print_tweet_limit_message, check_vowel
from helpers import get_alphabet_data

class TestTweetLimit:
    """Checks for tweet_limit parameter and related functional logics"""

    @pytest.mark.positive
    @pytest.mark.parametrize("tweet_str, tweet_limit, expected", [
        # for custom limit of 33
        ('a' * 32, 33, False), ('a' * 33, 33, False), ('a' * 34, 33, True),
        # for lower limit of 0 and 1
        ('', 0, False), ('a', 0, True), ('', 1, False), ('a', 1, False), ('ab', 1, True)
    ])
    def test_tweet_limit_logic(self, tweet_str, tweet_limit, expected):
        """Check the upper non-default limit and the lower limit """
        assert check_tweet_limit_excess(tweet_str,
                                        tweet_limit) is expected, f'Failed: tweet_str={tweet_str}, tweet_limit={tweet_limit}'

    @pytest.mark.positive
    @pytest.mark.parametrize("tweet_str, expected", [
        ('a' * 279, False), ('a' * 280, False), ('a' * 281, True)
    ])
    def test_tweet_default_limit(self, tweet_str, expected):
        """Check the default limit is set and equals 280"""
        assert check_tweet_limit_excess(tweet_str) is expected, f'Failed: tweet_str={tweet_str}'

    @pytest.mark.negative
    @pytest.mark.xfail(reason="Validation of negative values isn't yet implemented")
    def test_tweet_limit_negative_val_fails(self):
        """Checks if the function fails with ValueError on negative tweet_limit value"""
        with pytest.raises(ValueError, match="Tweet limit cannot be negative"):
            check_tweet_limit_excess("some random tweet", -5)

    @pytest.mark.negative
    @pytest.mark.parametrize("tweet_limit", [
        True, "10", None, [280], {280}, (280,), 210.5,
    ])
    @pytest.mark.xfail(reason="Validation of types is not implemented yet")
    def test_tweet_limit_type_check(self, tweet_limit):
        """Checks if the function accepts different types for tweet limit"""
        with pytest.raises(TypeError, match="Tweet limit value type can only be integer"):
            check_tweet_limit_excess("some tweet string", tweet_limit)


class TestTweetString:
    """Checks for tweet_string parameter and related functional logics"""

    @pytest.mark.negative
    @pytest.mark.parametrize("tweet_str", [
        25000, 25.055, None, ["my tweet"], {"my tweet"}, ("my tweet",),
    ])
    @pytest.mark.xfail(reason="Validation of types is not implemented yet")
    def test_tweet_string_type_check(self, tweet_str):
        """Check type validation for tweet_str parameter"""
        with pytest.raises(TypeError, match="Tweet value type can only be string"):
            check_tweet_limit_excess(tweet_str)

    @pytest.mark.negative
    @pytest.mark.xfail(reason="Validation of missing arguments is not implemented yet")
    def test_tweet_string_is_missing(self):
        with pytest.raises(TypeError, match="Tweet value is required"):
            check_tweet_limit_excess()


class TestTerminalOutput:
    """Checks for tweet limit message output"""

    @pytest.mark.positive
    @pytest.mark.parametrize("is_over_limit, expected_message", [
        (True, "Too many characters."), (False, "A fitting tweet.")
    ])
    def test_tweet_limit_message_output(self, is_over_limit, expected_message, capsys):
        """Checks if function prints the right message out into the terminal"""
        print_tweet_limit_message(is_over_limit)
        captured = capsys.readouterr()
        assert captured.out is expected_message


    @pytest.mark.negative
    def test_obligatory_parameter_is_missing_fails(self):
        with pytest.raises(TypeError):
            print_tweet_limit_message()

    @pytest.mark.negative
    def test_obligatory_parameter_is_missing_fails_with_right_err(self):
        with pytest.raises(TypeError, match="'True' or 'False' should be passed as the parameter"):
            print_tweet_limit_message()

    @pytest.mark.negative
    @pytest.mark.parametrize("is_over_limit",[
        'String', 1, 0.0, [1], {}, (0,), None,
    ])
    def test_wrong_type_params_fail(self, is_over_limit, capsys):
        """Checks if function handles falsy and truthy values as wrong type """
        with pytest.raises(TypeError):
            result = print_tweet_limit_message(is_over_limit)
            captured = capsys.readouterr()
            print(f"\nReturned: '{result}', printed: '{captured.out}' with passed parameter '{is_over_limit}'")


class TestLetters:

    @pytest.mark.positive
    @pytest.mark.parametrize("letter, expected", get_alphabet_data())
    @pytest.mark.xfail(reason="Function returns string instead of bool")
    def test_check_all_latin_letters(self, letter, expected):
        """Checks if the function returns True when the letter is a vowel or False when the letter is a consonant """
        assert check_vowel(letter) is expected


    @pytest.mark.negative
    @pytest.mark.parametrize("char", [
        'ж', 'а', 'с', 'ñ', 'ö', 'λ', '阿', '!','7',' ', '🦊'
    ])
    @pytest.mark.xfail(reason="Validation of the value is not yet implemented")
    def test_not_latin_letters_fails(self, char):
        """Checks if the function fails with a string containing elements not related to the latin alphabet"""
        with pytest.raises(ValueError, match="Only a latin letter can be passed."):
            result = check_vowel(char)
            print(result)


    @pytest.mark.negative
    @pytest.mark.parametrize("value", [
        True, 1, 5.5, None, {}, [], ("a","b"),
    ])
    def test_wrong_type_values_fails(self, value):
        """Checks if function fails with non-string values properly"""
        with pytest.raises(TypeError, match='Wrong value type. String containing a latin letter should be passed'):
            result = check_vowel(value)
            print(result)

    @pytest.mark.negative
    @pytest.mark.parametrize("value", [
        "", "ch"
    ])
    def test_input_value_length_fails(self, value):
        """Checks if function fails properly with strings of the wrong length """
        with pytest.raises(ValueError, match="Value must be exactly one character"):
            result = check_vowel(value)
            print(result)

