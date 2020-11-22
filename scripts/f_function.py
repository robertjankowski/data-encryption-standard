from scripts.bits_utils import xor
from scripts.permutation import _permutation
from scripts.s_box import S_BOXES

E_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

P_TABLE = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]


def _chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def num_to_bits(num: int) -> list:
    out = [1 if num & (1 << (7 - n)) else 0 for n in range(8)]
    return out


def bits_to_num(bits: list) -> int:
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out


def expansion_function(bits: list):
    return _permutation(bits, E_TABLE, 32, 48)


def f_function(bits: list, key: list):
    assert len(key) == 48
    bits = expansion_function(bits)
    result = xor(bits, key)
    assert len(result) == 48
    output = []
    for idx, part in enumerate(_chunks(result, 6)):
        s_box = S_BOXES[idx]
        row_select = bits_to_num([part[0], part[-1]])
        col_select = bits_to_num(part[1:-1])
        value = num_to_bits(s_box[row_select][col_select])[4:]
        output.extend(value)
    output = permutation(output)
    return output


def permutation(bits: list):
    return _permutation(bits, P_TABLE, 32, 32)
