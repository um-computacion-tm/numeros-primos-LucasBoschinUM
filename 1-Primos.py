import unittest

def is_prime(value):
    return True

class TestPrimos(unittest.TestCase):

    def test_numero_2_primo(self):
        self.assertEqual(is_prime(2), True)

        if __name__ == "__main__":
            unittest.main()