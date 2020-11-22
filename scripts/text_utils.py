def text_to_bits(data: str) -> list:
    """
    Convert string into bits array

    :param s:
    :return:
    """
    l = len(data) * 8
    result = [0] * l
    pos = 0
    for ch in data:
        i = 7
        while i >= 0:
            if ch & (1 << i) != 0:
                result[pos] = 1
            else:
                result[pos] = 0
            pos += 1
            i -= 1

    return result


def bits_to_text(data: list) -> str:
    """
    Convert list of bits into string

    :param bits:
    :return:
    """
    assert len(data) % 8 == 0
    result = []
    pos = 0
    c = 0
    while pos < len(data):
        c += data[pos] << (7 - (pos % 8))
        if (pos % 8) == 7:
            result.append(c)
            c = 0
        pos += 1

    return bytes(result)


def divide_into_chunks(s: str, nbits=8) -> list:
    """
    Split input string into chunks. All with length 8 (64 bits)

    :param s: input string
    :param nbits:
    :return: list of equally divided strings
    """
    result = [s[i:(i + nbits)].ljust(nbits) for i in range(0, len(s), nbits)]
    return result


def divide_message(bits: list) -> tuple:
    assert len(bits) == 64
    return bits[:32], bits[32:]
