from calc import add, sub


def test_add():
    assert add(3, 5) == 8
    assert add(23, 438) == 461


def test_sub():
    assert sub(43, 21) == 22
