from scripts.permutation import _permutation

DEFAULT_KEY = [
    0, 1, 1, 0, 0, 0, 1, 1,
    0, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 1, 0, 1, 0, 0, 1,
    0, 1, 1, 0, 1, 1, 0, 1,
    0, 1, 1, 0, 1, 0, 0, 1,
    0, 1, 1, 0, 1, 1, 1, 0,
    0, 1, 1, 0, 0, 0, 0, 1,
    0, 1, 1, 0, 1, 1, 0, 0
]

PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC_2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]


def divide_key(key: list) -> tuple:
    assert len(key) == 56
    return key[:28], key[28:]


def rotate(key: list, round: int):
    if round == 1 or round == 2 or round == 9 or round == 16:
        return _rotate_by(key, 1)
    else:
        return _rotate_by(key, 2)


def _rotate_by(key: list, by: int):
    # Left shift
    return key[by:] + key[:by]


def pc_2_permutation(key: list):
    """
    Create subkey k_i

    :param key:
    """
    return _permutation(key, PC_2, 56, 48)


def pc_1_permutation(key: list):
    return _permutation(key, PC_1, 64, 56)
