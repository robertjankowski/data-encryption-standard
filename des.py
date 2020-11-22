from scripts.bits_utils import xor
from scripts.f_function import f_function
from scripts.key import DEFAULT_KEY, divide_key, rotate, pc_2_permutation, pc_1_permutation
from scripts.permutation import final_permutation, initial_permutation
from scripts.text_utils import divide_into_chunks, text_to_bits, divide_message, bits_to_text


class DES:
    def __init__(self, key: list = DEFAULT_KEY):
        self.key = key
        self.subkeys = self._prepare_keys()

    def _prepare_keys(self) -> list:
        subkeys = []
        key = pc_1_permutation(self.key)
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
                tmp = f_function(R, self.subkeys[r - 1])
                L = R
                R = xor(L, tmp)

            output = L + R
            output = final_permutation(output)
            total_output.append(output)

        return total_output

    def decrypt(self, bits: list) -> str:
        bits = initial_permutation(bits)
        L, R = divide_message(bits)
        for r in range(1, 17):
            k_i = self.subkeys[15 - r]
            tmp = f_function(R, k_i)
            L = R
            R = xor(L, tmp)

        output = L + R
        output = final_permutation(output)
        print('Decryption: ', output)
        return bits_to_text(output)


if __name__ == '__main__':
    # TODO: https://github.com/twhiteman/pyDes/blob/e988a5ffc9abb8010fc75dba54904d1c5dbe83db/pyDes.py#L437
    #  1. encode data as ASCII
    #  2. check perm table
    d = DES()
    data = "Robert".encode("ascii")
    print('Data in bits: ', text_to_bits(data))
    cipher = d.encrypt(data)
    print('Encrypted: ', cipher[0])
    [print(bits_to_text(m)) for m in cipher]
    decryption = d.decrypt(cipher[0])
    print(decryption)
