from src.solution1 import solution
import pytest

@pytest.mark.parametrize(
    "N, words, expected",
    [
        (3, ["happy", "new", "year"], 3),
        (4, ["aba", "abab", "abcabc", "a"], 1),
        (5, ["ab", "aa", "aca", "ba", "bb"], 4),
        (2, ["yzyzy", "zyzyz"], 0),
    ]
)
def test_solution(N, words, expected):
    assert solution(N, words) == expected