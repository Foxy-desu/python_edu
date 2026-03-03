import pytest
from functions import check_tweet_limit_excess

@pytest.mark.parametrize("length_offset, expected",[
    (-1, False),
    (0, False),
    (1, True),
])
def test_check_tweet_upper_limit_boundaries(length_offset, expected):
    """Проверка граничных значений c передаваемым верхим лимитом 30"""
    limit = 30
    tweet = 'a' * (limit + length_offset)
    result = check_tweet_limit_excess(tweet, limit)
    assert result is expected, f"Failed with tweet_length = {len(tweet)} and limit = {limit}"


@pytest.mark.parametrize("tweet_len, expected", [
    (279, False),
    (280, False),
    (281, True)
])
def test_check_tweet_upper_limit_boundaries_with_default(tweet_len, expected):
    """Проверка граничных значений с дефолтным верхним лимитом 280"""
    tweet = 'a' * tweet_len
    result = check_tweet_limit_excess(tweet)
    assert result is expected, f'Failed with tweet_len = {tweet_len}'


# TODO

# Лимит = 0,1
# Лимит = другие типы данных помимо int
# твит_стринг - пустой
# твит_стринг - не строка