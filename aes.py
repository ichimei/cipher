#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

S_BOX = (
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
)

INV_S_BOX = (
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
)

RCON_VAL = (None, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36)

def byte_mul(a, b):
    res = 0
    while b > 0:
        if b & 1:
            res ^= a
        if a & 0x80:
            a = (a << 1) ^ 0x11b
        else:
            a <<= 1
        b >>= 1
    return res

def num_to_bytes(num, size):
    byts = [0] * size
    for i in range(size-1, -1, -1):
        byts[i] = num & 0xff
        num >>= 8
    return byts

def bytes_to_num(byts):
    num = 0
    for byt in byts:
        num <<= 8
        num |= byt
    return num

def rcon(i):
    return [RCON_VAL[i], 0x00, 0x00, 0x00]

def sub_word(word):
    return [S_BOX[elem] for elem in word]

def rot_word(word):
    return word[1:] + word[:1]

def xor_vec(a, b, size):
    return [a[i] ^ b[i] for i in range(size)]

def bytes_to_blocks(bstr, size):
    return [bytes_to_num(bstr[size*i:size*(i+1)]) for i in range(len(bstr) // size)]

def blocks_to_bytes(blks, size):
    return bytes(sum([num_to_bytes(num, size) for num in blks], []))

class AESInputError(Exception):
    pass

class AESDataError(Exception):
    pass

class AESPaddingError(Exception):
    pass

class AES:
    def __init__(self, keylen, key=None):
        if not (isinstance(keylen, int) and keylen in (128, 192, 256) and \
                (key is None or isinstance(key, int) and 0 <= key < 1 << keylen)):
            raise AESInputError

        if key is None:
            key = random.randrange(1 << keylen)
        self._key = key
        self._keylen = keylen
        self._keysize = keylen // 8
        self._nk = keylen // 32
        self._nb = 4
        self._blklen = 128
        self._blksize = 16
        self._nr = self._nk + 6
        self._key_schedule()

    def enc(self, msg):
        if not (isinstance(msg, int) and 0 <= msg < 1 << self._blklen):
            raise AESInputError

        return self._enc(msg)

    def dec(self, ciph):
        if not (isinstance(ciph, int) and 0 <= ciph < 1 << self._blklen):
            raise AESInputError

        return self._dec(ciph)

    def getkey(self):
        return self._key

    def _key_schedule(self):
        w = [0] * (self._nb * (self._nr+1))
        keys = num_to_bytes(self._key, self._keysize)

        for i in range(self._nk):
            w[i] = keys[4*i : 4*i+4]

        for i in range(self._nk, self._nb * (self._nr+1)):
            temp = w[i-1]
            if i % self._nk == 0:
                temp = xor_vec(sub_word(rot_word(temp)), rcon(i // self._nk), 4)
            elif self._nk > 6 and i % self._nk == 4:
                temp = sub_word(temp)
            w[i] = xor_vec(w[i-self._nk], temp, 4)

        self._w = w

    def _enc(self, msg):
        state = num_to_bytes(msg, self._blksize)
        state = self._add_round_key(state, self._w[:self._nb])

        for rnd in range(1, self._nr):
            state = self._sub_bytes(state)
            state = self._shift_rows(state)
            state = self._mix_columns(state)
            state = self._add_round_key(state, self._w[rnd*self._nb : (rnd+1)*self._nb])

        state = self._sub_bytes(state)
        state = self._shift_rows(state)
        state = self._add_round_key(state, self._w[self._nr*self._nb:])

        return bytes_to_num(state)

    def _dec(self, ciph):
        state = num_to_bytes(ciph, self._blksize)
        state = self._add_round_key(state, self._w[self._nr*self._nb:])

        for rnd in range(self._nr-1, 0, -1):
            state = self._inv_shift_rows(state)
            state = self._inv_sub_bytes(state)
            state = self._add_round_key(state, self._w[rnd*self._nb : (rnd+1)*self._nb])
            state = self._inv_mix_columns(state)

        state = self._inv_shift_rows(state)
        state = self._inv_sub_bytes(state)
        state = self._add_round_key(state, self._w[:self._nb])

        return bytes_to_num(state)

    def _sub_bytes(self, state):
        return [S_BOX[elem] for elem in state]

    def _inv_sub_bytes(self, state):
        return [INV_S_BOX[elem] for elem in state]

    def _shift_rows(self, state):
        new_state = [0] * self._blksize
        for c in range(self._nb):
            for r in range(4):
                new_state[4*c+r] = state[4*((c+r)%self._nb)+r]
        return new_state

    def _inv_shift_rows(self, state):
        new_state = [0] * self._blksize
        for c in range(self._nb):
            for r in range(4):
                new_state[4*c+r] = state[4*((c-r)%self._nb)+r]
        return new_state

    def _mix_columns(self, state):
        new_state = [0] * self._blksize
        for c in range(self._nb):
            new_state[4*c]   = byte_mul(state[4*c],   0x02) ^ \
                               byte_mul(state[4*c+1], 0x03) ^ \
                                        state[4*c+2]        ^ \
                                        state[4*c+3]
            new_state[4*c+1] =          state[4*c]          ^ \
                               byte_mul(state[4*c+1], 0x02) ^ \
                               byte_mul(state[4*c+2], 0x03) ^ \
                                        state[4*c+3]
            new_state[4*c+2] =          state[4*c]          ^ \
                                        state[4*c+1]        ^ \
                               byte_mul(state[4*c+2], 0x02) ^ \
                               byte_mul(state[4*c+3], 0x03)
            new_state[4*c+3] = byte_mul(state[4*c],   0x03) ^ \
                                        state[4*c+1]        ^ \
                                        state[4*c+2]        ^ \
                               byte_mul(state[4*c+3], 0x02)
        return new_state

    def _inv_mix_columns(self, state):
        new_state = [0] * self._blksize
        for c in range(self._nb):
            new_state[4*c]   = byte_mul(state[4*c],   0x0e) ^ \
                               byte_mul(state[4*c+1], 0x0b) ^ \
                               byte_mul(state[4*c+2], 0x0d) ^ \
                               byte_mul(state[4*c+3], 0x09)
            new_state[4*c+1] = byte_mul(state[4*c+1], 0x0e) ^ \
                               byte_mul(state[4*c+2], 0x0b) ^ \
                               byte_mul(state[4*c+3], 0x0d) ^ \
                               byte_mul(state[4*c],   0x09)
            new_state[4*c+2] = byte_mul(state[4*c+2], 0x0e) ^ \
                               byte_mul(state[4*c+3], 0x0b) ^ \
                               byte_mul(state[4*c],   0x0d) ^ \
                               byte_mul(state[4*c+1], 0x09)
            new_state[4*c+3] = byte_mul(state[4*c+3], 0x0e) ^ \
                               byte_mul(state[4*c],   0x0b) ^ \
                               byte_mul(state[4*c+1], 0x0d) ^ \
                               byte_mul(state[4*c+2], 0x09)
        return new_state

    def _add_round_key(self, state, words):
        return xor_vec(state, sum(words, []), self._blksize)

class AESCBC(AES):
    def encfile(self, infile, outfile, iv=0, pad=True):
        if not (isinstance(infile, str) and isinstance(outfile, str) and \
                isinstance(iv, int) and 0 <= iv < 1 << self._blklen and \
                isinstance(pad, bool)):
            raise AESInputError

        with open(infile, 'rb') as infi:
            inbytes = infi.read()

        inlen = len(inbytes)
        blksize = self._blksize
        if pad:
            npad = blksize - inlen % blksize
            inbytes += bytes([npad] * npad)
            inlen += npad
        elif inlen % blksize > 0:
            raise AESPaddingError

        inblks = bytes_to_blocks(inbytes, blksize)
        nblks = len(inblks)
        outblks = [0] * nblks
        prev = iv
        for i in range(nblks):
            outblks[i] = self._enc(inblks[i] ^ prev)
            prev = outblks[i]
        outbytes = blocks_to_bytes(outblks, blksize)

        with open(outfile, 'wb') as outfi:
            outfi.write(outbytes)

    def decfile(self, infile, outfile, iv=0, pad=True):
        if not (isinstance(infile, str) and isinstance(outfile, str) and \
                isinstance(iv, int) and 0 <= iv < 1 << self._blklen and \
                isinstance(pad, bool)):
            raise AESInputError

        with open(infile, 'rb') as infi:
            inbytes = infi.read()

        inlen = len(inbytes)
        blksize = self._blksize
        if inlen % blksize > 0:
            raise AESDataError
        if pad and inlen == 0:
            raise AESPaddingError

        inblks = bytes_to_blocks(inbytes, blksize)
        nblks = len(inblks)
        outblks = [0] * nblks
        prev = iv
        for i in range(nblks):
            outblks[i] = self._dec(inblks[i]) ^ prev
            prev = inblks[i]
        outbytes = blocks_to_bytes(outblks, blksize)

        if pad:
            npad = outbytes[-1]
            if not 1 <= npad <= 16:
                raise AESPaddingError
            padded = outbytes[-npad:-1]
            for pad in padded:
                if pad != npad:
                    raise AESPaddingError
            outbytes = outbytes[:-npad]

        with open(outfile, 'wb') as outfi:
            outfi.write(outbytes)

def test():
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    msg = 0x3243f6a8885a308d313198a2e0370734
    ciph_ans = 0x3925841d02dc09fbdc118597196a0b32

    aes = AES(128, key)
    ciph = aes.enc(msg)
    assert ciph == ciph_ans
    msg2 = aes.dec(ciph)
    assert msg == msg2

def test2():
    msg_file = 'file.m'
    ciph_file = 'file.c'
    msg2_file = 'file2.m'
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    msg = 0x3243f6a8885a308d313198a2e0370734face
    ciph_ans = 0x3925841d02dc09fbdc118597196a0b32f4a3358aa7c61ced508f3435fe67f854

    aes = AESCBC(128, key)
    with open(msg_file, 'wb') as f:
        f.write(msg.to_bytes(18, 'big'))

    aes.encfile(msg_file, ciph_file)
    with open(ciph_file, 'rb') as f:
        ciph = int.from_bytes(f.read(), 'big')
    assert ciph == ciph_ans

    aes.decfile(ciph_file, msg2_file)
    with open(msg2_file, 'rb') as f:
        msg2 = int.from_bytes(f.read(), 'big')
    assert msg == msg2

if __name__ == '__main__':
    test()
    test2()
