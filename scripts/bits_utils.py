def xor(bits_A: list, bits_B: list):
    assert len(bits_A) == len(bits_B)
    bits = []
    for a, b in zip(bits_A, bits_B):
        bits.append(a ^ b)
    return bits
