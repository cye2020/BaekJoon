import pytest

from src.solution1 import solution

# class TestGame:

# input.txt를 parameter로 받고 result는 1로 parameterize화
@pytest.mark.parametrize("test_input, result", [
    ("input1.txt", 1),
    ("input2.txt", 5),
    ("input3.txt", 5),
    ("input4.txt", -1),
    ("input5.txt", 1),
    ("input6.txt", 7),
    ("input7.txt", -1)
])
def test_game(test_input, result):
    # test_input 파일을 열어서 N, M, marix에 할당
    with open(test_input, 'r') as file:
        N, M = map(int, file.readline().split())
        matrix = [list(map(str, file.readline().strip('\n'))) for _ in range(N)]

    answer = solution(N, M, matrix)
    assert answer == result
