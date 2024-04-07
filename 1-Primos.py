import unittest

def is_primo(value):
    # valor % div -> resto
    if value % 2 != 0:
        return True
    else:
        return False
    


class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, True)
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)
 
 # Nuevos tests
 
    def test_7(self):
        result = is_primo(7)
        self.assertEqual(result, True)

    def test_8(self):
        result = is_primo(8)
        self.assertEqual(result, False)

    def test_9(self):
        result = is_primo(9)
        self.assertEqual(result, True)

    def test_10(self):
        result = is_primo(10)
        self.assertEqual(result, False)

    def test_11(self):
        result = is_primo(11)
        self.assertEqual(result, True)

    def test_12(self):
        result = is_primo(12)
        self.assertEqual(result, False)

    def test_13(self):
        result = is_primo(13)
        self.assertEqual(result, True)

    def test_14(self):
        result = is_primo(14)
        self.assertEqual(result, False)

    def test_15(self):
        result = is_primo(15)
        self.assertEqual(result, True)

    def test_16(self):
        result = is_primo(16)
        self.assertEqual(result, False)

    def test_17(self):
        result = is_primo(17)
        self.assertEqual(result, True)

    def test_18(self):
        result = is_primo(18)
        self.assertEqual(result, False)

    def test_19(self):
        result = is_primo(19)
        self.assertEqual(result, True)

    def test_20(self):
        result = is_primo(20)
        self.assertEqual(result, False)

unittest.main()
