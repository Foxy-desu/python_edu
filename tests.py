import pytest
from functions import check_tweet_limit_excess


class TestTweetLimit:
    """Checks for tweet_limit parameter and related functional logics"""

    @pytest.mark.parametrize("tweet_str, tweet_limit, expected", [
        # for custom limit of 33
        ('a' * 32, 33, False),
        ('a' * 33, 33, False),
        ('a' * 34, 33, True),
        # for lower limit of 0 and 1
        ('', 0, False),
        ('a', 0, True),
        ('', 1, False),
        ('a', 1, False),
        ('ab', 1, True)
    ])
    def test_tweet_limit_logic(self, tweet_str, tweet_limit, expected):
        """Check the upper non-default limit and the lower limit """
        assert check_tweet_limit_excess(tweet_str,
                                        tweet_limit) is expected, f'Failed: tweet_str={tweet_str}, tweet_limit={tweet_limit}'

    @pytest.mark.parametrize("tweet_str, expected", [
        ('a' * 279, False),
        ('a' * 280, False),
        ('a' * 281, True)
    ])
    def test_tweet_default_limit(self, tweet_str, expected):
        """Check the default limit is set and equals 280"""
        assert check_tweet_limit_excess(tweet_str) is expected, f'Failed: tweet_str={tweet_str}'

    @pytest.mark.xfail(reason="Validation of negative values isn't yet implemented")
    def test_tweet_limit_negative_val_fails(self):
        """Checks if the function fails with ValueError on negative tweet_limit value"""
        with pytest.raises(ValueError, match="Tweet limit cannot be negative"):
            check_tweet_limit_excess("some random tweet", -5)

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

    @pytest.mark.parametrize("tweet_str", [
        25000, 25.055, None, ["my tweet"], {"my tweet"}, ("my tweet",),
    ])
    @pytest.mark.xfail(reason="Validation of types is not implemented yet")
    def test_tweet_string_type_check(self, tweet_str):
        """Check type validation for tweet_str parameter"""
        with pytest.raises(TypeError, match="Tweet value type can only be string"):
            check_tweet_limit_excess(tweet_str)

    @pytest.mark.xfail(reason="Validation of missing arguments is not implemented yet")
    def test_tweet_string_is_missing(self):
        with pytest.raises(TypeError, match="Tweet value is required"):
            check_tweet_limit_excess()
# TODO

# твит_стринг - пустой
# твит_стринг - не строка
