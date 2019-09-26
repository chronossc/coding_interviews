import pytest
from numbers_sum.code import pairs

@pytest.mark.parametrize(
    "result, expected_pairs", [
        pytest.param(4, {(1, 3), (3, 1), (0, 4), (2, 2), (4, 0)}, id="4"),
        pytest.param(32, {(16, 16), (24, 8), (28, 4), (7, 25), (26, 6), (17, 15), (31, 1), (0, 32), (8, 24), (12, 20), (20, 12), (2, 30), (14, 18), (27, 5), (29, 3), (10, 22), (22, 10), (4, 28), (25, 7), (3, 29), (11, 21), (19, 13), (13, 19), (21, 11), (6, 26), (15, 17), (1, 31), (32, 0), (18, 14), (30, 2), (9, 23), (23, 9), (5, 27)}, id="32"),
        pytest.param(10, {(6, 4), (7, 3), (4, 6), (5, 5), (8, 2), (9, 1), (2, 8), (1, 9), (0, 10), (10, 0), (3, 7)}, id="10")
    ]
)
def test_pairs(result, expected_pairs):
    result_pairs = pairs(
        list(range(100)),
        result
    )
    assert result_pairs == expected_pairs