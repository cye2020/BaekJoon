from src.solution import solution1, solution2
import pytest

# solution에 대해 @pytest.mark.parametrize를 이용해 여러 개 지정해서 테스트 케이스를 생성
@pytest.mark.parametrize(
    "alphabet, expected",
    [
        ("ljes=njak", 6),
        ("ddz=z=", 3),
        ("nljj", 3),
        ("c=c=", 2),
        ("dz=ak", 3)
    ]
)
def test_solution(alphabet, expected):
    # assert를 이용해 solution의 결과와 expected가 같은지 확인
    assert solution1(alphabet) == expected
    assert solution2(alphabet) == expected