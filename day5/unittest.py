import unittest, pytest


def apply_discount(price, percent):
    return price - (price * (percent / 100))


class Test(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(apply_discount(1000, 20), 800)
        self.assertEqual(apply_discount(2500, 15), 2125)


# Test().test_discount() gives no output
if __name__ == "__main__":
    unittest.main()
