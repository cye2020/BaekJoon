import io
import sys
import pytest
from src.solution1 import solution


def run_io_test(input_path: str, expected_path: str):
    # 파일에서 입력과 기대 출력 읽기
    with open(input_path, "r") as f:
        input_data = f.read()
    with open(expected_path, "r") as f:
        expected_output = f.read()

    # stdin/stdout 리디렉션
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()

    solution()  # 백준 제출용 main 실행

    output = sys.stdout.getvalue().strip()
    assert output == expected_output.strip()


@pytest.mark.parametrize("input_file, expected_file", [
    ("tests/inputs/input1.txt", "tests/expected/expected1.txt"),
    # ("tests/inputs/input2.txt", "tests/expected/expected2.txt"),  # 다른 케이스도 추가 가능
])
def test_solution(input_file, expected_file):
    run_io_test(input_file, expected_file)
