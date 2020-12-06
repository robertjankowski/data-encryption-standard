from scripts.bits_utils import xor
from scripts.f_function import f_function
from scripts.key import DEFAULT_KEY, divide_key, rotate, pc_2_permutation, pc_1_permutation
from scripts.permutation import final_permutation, initial_permutation
from scripts.text_utils import divide_into_chunks, text_to_bits, divide_message, bits_to_text


class DES:
    def __init__(self, key: list = DEFAULT_KEY):
        self.key = key
        self.subkeys = self._prepare_keys(key)

    def _prepare_keys(self, key) -> list:
        subkeys = []
        key = pc_1_permutation(key)
        c, d = divide_key(key)
        for r in range(1, 17):
            c = rotate(c, r)
            d = rotate(d, r)
            k_i = pc_2_permutation(c + d)
            subkeys.append(k_i)
        return subkeys

    def encrypt(self, message: str) -> list:
        msgs = divide_into_chunks(message)
        msgs_bits = [text_to_bits(m) for m in msgs]
        total_output = []

        for m in msgs_bits:
            m = initial_permutation(m)
            L, R = divide_message(m)

            for r in range(1, 17):
                k_i = self.subkeys[r - 1]
                old_L = L
                L = R
                R = xor(old_L, f_function(R, k_i))

            output = R + L
            output = final_permutation(output)
            total_output.append(output)

        return total_output

    def decrypt(self, bits: list) -> bytes:
        bits = initial_permutation(bits)
        L, R = divide_message(bits)
        for r in range(1, 17):
            k_i = self.subkeys[16 - r]
            old_L = L
            L = R
            R = xor(old_L, f_function(R, k_i))

        output = R + L
        output = final_permutation(output)
        return bits_to_text(output)


if __name__ == '__main__':
    d = DES()
    data = "Testing DES algorithm"
    print('Input: {}'.format(data))
    cipher = d.encrypt(data)
    print('Encrypted:')
    for c in cipher:
        print(bits_to_text(c).hex(), c)
    decryption = ''.join([d.decrypt(c).decode('ascii') for c in cipher])
    print('Decrypted: {}'.format(decryption))
