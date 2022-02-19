import functools
import unittest

from main import QuadraticEquation


def cases(cases_items):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args):
            for c in cases_items:
                new_args = args + (c if isinstance(c, tuple) else (c,))
                f(*new_args)

        return wrapper

    return decorator


class TestSuite(unittest.TestCase):
    @cases([
        [1, 0, 1],
    ])
    def test_return_is_empty(self, data):
        self.assertEqual(
            QuadraticEquation(*data).solve(), []
        )

    @cases([
        [1, 2, 1],
        [1, 0, 0.0000000001],
    ])
    def test_return_one(self, data):
        self.assertEqual(
            len(QuadraticEquation(*data).solve()), 1
        )

    def test_return_two(self):
        self.assertEqual(
            QuadraticEquation(1, 0, -1).solve(), [-1.0, 1.0]
        )

    @cases([
        [0, 0, 1],
        [0.00000001, 1, 1],
    ])
    def test_a_not_zero(self, data):
        self.assertRaises(
            ValueError,
            QuadraticEquation(*data).solve
        )

    def test_is_value_error(self):
        self.assertRaises(
            ValueError,
            QuadraticEquation('sdfsdf', 0, 1).solve
        )

    @cases([
        [0.00000001, ['1'], 1],
        [0.00000001, (1, 5), 1],
    ])
    def test_is_type_error(self, data):
        self.assertRaises(
            TypeError,
            QuadraticEquation(*data).solve
        )


if __name__ == "__main__":
    unittest.main()
