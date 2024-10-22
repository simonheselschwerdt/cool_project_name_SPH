import pytest
from cool_project_name_SPH import add_one, mul


@pytest.mark.parametrize("x, y", [(1, 2), (2, 3), (3, 4)])
def test_add_one(x, y):
    print(f"Testing add_one with x={x}, expecting y={y}")
    assert y == add_one(x)

@pytest.mark.parametrize("x_1, x_2, y", [(1, 2, 2), (2, 2, 4), (3, 4, 12)])
def test_mul(x_1, x_2, y):
    print(f"Testing mul with x_1={x_1}, x_1={x_1}, expecting y={y}")
    assert y == mul(x_1, x_2)
