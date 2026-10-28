import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    # новый объект для каждого теста, чтобы тесты не зависели друг от друга
    return Calculator()


# ---------- add ----------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 0, 0),
        (1_000_000, 2_000_000, 3_000_000),
    ],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


def test_add_floats(calc):
    # 0.1 + 0.2 в двоичной системе не равно ровно 0.3, поэтому approx
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)


# ---------- subtract ----------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (3, 5, -2),
        (-5, -3, -2),
        (0, 7, -7),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


# ---------- multiply ----------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 5, 20),
        (-4, 5, -20),
        (-4, -5, 20),
        (7, 0, 0),
        (1.5, 2, 3.0),
    ],
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


# ---------- divide ----------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (7, 2, 3.5),
        (-9, 3, -3),
        (0, 5, 0),
        (1, 3, 0.3333333333),
    ],
)
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a", [1, -1, 0, 2.5])
def test_divide_by_zero(calc, a):
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно"):
        calc.divide(a, 0)


# ---------- is_prime_number ----------

@pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 97, 7919])
def test_is_prime_true(calc, n):
    assert calc.is_prime_number(n) is True


@pytest.mark.parametrize("n", [-7, 0, 1, 4, 9, 15, 25, 100])
def test_is_prime_false(calc, n):
    assert calc.is_prime_number(n) is False


@pytest.mark.parametrize("value", [2.5, "7", None, True])
def test_is_prime_wrong_type(calc, value):
    with pytest.raises(TypeError):
        calc.is_prime_number(value)


# ---------- average ----------

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([5], 5),
        ([1, 2, 3, 4], 2.5),
        ([-1, 1], 0),
        ([0.1, 0.2, 0.3], 0.2),
    ],
)
def test_average(calc, numbers, expected):
    assert calc.average(numbers) == pytest.approx(expected)


def test_average_empty_list(calc):
    with pytest.raises(ValueError, match="Список пуст"):
        calc.average([])
