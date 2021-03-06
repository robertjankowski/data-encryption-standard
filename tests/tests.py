import unittest

from scripts.bits_utils import xor
from scripts.f_function import expansion_function, num_to_bits, bits_to_num
from scripts.key import DEFAULT_KEY, rotate, divide_key
from scripts.text_utils import bits_to_text, text_to_bits, divide_into_chunks
from scripts.permutation import initial_permutation, final_permutation


class TestTextUtils(unittest.TestCase):
    def test_bits(self):
        text = 'This is an example'
        bits = text_to_bits(text)
        self.assertEqual(text, bits_to_text(bits).decode('ascii'))

    def test_divide(self):
        text = 'This is an example'
        splitted = divide_into_chunks(text)
        self.assertEqual(len(splitted), 3)


class TestPermutation(unittest.TestCase):
    def test_initial_permutation(self):
        text = 'Exampl'
        text = divide_into_chunks(text)[0]
        bits = text_to_bits(text)
        bits_after = initial_permutation(bits)
        self.assertEqual(bits[58 - 1], bits_after[0])
        self.assertEqual(bits[26 - 1], bits_after[4])

    def test_final_permutation(self):
        text = 'Exampl'
        text = divide_into_chunks(text)[0]
        bits = text_to_bits(text)
        bits_after = final_permutation(bits)
        self.assertEqual(bits[40 - 1], bits_after[0])
        self.assertEqual(bits[7 - 1], bits_after[9])


class TestfFunction(unittest.TestCase):
    def test_expansion_function(self):
        text = 'Exampl'
        text = divide_into_chunks(text)[0]
        bits = text_to_bits(text)[:32]
        bits_after = expansion_function(bits)
        self.assertEqual(bits[32 - 1], bits_after[0])
        self.assertEqual(bits[5 - 1], bits_after[5])
        self.assertEqual(bits[5 - 1], bits_after[7])

    def test_convert_num_to_bits(self):
        num = 4
        a = num_to_bits(num)
        self.assertEqual(a, [0, 0, 0, 0, 0, 1, 0, 0])
        num = 15
        a = num_to_bits(num)
        self.assertEqual(a, [0, 0, 0, 0, 1, 1, 1, 1])

    def test_convert_bits_to_num(self):
        bits = [0, 0, 0, 0, 0, 1, 0, 0]
        a = bits_to_num(bits)
        self.assertEqual(a, 4)
        bits = [0, 0, 0, 0, 1, 1, 1, 1]
        a = bits_to_num(bits)
        self.assertEqual(a, 15)


class TestKey(unittest.TestCase):
    def test_rotate(self):
        k = DEFAULT_KEY
        k_rotated = rotate(k, 1)
        self.assertEqual(k_rotated[0], k[-1])
        k_rotated = rotate(k, 2)
        self.assertEqual(k_rotated[0], k[-2])

    def test_divide(self):
        k = DEFAULT_KEY
        k = k[:56]
        c, d = divide_key(k)
        self.assertEqual(len(c), 28)
        self.assertEqual(len(d), 28)


class TestBitsUtils(unittest.TestCase):
    def test_xor(self):
        bits_A = [1, 0, 1, 0]
        bits_B = [0, 0, 1, 1]
        bits = xor(bits_A, bits_B)
        self.assertEqual(bits, [1, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
