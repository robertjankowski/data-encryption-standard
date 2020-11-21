from scripts.key import DEFAULT_KEY, divide_key, rotate, pc_2_permutation
from scripts.text_utils import divide_into_chunks, text_to_bits


def encrypt(message: str, key: list = DEFAULT_KEY):
    msgs = divide_into_chunks(message)
    msgs_bits = [text_to_bits(m) for m in msgs]
    c, d = divide_key(key)

    for r in range(1, 17):
        c = rotate(c, r)
        d = rotate(d, r)
        k_i = pc_2_permutation(c + d)
        # TODO: implement message part


def decrypt(key: list = DEFAULT_KEY) -> str:
    # TODO
    pass


if __name__ == '__main__':
    encrypt("Tob")
