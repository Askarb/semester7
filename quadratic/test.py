from django.test import TestCase
from quadratic.core_quadratic import solve_quadratic


class TestQuadraticMethod(TestCase):
    def test_not_possible(self):
        result = solve_quadratic(5, 2, 1)
        self.assertEqual(result['status'], 0)

    def test_possible_1(self):
        result = solve_quadratic(1, -4, 4)
        self.assertEqual(result['status'], 1)
        self.assertEqual(result['x'], 2)

    def test_possible_2(self):
        result = solve_quadratic(5, 6, 1)
        self.assertEqual(result['status'], 2)
        self.assertEqual(result['x1'], -0.2)
        self.assertEqual(result['x2'], -1)

    def test_possible_2_1(self):
        result = solve_quadratic(1, 2, -8)
        self.assertEqual(result['status'], 2)
        self.assertEqual(result['x1'], 2)
        self.assertEqual(result['x2'], -4)

    def test_possible_2_3(self):
        result = solve_quadratic(1, -7, 0)
        self.assertEqual(result['status'], 2)
        self.assertEqual(result['x1'], 7)
        self.assertEqual(result['x2'], 0)

