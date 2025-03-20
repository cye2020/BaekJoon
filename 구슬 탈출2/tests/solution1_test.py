import pytest

from src.solution1 import Game

# class TestGame:

# input.txt를 parameter로 받고 result는 1로 parameterize화
@pytest.mark.parametrize("test_input, result", [
    ("input.txt", 1),
])
def test_game(test_input, result):
    # test_input 파일을 열어서 N, M, marix에 할당
    with open(test_input, 'r') as file:
        N, M = map(int, file.readline().split())
        matrix = [list(map(str, file.readline().strip('\n'))) for _ in range(N)]

    game = Game(N, M, matrix)
    game.game_set()
    print(game.R, game.B, game.O)
