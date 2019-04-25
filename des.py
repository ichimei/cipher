#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# Selection tables are declared below.
IP = (
    58, 50, 42, 34, 26, 18, 10,  2,
    60, 52, 44, 36, 28, 20, 12,  4,
    62, 54, 46, 38, 30, 22, 14,  6,
    64, 56, 48, 40, 32, 24, 16,  8,
    57, 49, 41, 33, 25, 17,  9,  1,
    59, 51, 43, 35, 27, 19, 11,  3,
    61, 53, 45, 37, 29, 21, 13,  5,
    63, 55, 47, 39, 31, 23, 15,  7
)
IIP = (
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
)
E = (
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
)
P = (
    16,  7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
)
S1 = (
    14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
     0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
     4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
    15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
)
S2 = (
    15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
     3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
     0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
    13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9
)
S3 = (
    10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
    13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
    13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
     1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12
)
S4 = (
     7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
    13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
    10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
     3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
)
S5 = (
     2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
    14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
     4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
    11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
)
S6 = (
    12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
    10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
     9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
     4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
)
S7 = (
     4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
    13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
     1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
     6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
)
S8 = (
    13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
     1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
     7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
     2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
)
PC1 = (
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4
)
PC2 = (
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)
# Note: The index starts from 1.
Lshift = (None, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1)

def check_len(src, leng):
    """
    Check if `src` is an integer which has length `leng`.
    Raise an error if not.
    """
    if not isinstance(src, int):
        raise ValueError('{} is not an integer'.format(src))
    if src not in range(1 << leng):
        raise ValueError('The value {} is not a valid {}-bit number'.format(src, leng))

def get_bit(src, ind, leng):
    """
    Get the `ind`th bit in `src` which has length `leng`.
    Returns that bit.
    """
    return (src >> (leng - ind)) & 1

def select_bits(src, inds, leng):
    """
    For every index `ind` in `inds`, select the `ind`th bit in `src` which has length `leng`, then concatenate all the bits into a single number.
    Returns that number.
    """
    bits = []
    for ind in inds:
        bits.append(get_bit(src, ind, leng))
    ret = 0
    for bit in bits:
        ret <<= 1
        ret |= bit
    return ret

def concat(*args):
    """
    Bitwisely concatenate numbers.
    The `args` may have 1 or 2n arguments.
    - 1 argument: That argument is an iterable with 2n elements. Treat them as 2n arguments.
    - 2n arguments: The first n arguments are n numbers to concatenate, and the last n ones are their lengths. For the i'th (0 <= i < n) number, the (i+n)'th argument is its length.
    Returns the concatenated number.
    """
    if len(args) == 1:
        args = args[0]
    n = len(args) // 2
    ret = 0
    for i in range(0, n):
        src = args[i]
        leng = args[i+n]
        ret <<= leng
        ret |= src
    return ret

def split(src, *lengs):
    """
    Split `src` to a list of numbers.
    The `lengs` may have 1 or n (n > 1) arguments.
    - 1 argument: That argument is an iterable with n elements. Treat them as n arguments.
    - n arguments: Represents the lengths of each number which is splitted into. The sum of the lengths is considered as the length of `src`.
    Return a list of the numbers which is splitted into.
    """
    if len(lengs) == 1:
        lengs = lengs[0]
    ret = []
    for leng in reversed(lengs):
        bits = src & ((1 << leng) - 1)
        ret.insert(0, bits)
        src >>= leng
    return ret

def rotate_left(src, num, leng):
    """
    Rotate `src` (which has length `leng`) left by `num` bits.
    Return the rotated value.
    """
    return ((src << num) | (src >> (leng - num))) & ((1 << leng) - 1)

def key_schedule(key):
    """
    Given the master key `key`, run the key schedule and generate sub-keys.
    Return a list of sub-keys.
    """
    subkey = [None] * 17
    C = [None] * 17
    D = [None] * 17
    C[0] = select_bits(key, PC1[0:28], 64)
    D[0] = select_bits(key, PC1[28:56], 64)
    for i in range(1, 17):
        C[i] = rotate_left(C[i-1], Lshift[i], 28)
        D[i] = rotate_left(D[i-1], Lshift[i], 28)
        subkey[i] = select_bits(concat(C[i], D[i], 28, 28), PC2, 56)
    return subkey

def S_box(i, B):
    """
    The function for the `i`th (0 <= i < 8) S-box given the input `B`.
    Returns the value of the function.
    """
    S_list = (S1, S2, S3, S4, S5, S6, S7, S8)
    a = select_bits(B, (1, 6), 6)
    b = select_bits(B, (2, 3, 4, 5), 6)
    return S_list[i][a * 16 + b]

def cipher_func(r, subkey):
    """
    The cipher function f(R[i-1], K[i]). `r` is R[i-1] and `subkey` is K[i].
    Returns the value of the function.
    """
    r_extend = select_bits(r, E, 32)
    before_select = split(r_extend ^ subkey, [6] * 8)
    after_select = [S_box(i, before_select[i]) for i in range(8)]
    after_select = concat(after_select + [4] * 8)
    output = select_bits(after_select, P, 32)
    return output

