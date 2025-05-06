import pytest
from src.solution1 import solution

# class TestGame:

# input.txt를 parameter로 받고 result는 1로 parameterize화
@pytest.mark.parametrize("test_input, result", [
    ("input1.txt", 21),
    ("input2.txt", 497),
])
def test_game(test_input, result):
    # test_input 파일을 열어서 N, K, values에 할당
    with open(test_input, 'r') as file:
        input = file.readline
        N, M = map(int, input().split())
        cards = list(map(int, input().split()))
        
    answer = solution(M, cards)
    assert answer == result