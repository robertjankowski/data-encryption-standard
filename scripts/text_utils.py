def text_to_bits(s: str) -> list:
    """
    Convert string into bits array

    :param s:
    :return:
    """
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def bits_to_text(bits: list) -> str:
    """
    Convert list of bits into string

    :param bits:
    :return:
    """
    assert len(bits) % 8 == 0
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def divide_into_chunks(s: str, nbits=8) -> list:
    """
    Split input string into chunks. All with length 8 (64 bits)

    :param s: input string
    :param nbits:
    :return: list of equally divided strings
    """
    result = [s[i:(i + nbits)].ljust(nbits) for i in range(0, len(s), nbits)]
    return result
