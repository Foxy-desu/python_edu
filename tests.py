import pytest
from functions import check_tweet_limit_excess

@pytest.mark.parametrize("tweet_str, tweet_limit, expected", [
    #for custom limit of 33
    ('a' * 32, 33, False),
    ('a' * 33, 33, False),
    ('a' * 34, 33, True),
    #for lower limit of 0 and 1
    ('', 0, False),
    ('a', 0, True),
    ('', 1, False),
    ('a', 1, False),
    ('ab', 1, True)
])
def test_tweet_limit_logic(tweet_str, tweet_limit, expected):
    """Check the upper non-default limit and the lower limit """
    assert check_tweet_limit_excess(tweet_str, tweet_limit) is expected, f'Failed: tweet_str={tweet_str}, tweet_limit={tweet_limit}'

@pytest.mark.parametrize("tweet_str, expected", [
    ('a' * 279, False),
    ('a' * 280, False),
    ('a' * 281, True)
])
def test_tweet_default_limit(tweet_str, expected):
    """Check the default limit is set and equals 280"""
    assert check_tweet_limit_excess(tweet_str) is expected, f'Failed: tweet_str={tweet_str}'
# TODO

# Лимит = 0,1
# Лимит = другие типы данных помимо int
# твит_стринг - пустой
# твит_стринг - не строка