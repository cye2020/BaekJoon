import pytest
from src.solution1 import solution

# class TestGame:

# input.txt를 parameter로 받고 result는 1로 parameterize화
@pytest.mark.parametrize("test_input, result", [
    ("input1.txt", 6),
    ("input2.txt", 12),
])
def test_game(test_input, result):
    # test_input 파일을 열어서 N, K, values에 할당
    with open(test_input, 'r') as file:
        input = file.readline
        N, K = map(int, input().split())
        values = [int(input()) for _ in range(N)]
        
    answer = solution(K, values)
    assert answer == result