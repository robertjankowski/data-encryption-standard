from scripts.bits_utils import xor
from scripts.f_function import f_function
from scripts.key import DEFAULT_KEY, divide_key, rotate, pc_2_permutation
from scripts.permutation import final_permutation, initial_permutation
from scripts.text_utils import divide_into_chunks, text_to_bits, divide_message, bits_to_text


def encrypt(message: str, key: list = DEFAULT_KEY):
    msgs = divide_into_chunks(message)
    msgs_bits = [text_to_bits(m) for m in msgs]
    total_output = []

    for m in msgs_bits:
        # 1. Initial permutation
        m = initial_permutation(m)
        L, R = divide_message(m)

        # 2. Prepare key
        c, d = divide_key(key)

        # 3. Transform for 16 rounds
        for r in range(1, 17):
            # 3a) rotate keys and do permutation (depends on round)
            c = rotate(c, r)
            d = rotate(d, r)
            k_i = pc_2_permutation(c + d)

            # 3b) run f-Function
            tmp = f_function(R, k_i)

            # 3c) switch sides
            L = R
            R = xor(L, tmp)

        # Final Permutation
        output = L + R
        output = final_permutation(output)
        total_output.append(output)

    return total_output


def decrypt(key: list = DEFAULT_KEY) -> str:
    # TODO
    pass


if __name__ == '__main__':
    cipher = encrypt("All day is raining")
    [print(m) for m in cipher]
    [print(bits_to_text(m)) for m in cipher]
