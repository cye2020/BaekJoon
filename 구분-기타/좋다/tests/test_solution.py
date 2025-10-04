import io
import sys
import pytest
from src.solution import solution1, solution2


def run_io_test(func, input_path: str, expected_path: str):
    # 파일에서 입력과 기대 출력 읽기
    with open(input_path, "r") as f:
        input_data = f.read()
    with open(expected_path, "r") as f:
        expected_output = f.read()

    # stdin/stdout 리디렉션
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()

    func()  # 각각 solution1, solution2 실행

    output = sys.stdout.getvalue().strip()
    assert output == expected_output.strip()


@pytest.mark.parametrize("func", [solution1, solution2])
@pytest.mark.parametrize("input_file, expected_file", [
    ("tests/inputs/input1.txt", "tests/expected/expected1.txt"),
    # ("tests/inputs/input2.txt", "tests/expected/expected2.txt"),
])
def test_solution(func, input_file, expected_file):
    run_io_test(func, input_file, expected_file)