class DES:
    """
    The Data Encryption Standard (DES) cipher.
    """
    def __init__(self, key = None):
        """
        Generate a key randomly if the `key` is None, or use the provided `key`. Then runs the key schedule.
        """
        if key is not None:
            check_len(key, 64)
            self.key = key
        else:
            self.key = random.randrange(1 << 64)
        self.subkey = key_schedule(self.key)

    def enc(self, msg):
        """
        Encrypt a 64-bit block message `msg` and return the ciphertext.
        """
        check_len(msg, 64)
        L = [None] * 17
        R = [None] * 17
        init_perm = select_bits(msg, IP, 64)
        L[0], R[0] = split(init_perm, 32, 32)
        for i in range(1, 17):
            L[i] = R[i-1]
            R[i] = L[i-1] ^ cipher_func(R[i-1], self.subkey[i])
        pre_output = concat(R[16], L[16], 32, 32)
        ciph = select_bits(pre_output, IIP, 64)
        return ciph

    def dec(self, ciph):
        """
        Decrypt a 64-bit block ciphertext `ciph` and return the plaintext.
        """
        L = [None] * 17
        R = [None] * 17
        pre_output = select_bits(ciph, IP, 64)
        R[16], L[16] = split(pre_output, 32, 32)
        for i in range(16, 0, -1):
            R[i-1] = L[i]
            L[i-1] = R[i] ^ cipher_func(L[i], self.subkey[i])
        init_perm = concat(L[0], R[0], 32, 32)
        msg = select_bits(init_perm, IIP, 64)
        return msg

class ArbiDES(DES):
    """
    The DES cipher, which accepts arbitrary long messages. For the sake of convenience, it takes a UTF-8 Python string as the input.
    Uses ECB and PKCS #5 Padding.
    Inherits from the DES class.
    """
    def enc(self, msg):
        """
        Encrypt a UTF-8 string message `msg` and return the ciphertext (list of blocks).
        """
        msg_bytes = list(msg.encode())
        num_padding = 8 - len(msg_bytes) % 8
        msg_bytes += [num_padding] * num_padding
        ciph = []
        for i in range(0, len(msg_bytes), 8):
            msg_block = concat(msg_bytes[i:i+8] + [8] * 8)
            ciph_block = DES.enc(self, msg_block)
            ciph.append(ciph_block)
        return ciph

    def dec(self, ciph):
        """
        Decrypt a ciphertext (list of blocks) `ciph` and return the plaintext (UTF-8 string).
        """
        msg_bytes = []
        for ciph_block in ciph:
            msg_block = DES.dec(self, ciph_block)
            msg_bytes += split(msg_block, [8] * 8)
        num_padding = msg_bytes[-1]
        msg_bytes = msg_bytes[0 : len(msg_bytes) - num_padding]
        msg = bytes(msg_bytes).decode()
        return msg

def fixed_hex(value, leng = 16):
    """
    Return a fixed length `leng` hexadecimal representation of a number `value`.
    """
    return '{0:#0{1}x}'.format(value, leng + 2)

def example_DES():
    """
    A simple example of the DES cipher.
    """
    print('======== Example of DES ========')
    print()
    des = DES()    # instantialize the DES cipher and generate a key
    m1 = random.randrange(1 << 64)    # generate a message randomly
    print('The key is:')
    print('k =', fixed_hex(des.key))
    print()
    print('The message is:')
    print('m1 =', fixed_hex(m1))
    print()
    c = des.enc(m1)
    print('We encrypted the above message. The ciphertext is:')
    print('c =', fixed_hex(c))
    print()
    m2 = des.dec(c)
    print('We decrypted the above ciphertext. The decrypted message is:')
    print('m2 =', fixed_hex(m2))
    print()
    print('The correctness holds, since m1 == m2 is', m1 == m2)
    print()

def example_ArbiDES():
    """
    A simple example of the arbitrary-input DES cipher.
    """
    print('======== Example of arbitrary-input DES ========')
    print()
    des = ArbiDES()    # instantialize the DES cipher and generate a key
    m1 = '这是一个使用万国码的字符串。This is a string using Unicode.'    # input a UTF-8 string
    print('The key is:')
    print('k =', fixed_hex(des.key))
    print()
    print('The message is:')
    print('m1 =', m1)
    print()
    c = des.enc(m1)
    print('We encrypted the above message. The ciphertext (list of blocks) is:')
    print('c = [{}]'.format(', '.join(fixed_hex(block) for block in c)))
    print()
    m2 = des.dec(c)
    print('We decrypted the above ciphertext. The decrypted message is:')
    print('m2 =', m2)
    print()
    print('The correctness holds, since m1 == m2 is', m1 == m2)
    print()

# run the examples
if __name__ == '__main__':
    example_DES()
    example_ArbiDES()
