import io
import sys
import pytest
from src.solution import Solution


solutions = [
    getattr(Solution, name)
    for name in sorted(dir(Solution))
    if name.startswith("solution")
]


def run_io_test(func, input_path: str, expected_path: str):
    with open(input_path, "r") as f:
        input_data = f.read()
    with open(expected_path, "r") as f:
        expected_output = f.read()

    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()

    func()

    output = sys.stdout.getvalue().strip()
    assert output == expected_output.strip()


@pytest.mark.parametrize("func", solutions, ids=[s.__name__ for s in solutions])
@pytest.mark.parametrize("input_file, expected_file", [
    ("tests/inputs/input1.txt", "tests/expected/expected1.txt"),
    # ("tests/inputs/input2.txt", "tests/expected/expected2.txt"),
])
def test_solution(func, input_file, expected_file):
    run_io_test(func, input_file, expected_file)
