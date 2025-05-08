import pytest
from src.solution1 import solution

# input.txt를 parameter로 받고 result는 1로 parameterize화
@pytest.mark.parametrize("test_input, result", [
    ("input1.txt", [3, 7, 8, 9]),
])
def test_game(test_input, result):
    # test_input 파일을 열어서 N, K, values에 할당
    with open(test_input, 'r') as file:
        input = file.readline
        N = int(input())
        matrix = [list(map(int, list(input().strip()))) for _ in range(N)]
        
    answer = solution(N, matrix)
    assert answer == result