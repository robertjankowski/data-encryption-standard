def xor(bits_A: list, bits_B: list):
    assert len(bits_A) == len(bits_B)
    return [a ^ b for a, b in zip(bits_A, bits_B)]
