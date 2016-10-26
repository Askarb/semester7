from django.test import TestCase
from fibonacci.core_fibonacci import fibonacci


class TestQuadraticMethod(TestCase):
    def test_possible_enter_1(self):
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_possible_enter_2(self):
        result = fibonacci(2)
        self.assertEqual(result, 1)

    def test_possible_enter_3(self):
        result = fibonacci(3)
        self.assertEqual(result, 2)

    def test_possible_enter_4(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)

    def test_possible_enter_5(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)

    def test_possible_enter_6(self):
        result = fibonacci(6)
        self.assertEqual(result, 8)

    def test_possible_enter_7(self):
        result = fibonacci(7)
        self.assertEqual(result, 13)

    def test_possible_enter_8(self):
        result = fibonacci(8)
        self.assertEqual(result, 21)

    def test_possible_enter_9(self):
        result = fibonacci(9)
        self.assertEqual(result, 34)

    def test_possible_enter_10(self):
        result = fibonacci(10)
        self.assertEqual(result, 55)

    def test_possible_enter_100(self):
        result = fibonacci(100)
        self.assertEqual(result, 354224848179261915075)

    def test_possible_enter_1000(self):
        result = fibonacci(1000)
        self.assertEqual(result, 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)



# 1 = 1
# 2 = 1
# 3 = 2
# 4 = 3
# 5 = 5
# 6 = 8
# 7 = 13
# 8 = 21
# 9 = 34
# 10 = 55
