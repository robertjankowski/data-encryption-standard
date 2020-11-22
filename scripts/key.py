from scripts.permutation import _permutation

DEFAULT_KEY = [
    0, 1, 1, 0, 0, 0, 1, 1,
    0, 1, 1, 0, 1, 1, 1, 1,
    0, 1, 1, 0, 1, 1, 0, 1,
    0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 0, 0,
    0, 1, 1, 0, 0, 1, 0, 1,
    0, 1, 1, 1, 1, 0, 0, 0
]

PC2_TABLE = [
    17, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
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
    return key[-by:] + key[:-by]


def pc_2_permutation(key: list):
    """
    Create subkey k_i

    :param key:
    """
    return _permutation(key, PC2_TABLE, 56, 48)
